from SyncDataProducts import SyncDataProducts
from typing import cast
from starburstapi.sep.data import DataProduct as SepDataProduct


def lambda_handler(event, context):
    # Initialize SyncDataProducts
    sync_data_products = SyncDataProducts(
        sep_host=event['event']['sep_host'],
        sep_password=event['event']['sep_password'],
        sep_username=event['event']['sep_username'],
        galaxy_host=event['event']['galaxy_host'],
        galaxy_client_id=event['event']['galaxy_client_id'],
        galaxy_client_secret=event['event']['galaxy_client_secret'],
        galaxy_sql_username=event['event']['galaxy_sql_username'],
        galaxy_sql_password=event['event']['galaxy_sql_password'],
        galaxy_sql_cluster_url=event['event']['galaxy_sql_cluster_url'],
        data_product_catalog=event['event']['data_product_catalog'],
        default_cluster=event['event']['default_cluster']
    )

    try:
        data_product = cast(SepDataProduct,
                            sync_data_products.sep_api.get_data_product(event['id']))
        sync_data_products.galaxy_create_data_product(data_product)
        print(f'New data_product {data_product.name} successfully created')
    except Exception as e:
        print(f'Could not create data_product: {e}')
