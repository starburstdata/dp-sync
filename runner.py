from SyncDataProducts import SyncDataProducts
import datetime
from typing import cast, List
from sep_swagger_client.models import DataProductSummary as SepDataProductSummary
from sep_swagger_client.models import DataProduct as SepDataProduct


if __name__ == '__main__':
    import pickle
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--sep-host")
    parser.add_argument("--sep-username")
    parser.add_argument("--sep-password")
    parser.add_argument("--galaxy-host")
    parser.add_argument("--galaxy-client-id")
    parser.add_argument("--galaxy-client-secret")
    parser.add_argument("--galaxy-sql-username")
    parser.add_argument("--galaxy-sql-password")
    parser.add_argument("--galaxy-sql-cluster_url")
    parser.add_argument("--data-product-catalog")
    parser.add_argument("--default-cluster")
    args = parser.parse_args()

    sync_data_products = SyncDataProducts(sep_host=args.sep_host,
                                          sep_password=args.sep_password,
                                          sep_username=args.sep_username,
                                          galaxy_host=args.galaxy_host,
                                          galaxy_client_id=args.galaxy_client_id,
                                          galaxy_client_secret=args.galaxy_client_secret,
                                          galaxy_sql_username=args.galaxy_sql_username,
                                          galaxy_sql_password=args.galaxy_sql_password,
                                          galaxy_sql_cluster_url=args.galaxy_sql_cluster_url,
                                          data_product_catalog=args.data_product_catalog,
                                          default_cluster=args.default_cluster
                                          )

    sync_data_products.galaxy_wake_cluster()

    run_timestamp_file_path = '/tmp/dp-sync-timestamp.pickle'
    try:
        previous_run_timestamp = pickle.load(open(run_timestamp_file_path, 'rb'))
    except FileNotFoundError:
        previous_run_timestamp = -1
    search_time = datetime.datetime.now(tz=datetime.UTC)

    data_product_search_results = cast(List[SepDataProductSummary],
                                       sync_data_products.sep_api_instance.search_data_products())
    for data_product_summary in data_product_search_results:
        data_product = cast(SepDataProduct,
                            sync_data_products.sep_api_instance.get_data_product(data_product_summary.id))
        if data_product.created_at > previous_run_timestamp:
            print(f'Creating new Galaxy Data Product: {data_product.name}')
            sync_data_products.galaxy_create_data_product(data_product)
        elif data_product.updated_at > previous_run_timestamp:
            print(f'Updating Galaxy Data Product: {data_product.name}')
            sync_data_products.galaxy_update_data_product(data_product)
        else:
            print(f'Refreshing materialized views for Galaxy Data Product: {data_product.name}')
            sync_data_products.galaxy_sync_datasets(data_product, True)

    sep_data_product_names = set([dp.name for dp in data_product_search_results])
    for galaxy_data_product in sync_data_products.galaxy_list_data_products():
        if galaxy_data_product.name not in sep_data_product_names:
            sync_data_products.galaxy_delete_data_product(data_product_id=galaxy_data_product.data_product_id)

    # Do not save timestamp unless updates complete without failures
    run_timestamp_file = open(run_timestamp_file_path, 'wb')
    pickle.dump(search_time, run_timestamp_file)
    run_timestamp_file.close()
