from starburstapi.sep.api import Api as SepApi
from starburstapi.sep.data import DataProduct as SepDataProduct
from starburstapi.sep.data import MaterializedView as SepMaterializedView

from starburstapi.galaxy.api import Api as GalaxyApi
from starburstapi.galaxy.models import CreateDataProductRequest, Link

from starburstapi.shared.api import ApiException

from trino.dbapi import connect as trino_connect
from trino.auth import BasicAuthentication

import json


class SyncDataProducts:
    def __init__(self,
                 sep_host: str,
                 sep_username: str,
                 sep_password: str,
                 galaxy_host: str,
                 galaxy_client_id: str,
                 galaxy_client_secret: str,
                 galaxy_sql_username: str,
                 galaxy_sql_password: str,
                 galaxy_sql_cluster_url: str,
                 data_product_catalog: str,
                 default_cluster: str,
                 galaxy_api_key: str = None,
                 data_product_catalog_id: str = None,
                 default_cluster_id: str = None):

        self.sep_api = SepApi(host=sep_host, username=sep_username, password=sep_password)
        self.sep_trino_connection = trino_connect(
            host=sep_host,
            port=443,
            user=sep_username,
            catalog='system',
            http_scheme="https",
            auth=BasicAuthentication(sep_username, sep_password)
        )
        self.galaxy_api = GalaxyApi(
            host=galaxy_host,
            client_id=galaxy_client_id,
            client_secret=galaxy_client_secret,
            username=galaxy_sql_username,
            password=galaxy_sql_password,
            cluster=default_cluster,
            default_catalog=data_product_catalog
        )

        if data_product_catalog_id is None:
            self.data_product_catalog_id = self.galaxy_api.get_catalog_id_for_name(data_product_catalog)
            if self.data_product_catalog_id is None:
                raise ValueError(f'Could not look up id for catalog {data_product_catalog}')
        else:
            self.data_product_catalog_id = data_product_catalog_id
        self.data_product_catalog = data_product_catalog

        self.galaxy_host = galaxy_host

        if default_cluster_id is None:
            self.default_cluster_id = self.galaxy_api.get_cluster_by_name(default_cluster).clusterId
            if self.default_cluster_id is None:
                raise ValueError(f'Could not look up cluster id for {default_cluster}')
        else:
            self.default_cluster_id = default_cluster_id

        self.galaxy_trino_client_connection = trino_connect(
            host=galaxy_sql_cluster_url,
            port=443,
            user=galaxy_sql_username,
            catalog=data_product_catalog,
            auth=BasicAuthentication(galaxy_sql_username, galaxy_sql_password),
            http_scheme="https"
        )

        self.galaxy_data_products = None

    def galaxy_get_data_product_by_name(self, name: str):
        return self.galaxy_api.get_data_product_id_by_name(name)

    def galaxy_create_schema(self, schema: str):
        cursor = self.galaxy_trino_client_connection.cursor()
        cursor.execute(
            f"create schema if not exists {self.data_product_catalog}.{schema}"
        )
        result = cursor.fetchall()

    def galaxy_create_view_dataset(
            self,
            definition_query: str,
            catalog_name: str,
            schema_name: str,
            view_name: str,
            or_replace: bool = False):
        cursor = self.galaxy_trino_client_connection.cursor()
        execution = cursor.execute(f'''
        CREATE {'OR REPLACE' if or_replace else ''} VIEW {catalog_name}.{schema_name}.{view_name} 
        as 
        {definition_query}
        ''')
        result = execution.fetchall()

    def galaxy_create_materialized_view_dataset(
            self,
            sep_mv: SepMaterializedView,
            data_product_catalog_name: str,
            target_catalog_name: str,
            schema_name: str):
        cursor = self.sep_trino_connection.cursor()
        execution = cursor.execute(f"""
        select storage_catalog || '.' || storage_schema || '.' || storage_table 
        from system.metadata.materialized_views 
        where catalog_name='{data_product_catalog_name}' AND schema_name = '{schema_name}' and name = '{sep_mv.name}'
        and storage_table IS NOT NULL
        """)
        query_results = execution.fetchall()
        if len(query_results) == 0 or query_results == '..':
            print(f'''
            No storage table found for materialized view {data_product_catalog_name}.{schema_name}.{sep_mv.name}!
            Refresh the materialized view. If it is not populated after the next data product synchronization 
            completes, report this issue.
            ''')
        if len(query_results) > 1:
            raise Exception(f'''
            Multiple materialized views found for {data_product_catalog_name}.{schema_name}.{sep_mv.name}!
            {"""
            """.join(query_results)}
            ''')
        storage_table = query_results[0][0]
        self.galaxy_create_view_dataset(
            definition_query=f'SELECT * FROM {storage_table} /*SEP MATERIALIZED VIEW STORAGE TABLE*/',
            catalog_name=target_catalog_name,
            schema_name=schema_name,
            view_name=sep_mv.name,
            or_replace=True
        )

    def galaxy_sync_datasets(self, sep_data_product: SepDataProduct, replace_view_if_exists: bool = False):
        for view in sep_data_product.views:
            print(f'Updating view {view.name}')
            self.galaxy_create_view_dataset(
                definition_query=view.definitionQuery,
                catalog_name=self.data_product_catalog,
                schema_name=sep_data_product.schemaName,
                view_name=view.name,
                or_replace=replace_view_if_exists
            )
        for mv in sep_data_product.materializedViews:
            # TODO: freshness check or something else to make sure the view has been populated?
            print(f'Updating materialized view {mv.name}')
            self.galaxy_create_materialized_view_dataset(
                sep_mv=mv,
                data_product_catalog_name=sep_data_product.catalogName,
                target_catalog_name=self.data_product_catalog,
                schema_name=sep_data_product.schemaName
            )

    def galaxy_update_data_product(self, sep_data_product: SepDataProduct):
        emails = ([product_owner.email for product_owner in sep_data_product.productOwners or []] +
                  [owner.email for owner in sep_data_product.owners or []])

        create_data_product_request = CreateDataProductRequest(
            name=sep_data_product.name,
            summary=sep_data_product.summary,
            description=sep_data_product.description,
            catalogId=self.galaxy_api.get_default_catalog_id(),
            schemaName=sep_data_product.schemaName,
            contacts=self.galaxy_api.emails_to_users(emails),
            links=[Link(uri=relevantLink.url, name=relevantLink.label)
                   for relevantLink in sep_data_product.relevantLinks],
            defaultClusterId=self.default_cluster_id
        )
        self.galaxy_api.update_data_product(create_data_product_request)
        self.galaxy_sync_datasets(sep_data_product=sep_data_product, replace_view_if_exists=True)

    def galaxy_create_data_product(self, sep_data_product: SepDataProduct):
        self.galaxy_create_schema(sep_data_product.schemaName)
        try:
            emails = ([product_owner.email for product_owner in sep_data_product.productOwners or []] +
                      [owner.email for owner in sep_data_product.owners or []])

            create_data_product_request = CreateDataProductRequest(
                name=sep_data_product.name,
                summary=sep_data_product.summary,
                description=sep_data_product.description,
                catalogId=self.galaxy_api.get_default_catalog_id(),
                schemaName=sep_data_product.schemaName,
                contacts=self.galaxy_api.emails_to_users(emails),
                links=[Link(uri=relevantLink.url, name=relevantLink.label)
                       for relevantLink in sep_data_product.relevantLinks],
                defaultClusterId=self.default_cluster_id
            )
            self.galaxy_api.create_data_product(create_data_product_request)
            self.galaxy_sync_datasets(sep_data_product=sep_data_product, replace_view_if_exists=False)
        except ApiException as e:
            if e.reason.lower() == 'conflict' and json.loads(e.body)['status'] == 'ALREADY_EXISTS':
                print(f'Data Product {sep_data_product.name} already exists. Updating.')
                self.galaxy_update_data_product(sep_data_product)
            else:
                raise e

    def galaxy_delete_data_product(self, data_product_id: str):
        self.galaxy_api.delete_data_product(data_product_id=data_product_id)

    def galaxy_wake_cluster(self):
        cursor = self.galaxy_trino_client_connection.cursor()
        result = cursor.execute("SELECT 'wake up - data product sync'")
        result.fetchall()

    def galaxy_list_data_products(self):
        return self.galaxy_api.list_data_products()
