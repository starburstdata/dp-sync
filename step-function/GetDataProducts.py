from SyncDataProductsCustomApi import SyncDataProductsCustomApi
import datetime
import pickle
from base64 import b64encode, b64decode
from typing import cast, List
from starburstapi.sep.data import DataProductSearchResult as SepDataProductSearchResult
import boto3


def lambda_handler(event, context):
    # Initialize SyncDataProducts
    sync_data_products = SyncDataProductsCustomApi(
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
    secret_name = "dp-sync/data-product-sync-last-run-timestamp"
    try:
        response = secrets_manager.get_secret_value(SecretId=secret_name)
        decoded_response = b64decode(response['SecretString'])
        previous_run_timestamp = pickle.loads(decoded_response)
    except Exception as e:
        print(f'Could not read previous run timestamp. Starting from beginning of time. Error: {e}')
        previous_run_timestamp = datetime.datetime(1970, 1, 1, 0, 0, 0, 0, datetime.UTC)

    search_time = datetime.datetime.now(tz=datetime.UTC)

    # Search for data products
    data_product_search_results = sync_data_products.sep_api.search_data_products()
    data_products = {
        'new': [],  # {'event': event, 'data_product_ids':[]},
        'modified': [],  # {'event': event, 'data_product_ids':[]},
        'unmodified': []  # {'event': event, 'data_product_ids':[]}
    }

    for data_product_summary in data_product_search_results:
        if data_product_summary.createdAt > previous_run_timestamp:
            data_products['new'].append(
                {'event': event, 'id': data_product_summary.id})
        elif data_product_summary.updatedAt > previous_run_timestamp:
            data_products['modified'].append(
                {'event': event, 'id': data_product_summary.id})
        else:
            data_products['unmodified'].append(
                {'event': event, 'id': data_product_summary.id})

    response = secrets_manager.put_secret_value(
        SecretId=secret_name,
        SecretString=b64encode(pickle.dumps(search_time)).decode("utf-8"))
    return data_products
