from SyncDataProducts import SyncDataProducts


def lambda_handler(event, context):
    # Initialize SyncDataProducts
    sync_data_products = SyncDataProducts(
        sep_host=event['sep_host'],
        sep_password=event['sep_password'],
        sep_username=event['sep_username'],
        galaxy_host=event['galaxy_host'],
        galaxy_client_id=event['galaxy_client_id'],
        galaxy_client_secret=event['galaxy_client_secret'],
        galaxy_sql_username=event['galaxy_sql_username'],
        galaxy_sql_password=event['galaxy_sql_password'],
        galaxy_sql_cluster_url=event['galaxy_sql_cluster_url'],
        data_product_catalog=event['data_product_catalog'],
        default_cluster=event['default_cluster']
    )

    # Wake cluster
    sync_data_products.galaxy_wake_cluster()

    return event
