from SyncDataProducts import SyncDataProducts
import datetime
from typing import cast, List
from sep_swagger_client.models import DataProductSummary as SepDataProductSummary
from sep_swagger_client.models import DataProduct as SepDataProduct
import boto3


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

    # Retrieve previous run timestamp from Secrets Manager
    secrets_manager = boto3.client('secretsmanager')
    secret_name = "data-product-sync-timestamp"
    try:
        response = secrets_manager.get_secret_value(SecretId=secret_name)
        previous_run_timestamp = datetime.datetime.fromisoformat(response['SecretString'])
    except:
        previous_run_timestamp = -1

    search_time = datetime.datetime.now(tz=datetime.UTC)

    # Search for data products
    data_product_search_results = cast(List[SepDataProductSummary],
                                       sync_data_products.sep_api_instance.search_data_products())

    for data_product_summary in data_product_search_results:
        data_product = cast(SepDataProduct,
                            sync_data_products.sep_api_instance.get_data_product(data_product_summary.id))

        if data_product.created_at > previous_run_timestamp:
            sync_data_products.galaxy_create_data_product(data_product)
        elif data_product.updated_at > previous_run_timestamp:
            sync_data_products.galaxy_update_data_product(data_product)

    # Pass the event forward
    event['search_time'] = search_time.isoformat()
    return event
