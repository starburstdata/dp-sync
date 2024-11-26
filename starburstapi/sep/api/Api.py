from starburstapi.sep.data import DataProductSearchResult
from starburstapi.sep.data import DataProduct
import requests
from typing import cast, List
from json import dumps


class Api:

    DATA_PRODUCT_PATH = 'api/v1/dataProduct/products'

    def __init__(self, host: str, username: str, password: str, protocol: str = 'https'):
        if '://' in host:
            raise ValueError(f'Hostname should not include protocol')
        self.host = host
        self.username = username
        self.password = password
        self.protocol = protocol

    def search_data_products(self, search_string=None) -> List[DataProductSearchResult]:
        #REQUEST searchOptions.searchString is bookended by '%' and compared against all
        #dp attributes https://github.com/starburstdata/starburst-enterprise/blob/807dbbbfb48b7e5ea87777fc3aae8cd360dea1e8/core/starburst-server-main/src/main/java/com/starburstdata/presto/dataproduct/search/SearchSqlBuilder.java#L213

        params = {'searchOptions': dumps({'searchString': search_string})} if search_string is not None else None
        response = requests.get(url=f'{self.protocol}://{self.host}/{self.DATA_PRODUCT_PATH}',
                                auth=(self.username, self.password), params=params)
        if not response.ok:
            raise Exception(f'Request returned code {response.status_code}.\nResponse body: {response.text}')

        return [search_result for search_result in
                [cast(DataProductSearchResult, DataProductSearchResult.load(result)) for result in response.json()]
                if search_string is None or search_string in search_result.name]

    def get_data_product(self, dp_id) -> DataProduct:
        response = requests.get(url= f'{self.protocol}://{self.host}/{self.DATA_PRODUCT_PATH}/{dp_id}',
                                auth=(self.username, self.password))
        if not response.ok:
            raise Exception('bad request' + str(response))
        return cast(DataProduct, DataProduct.load(response.json()))
