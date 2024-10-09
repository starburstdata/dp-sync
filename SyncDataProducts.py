import sep_swagger_client
from sep_swagger_client.models import DataProductSummary as SepDataProductSummary
from sep_swagger_client.models import MaterializedViewDataset as SepMaterializedViewDataset
from sep_swagger_client.models import DataProduct as SepDataProduct
from SepAuthConfiguration import SepAuthConfiguration

import galaxy_swagger_client
from galaxy_swagger_client.rest import ApiException as GalaxyApiException
from GalaxyAuthConfiguration import GalaxyAuthConfiguration

from trino.dbapi import connect as trino_connect
from trino.auth import BasicAuthentication

from typing import cast, List
from dataclasses import dataclass, asdict
import datetime
import json
import requests


@dataclass
class Contact:
    userId: str
    email: str

    def to_dict(self):
        return asdict(self)


@dataclass
class Link:
    name: str
    uri: str

    def to_dict(self):
        return asdict(self)


@dataclass
class CreateDataProductRequestBody:
    name: str
    summary: str
    description: str
    catalogId: str
    schemaName: str
    contacts: List[dict]
    links: List[dict]
    defaultClusterId: str


class SyncDataProducts:
    def __init__(self, sep_host: str,
                 sep_username: str,
                 sep_password: str,
                 galaxy_host: str,
                 galaxy_client_id: str,
                 galaxy_client_secret: str,
                 galaxy_sql_username: str,
                 galaxy_sql_password: str,
                 galaxy_sql_cluster_url: str,
                 data_product_catalog: str,
                 default_cluster: str):
        sep_configuration = SepAuthConfiguration()
        sep_configuration.host = sep_host
        sep_configuration.username = sep_username
        sep_configuration.password = sep_password
        sep_api_client = sep_swagger_client.ApiClient(configuration=sep_configuration)
        self.sep_api_instance = sep_swagger_client.DataProductsApi(api_client=sep_api_client)
        self.sep_trino_connection = trino_connect(
            host=sep_host,
            port=443,
            user=sep_username,
            catalog='system',
            auth=BasicAuthentication(sep_username, sep_password)
        )

        api_key_response = requests.post(url=f'{galaxy_host}/oauth/v2/token',
                                         auth=(galaxy_client_id, galaxy_client_secret),
                                         headers={'Content-Type': 'application/x-www-form-urlencoded'},
                                         data='grant_type=client_credentials')
        self.galaxy_api_key = api_key_response.json()['access_token']
        galaxy_configuration = GalaxyAuthConfiguration()
        galaxy_configuration.api_key = {'accessToken': self.galaxy_api_key}
        galaxy_configuration.host = galaxy_host
        galaxy_api_client = galaxy_swagger_client.ApiClient(galaxy_configuration)
        self.galaxy_host = galaxy_host
        self.galaxy_data_product_api_instance = galaxy_swagger_client.DataProductServiceApi(galaxy_api_client)
        self.galaxy_users_api_instance = galaxy_swagger_client.UserServiceApi(galaxy_api_client)

        galaxy_catalog_api_client = galaxy_swagger_client.CatalogServiceApi(galaxy_api_client)
        catalogs = galaxy_catalog_api_client.list_catalog().result
        self.data_product_catalog_id = next(iter(
            [catalog.catalog_id for catalog in catalogs if catalog.catalog_name == data_product_catalog]), None)
        if self.data_product_catalog_id is None:
            raise ValueError(f'Could not look up id for catalog {data_product_catalog}')
        self.data_product_catalog = data_product_catalog

        galaxy_cluster_api_client = galaxy_swagger_client.ClusterServiceApi(galaxy_api_client)
        clusters = galaxy_cluster_api_client.list_cluster().result

        self.default_cluster_id = next(iter(
            [cluster.cluster_id for cluster in clusters if cluster.name == default_cluster]), None)
        if self.default_cluster_id is None:
            raise ValueError(f'Could not look up cluster id for {default_cluster}')

        self.galaxy_trino_client_connection = trino_connect(
            host=galaxy_sql_cluster_url,
            port=443,
            user=galaxy_sql_username,
            catalog=data_product_catalog,
            auth=BasicAuthentication(galaxy_sql_username, galaxy_sql_password)
        )

        self.galaxy_data_products = None

    def galaxy_get_data_product_by_name(self, name: str):
        return next(iter([dp for dp in self.galaxy_list_data_products() if dp.name == name]))

    def galaxy_list_data_products(self):
        if self.galaxy_data_products is None:
            self.galaxy_data_products = self.galaxy_data_product_api_instance.list_data_product().result
        return self.galaxy_data_products

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
            sep_mv: SepMaterializedViewDataset,
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
        if len(query_results) == 0:
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

    def __prepare_data_product_request__(self, sep_data_product: SepDataProduct):
        users_list = self.galaxy_users_api_instance.list_user().result
        emails = ([product_owner.email for product_owner in sep_data_product.product_owners or []] +
                  [owner.email for owner in sep_data_product.owners or []])
        contacts = [Contact(userId=user.user_id, email=user.email).to_dict()
                    for user in users_list if user.email in emails]
        return CreateDataProductRequestBody(
            name=sep_data_product.name,
            summary=sep_data_product.summary,
            description=sep_data_product.description,
            catalogId=self.data_product_catalog_id,
            schemaName=sep_data_product.schema_name,
            contacts= contacts,
            links=[Link(link.label, link.uri).to_dict() for link in sep_data_product.relevant_links or []],
            defaultClusterId=self.default_cluster_id
        )

    def galaxy_sync_datasets(self, sep_data_product: SepDataProduct, replace_view_if_exists: bool = False):
        for view in sep_data_product.views:
            print(f'Updating view {view.name}')
            self.galaxy_create_view_dataset(
                definition_query=view.definition_query,
                catalog_name=self.data_product_catalog,
                schema_name=sep_data_product.schema_name,
                view_name=view.name,
                or_replace=replace_view_if_exists
            )
        for mv in sep_data_product.materialized_views:
            # TODO: freshness check or something else to make sure the view has been populated?
            print(f'Updating materialized view {mv.name}')
            self.galaxy_create_materialized_view_dataset(
                sep_mv=mv,
                data_product_catalog_name=sep_data_product.catalog_name,
                target_catalog_name=self.data_product_catalog,
                schema_name=sep_data_product.schema_name
            )

    def galaxy_update_data_product(self, sep_data_product: SepDataProduct):
        data_product_request_body = self.__prepare_data_product_request__(sep_data_product)
        galaxy_data_product = self.galaxy_get_data_product_by_name(sep_data_product.name)
        response = self.galaxy_data_product_api_instance.patch_update_data_product(
            body=data_product_request_body.__dict__, data_product_id=galaxy_data_product.data_product_id)
        self.galaxy_sync_datasets(sep_data_product=sep_data_product, replace_view_if_exists=True)

    def galaxy_create_data_product(self, sep_data_product: SepDataProduct):
        self.galaxy_create_schema(sep_data_product.schema_name)
        data_product_request_body = self.__prepare_data_product_request__(sep_data_product)
        try:
            # Galaxy APIs expect dicts, and transform them to json internally. A json string will result in an
            # error with an inscrutable error message
            response = self.galaxy_data_product_api_instance.create_data_product(
                body=data_product_request_body.__dict__)
            self.galaxy_sync_datasets(sep_data_product=sep_data_product, replace_view_if_exists=False)
        except GalaxyApiException as e:
            if e.reason.lower() == 'conflict' and json.loads(e.body)['status'] == 'ALREADY_EXISTS':
                print(f'Data Product {sep_data_product.name} already exists. Updating.')
                self.galaxy_update_data_product(sep_data_product)
            else:
                raise e

    def galaxy_delete_data_product(self, data_product_id: str):
        self.galaxy_data_product_api_instance.delete_data_product(data_product_id=data_product_id)

    def galaxy_wake_cluster(self):
        cursor = self.galaxy_trino_client_connection.cursor()
        result = cursor.execute("SELECT 'wake up - data product sync'")
        result.fetchall()
