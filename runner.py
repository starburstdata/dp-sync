from SyncDataProducts import SyncDataProducts
import datetime
from typing import cast, List
from starburstapi.sep.data import DataProductSearchResult as SepDataProductSearchResult
from starburstapi.sep.data import DataProduct as SepDataProduct

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
    parser.add_argument("--search-string")
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
                                          default_cluster=args.default_cluster,
                                          data_product_tag_name='dp_sync'
                                          )

    sync_data_products.galaxy_wake_cluster()
    run_timestamp_file_path = '/tmp/dp-sync-timestamp.pickle'
    try:
        #raise FileNotFoundError # uncomment to run from t = 0
        previous_run_timestamp = pickle.load(open(run_timestamp_file_path, 'rb'))
    except FileNotFoundError:
        previous_run_timestamp = datetime.datetime(1970,1,1,0,0,0, 0, datetime.UTC)
    search_time = datetime.datetime.now(tz=datetime.UTC)

    data_product_search_results = cast(List[SepDataProductSearchResult],
                                       sync_data_products.sep_api.search_data_products(args.search_string))
    for data_product_summary in data_product_search_results:
        data_product = cast(SepDataProduct,
                            sync_data_products.sep_api.get_data_product(data_product_summary.id))
        if data_product.createdAt > previous_run_timestamp:
            print(f'Creating new Galaxy Data Product: {data_product.name}')
            sync_data_products.galaxy_create_data_product(data_product)
        elif data_product.updatedAt > previous_run_timestamp:
            print(f'Updating Galaxy Data Product: {data_product.name}')
            sync_data_products.galaxy_update_data_product(data_product)
        else:
            print(f'Refreshing materialized views for Galaxy Data Product: {data_product.name}')
            sync_data_products.galaxy_sync_datasets(data_product, True)

    sep_data_product_names = set([dp.name for dp in data_product_search_results])
    for galaxy_data_product in sync_data_products.galaxy_list_data_products('dp_sync'):
        galaxy_data_product.to_json()
        print(f'evaluate {galaxy_data_product.name}')
        if galaxy_data_product.name not in sep_data_product_names:
            print(f'deleting {galaxy_data_product.name}')
            sync_data_products.galaxy_delete_data_product(data_product=galaxy_data_product)

    # Do not save timestamp unless updates complete without failures
    run_timestamp_file = open(run_timestamp_file_path, 'wb')
    pickle.dump(search_time, run_timestamp_file)
    run_timestamp_file.close()
