from SyncDataProducts import SyncDataProducts
from starburstapi.galaxy.models import DataProduct as GalaxyDataProduct


# test event must be updated every time with output from listtaggeddataproducts
# because dp ID will change every time that this lambda deletes it

def lambda_handler(event, context):
    sync_data_products = SyncDataProducts(
        sep_host=event['params']['sep_host'],
        sep_password=event['params']['sep_password'],
        sep_username=event['params']['sep_username'],
        galaxy_host=event['params']['galaxy_host'],
        galaxy_client_id=event['params']['galaxy_client_id'],
        galaxy_client_secret=event['params']['galaxy_client_secret'],
        galaxy_sql_username=event['params']['galaxy_sql_username'],
        galaxy_sql_password=event['params']['galaxy_sql_password'],
        galaxy_sql_cluster_url=event['params']['galaxy_sql_cluster_url'],
        data_product_catalog=event['params']['data_product_catalog'],
        default_cluster=event['params']['default_cluster'],
        data_product_tag_name=event['params'].get('tag')
    )

    galaxy_data_product = GalaxyDataProduct.load(event['dp'])
    sync_data_products.galaxy_delete_data_product(galaxy_data_product)
