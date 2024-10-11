import requests
import json
from typing import List, Any, cast
from starburstapi.galaxy.models import CreateDataProductRequest, Cluster, User, Contact, Catalog, DataProduct
from dataclasses import dataclass
import marshmallow_dataclass
from urllib.parse import quote_plus
from starburstapi.shared.api import ApiException


@dataclass
class PaginatedResponse:
    nextPageToken: str
    result: List[Any]


class Api:
    def __init__(self,
                 client_id: str,
                 client_secret: str,
                 username: str, password: str,
                 host: str,
                 cluster: str,
                 default_catalog: str,
                 api_key: str = None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password
        self.url = host
        self.cluster = cluster
        self.default_catalog = default_catalog
        if api_key is not None:
            self.api_key = api_key
        else:
            self.api_key = self.__get_api_key__(url=host, client_id=client_id, client_secret=client_secret)

        self.__data_products_list__ = None
        self.__default_catalog_id__: str = None
        self.__users_list__ = None

    def get_default_catalog_id(self):
        if self.__default_catalog_id__ is None:
            self.__default_catalog_id__ = self.get_catalog_id_for_name(self.default_catalog)
        return self.__default_catalog_id__

    def __get_api_key__(self, url: str, client_id: str, client_secret: str):
        api_key_response = requests.post(url=f'{url}/oauth/v2/token',
                                         auth=(client_id, client_secret),
                                         headers={'Content-Type': 'application/x-www-form-urlencoded'},
                                         data='grant_type=client_credentials')
        return api_key_response.json()['access_token']

    def delete_data_product(self, data_product_name: str = None, data_product_id: str = None):
        if data_product_id is None:
            if data_product_name is None:
                raise ValueError('Either data product name or id must be provided')
            else:
                data_product_id = self.get_data_product_id_by_name(data_product_name)
        PATH = f'public/api/v1/dataProduct/{data_product_id}'
        response = requests.delete(
            f'{self.url}/{PATH}',
            headers={'Authorization': f'bearer {self.api_key}'}
        )

        if not response.ok:
            raise ApiException(
                f'Could not create data product: {response.reason}. Status code {response.status_code}',
                reason=response.reason,
                status=response.status_code,
                body=response.text
            )


    def create_data_product(self, data_product_request: CreateDataProductRequest):
        PATH = 'public/api/v1/dataProduct'
        response = requests.post(
            f'{self.url}/{PATH}',
            headers={'Authorization': f'bearer {self.api_key}', "Content-type": "application/json"},
            data=data_product_request.to_json()
        )
        if not response.ok:
            raise ApiException(
                f'Could not create data product: {response.reason}. Status code {response.status_code}',
                reason=response.reason,
                status=response.status_code,
                body=response.text
            )

    def update_data_product(self, data_product_request: CreateDataProductRequest):
        data_product_id = self.get_data_product_id_by_name(data_product_request.name)
        PATH = f'public/api/v1/dataProduct/{data_product_id}'
        response = requests.patch(
            f'{self.url}/{PATH}',
            headers={'Authorization': f'bearer {self.api_key}', "Content-type": "application/json"},
            data=data_product_request.to_json()
        )
        if not response.ok:
            raise ApiException(
                f'Could not create data product: {response.reason}. Status code {response.status_code}',
                reason=response.reason,
                status=response.status_code,
                body=response.text
            )

    def get_data_product_id_by_name(self, data_product_name: str):
        return next(iter([dp.dataProductId for dp in self.list_data_products() if dp.name == data_product_name]))

    def list_data_products(self):
        PATH = 'public/api/v1/dataProduct'
        if self.__data_products_list__ is None:
            data_product_search_result_schema = marshmallow_dataclass.class_schema(DataProduct)()
            data_product_response = self.__get_paginated_response__(
                f'{self.url}/{PATH}',
                headers={'Authorization': f'bearer {self.api_key}'})
            self.__data_products_list__ = cast(List[DataProduct],
                                               [data_product_search_result_schema.load(dp)
                                                for dp in data_product_response])
        return self.__data_products_list__

    def __list_catalogs__(self):
        PATH = 'public/api/v1/catalog'
        catalog_schema = marshmallow_dataclass.class_schema(Catalog)()
        catalog_response = self.__get_paginated_response__(
            f'{self.url}/{PATH}',
            headers={'Authorization': f'bearer {self.api_key}'}
        )
        return cast(List[Catalog], [catalog_schema.load(catalog) for catalog in catalog_response])

    def get_catalog_id_for_name(self, name: str):
        catalogs = self.__list_catalogs__()
        return next(iter([catalog.catalogId for catalog in catalogs if catalog.catalogName == name]), None)

    def __list_clusters__(self):
        PATH = 'public/api/v1/cluster'
        cluster_schema = marshmallow_dataclass.class_schema(Cluster)()
        cluster_response = self.__get_paginated_response__(
            f'{self.url}/{PATH}',
            headers={'Authorization': f'bearer {self.api_key}'}
        )
        return cast(List[Cluster], [cluster_schema.load(cluster) for cluster in cluster_response])

    def get_cluster_by_name(self, name: str):
        encoded_name = f'name={quote_plus(name)}'
        PATH = f'public/api/v1/cluster/{encoded_name}'
        cluster_schema = marshmallow_dataclass.class_schema(Cluster)()
        cluster_response = requests.get(f'{self.url}/{PATH}',
                headers= {'Authorization': f'bearer {self.api_key}'}
        ).json()
        return cast(Cluster, cluster_schema.load(cluster_response))

    def __list_users__(self):
        PATH = 'public/api/v1/user'
        if self.__users_list__ is None:
            users_schema = marshmallow_dataclass.class_schema(User)()
            users_response = self.__get_paginated_response__(
                                                        f'{self.url}/{PATH}',
                                                        headers={'Authorization': f'bearer {self.api_key}'})
            self.__users_list__ = cast(List[User], [users_schema.load(user) for user in users_response])
        return self.__users_list__

    def emails_to_users(self, emails: List[str]):
        return [Contact(userId=user.userId, email=user.email)
                    for user in self.__list_users__() if user.email in emails]

    def __get_user_by_email(self, email: str):
        encoded_name = f'email={quote_plus(email)}'
        user_schema = marshmallow_dataclass.class_schema(User)()

        PATH = f'public/api/v1/user/{encoded_name}'
        return cast(User, user_schema.load(requests.get(f'{self.url}/{PATH}',
                                                        headers={'Authorization': f'bearer {self.api_key}'}
                                                        ).json()))

    def __get_paginated_response__(self, url: str, headers: {}):
        response = requests.get(url=url, headers=headers)
        paginated_response_schema = marshmallow_dataclass.class_schema(PaginatedResponse)()
        paginated_response = cast(PaginatedResponse, paginated_response_schema.load(response.json()))
        results = paginated_response.result
        while paginated_response.nextPageToken is not None and paginated_response.nextPageToken.strip() != '':
            response = requests.get(url=url, headers=headers, params={'pageToken': paginated_response.nextPageToken})
            paginated_response = cast(PaginatedResponse, paginated_response_schema.load(response.json()))
            results += paginated_response.result
        return results
