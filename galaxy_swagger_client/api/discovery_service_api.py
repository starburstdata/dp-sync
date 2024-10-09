# coding: utf-8

"""
    Starburst Galaxy Public API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from galaxy_swagger_client.api_client import ApiClient


class DiscoveryServiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_catalog_catalog_metadata(self, catalog_id, **kwargs):  # noqa: E501
        """get_catalog_catalog_metadata  # noqa: E501

        Return catalog metadata with any Galaxy added metadata  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_catalog_catalog_metadata(catalog_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog_id: - A catalog - This parameter can be looked up using `name` instead of its Id. Use `name=value` instead of an Id to lookup/search using the `value`. `value` must be encoded ([see RFC](https://www.rfc-editor.org/rfc/rfc3986#section-2.2) including `=`)  (required)
        :return: CatalogMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_catalog_catalog_metadata_with_http_info(catalog_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_catalog_catalog_metadata_with_http_info(catalog_id, **kwargs)  # noqa: E501
            return data

    def get_catalog_catalog_metadata_with_http_info(self, catalog_id, **kwargs):  # noqa: E501
        """get_catalog_catalog_metadata  # noqa: E501

        Return catalog metadata with any Galaxy added metadata  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_catalog_catalog_metadata_with_http_info(catalog_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog_id: - A catalog - This parameter can be looked up using `name` instead of its Id. Use `name=value` instead of an Id to lookup/search using the `value`. `value` must be encoded ([see RFC](https://www.rfc-editor.org/rfc/rfc3986#section-2.2) including `=`)  (required)
        :return: CatalogMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_catalog_catalog_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog_id' is set
        if ('catalog_id' not in params or
                params['catalog_id'] is None):
            raise ValueError("Missing the required parameter `catalog_id` when calling `get_catalog_catalog_metadata`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog_id' in params:
            path_params['catalogId'] = params['catalog_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken']  # noqa: E501

        return self.api_client.call_api(
            '/public/api/v1/catalog/{catalogId}/catalogMetadata', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CatalogMetadata',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_catalog_schema(self, catalog_id, **kwargs):  # noqa: E501
        """list_catalog_schema  # noqa: E501

        Return a catalog's schemas along with any Galaxy added metadata  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_catalog_schema(catalog_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog_id: - A catalog - This parameter can be looked up using `name` instead of its Id. Use `name=value` instead of an Id to lookup/search using the `value`. `value` must be encoded ([see RFC](https://www.rfc-editor.org/rfc/rfc3986#section-2.2) including `=`)  (required)
        :param str page_token: Pagination Token
        :param int page_size: Page size or 0 for default (current maximum is 100)
        :return: PaginatedSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_catalog_schema_with_http_info(catalog_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_catalog_schema_with_http_info(catalog_id, **kwargs)  # noqa: E501
            return data

    def list_catalog_schema_with_http_info(self, catalog_id, **kwargs):  # noqa: E501
        """list_catalog_schema  # noqa: E501

        Return a catalog's schemas along with any Galaxy added metadata  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_catalog_schema_with_http_info(catalog_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog_id: - A catalog - This parameter can be looked up using `name` instead of its Id. Use `name=value` instead of an Id to lookup/search using the `value`. `value` must be encoded ([see RFC](https://www.rfc-editor.org/rfc/rfc3986#section-2.2) including `=`)  (required)
        :param str page_token: Pagination Token
        :param int page_size: Page size or 0 for default (current maximum is 100)
        :return: PaginatedSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog_id', 'page_token', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_catalog_schema" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog_id' is set
        if ('catalog_id' not in params or
                params['catalog_id'] is None):
            raise ValueError("Missing the required parameter `catalog_id` when calling `list_catalog_schema`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog_id' in params:
            path_params['catalogId'] = params['catalog_id']  # noqa: E501

        query_params = []
        if 'page_token' in params:
            query_params.append(('pageToken', params['page_token']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken']  # noqa: E501

        return self.api_client.call_api(
            '/public/api/v1/catalog/{catalogId}/schema', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedSchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_catalog_schema_table(self, catalog_id, schema_id, **kwargs):  # noqa: E501
        """list_catalog_schema_table  # noqa: E501

        Return a catalog schema's tables along with any Galaxy added metadata  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_catalog_schema_table(catalog_id, schema_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog_id: - A catalog - This parameter can be looked up using `name` instead of its Id. Use `name=value` instead of an Id to lookup/search using the `value`. `value` must be encoded ([see RFC](https://www.rfc-editor.org/rfc/rfc3986#section-2.2) including `=`)  (required)
        :param str schema_id: A schema from a catalog (required)
        :param str page_token: Pagination Token
        :param int page_size: Page size or 0 for default (current maximum is 100)
        :return: PaginatedTable
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_catalog_schema_table_with_http_info(catalog_id, schema_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_catalog_schema_table_with_http_info(catalog_id, schema_id, **kwargs)  # noqa: E501
            return data

    def list_catalog_schema_table_with_http_info(self, catalog_id, schema_id, **kwargs):  # noqa: E501
        """list_catalog_schema_table  # noqa: E501

        Return a catalog schema's tables along with any Galaxy added metadata  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_catalog_schema_table_with_http_info(catalog_id, schema_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog_id: - A catalog - This parameter can be looked up using `name` instead of its Id. Use `name=value` instead of an Id to lookup/search using the `value`. `value` must be encoded ([see RFC](https://www.rfc-editor.org/rfc/rfc3986#section-2.2) including `=`)  (required)
        :param str schema_id: A schema from a catalog (required)
        :param str page_token: Pagination Token
        :param int page_size: Page size or 0 for default (current maximum is 100)
        :return: PaginatedTable
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog_id', 'schema_id', 'page_token', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_catalog_schema_table" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog_id' is set
        if ('catalog_id' not in params or
                params['catalog_id'] is None):
            raise ValueError("Missing the required parameter `catalog_id` when calling `list_catalog_schema_table`")  # noqa: E501
        # verify the required parameter 'schema_id' is set
        if ('schema_id' not in params or
                params['schema_id'] is None):
            raise ValueError("Missing the required parameter `schema_id` when calling `list_catalog_schema_table`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog_id' in params:
            path_params['catalogId'] = params['catalog_id']  # noqa: E501
        if 'schema_id' in params:
            path_params['schemaId'] = params['schema_id']  # noqa: E501

        query_params = []
        if 'page_token' in params:
            query_params.append(('pageToken', params['page_token']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken']  # noqa: E501

        return self.api_client.call_api(
            '/public/api/v1/catalog/{catalogId}/schema/{schemaId}/table', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedTable',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_catalog_schema_table_column(self, catalog_id, schema_id, table_id, **kwargs):  # noqa: E501
        """list_catalog_schema_table_column  # noqa: E501

        Return a catalog table's columns along with any Galaxy added metadata  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_catalog_schema_table_column(catalog_id, schema_id, table_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog_id: - A catalog - This parameter can be looked up using `name` instead of its Id. Use `name=value` instead of an Id to lookup/search using the `value`. `value` must be encoded ([see RFC](https://www.rfc-editor.org/rfc/rfc3986#section-2.2) including `=`)  (required)
        :param str schema_id: A schema from a catalog (required)
        :param str table_id: A table from a catalog (required)
        :param str page_token: Pagination Token
        :param int page_size: Page size or 0 for default (current maximum is 100)
        :return: PaginatedColumn
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_catalog_schema_table_column_with_http_info(catalog_id, schema_id, table_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_catalog_schema_table_column_with_http_info(catalog_id, schema_id, table_id, **kwargs)  # noqa: E501
            return data

    def list_catalog_schema_table_column_with_http_info(self, catalog_id, schema_id, table_id, **kwargs):  # noqa: E501
        """list_catalog_schema_table_column  # noqa: E501

        Return a catalog table's columns along with any Galaxy added metadata  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_catalog_schema_table_column_with_http_info(catalog_id, schema_id, table_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog_id: - A catalog - This parameter can be looked up using `name` instead of its Id. Use `name=value` instead of an Id to lookup/search using the `value`. `value` must be encoded ([see RFC](https://www.rfc-editor.org/rfc/rfc3986#section-2.2) including `=`)  (required)
        :param str schema_id: A schema from a catalog (required)
        :param str table_id: A table from a catalog (required)
        :param str page_token: Pagination Token
        :param int page_size: Page size or 0 for default (current maximum is 100)
        :return: PaginatedColumn
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog_id', 'schema_id', 'table_id', 'page_token', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_catalog_schema_table_column" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog_id' is set
        if ('catalog_id' not in params or
                params['catalog_id'] is None):
            raise ValueError("Missing the required parameter `catalog_id` when calling `list_catalog_schema_table_column`")  # noqa: E501
        # verify the required parameter 'schema_id' is set
        if ('schema_id' not in params or
                params['schema_id'] is None):
            raise ValueError("Missing the required parameter `schema_id` when calling `list_catalog_schema_table_column`")  # noqa: E501
        # verify the required parameter 'table_id' is set
        if ('table_id' not in params or
                params['table_id'] is None):
            raise ValueError("Missing the required parameter `table_id` when calling `list_catalog_schema_table_column`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog_id' in params:
            path_params['catalogId'] = params['catalog_id']  # noqa: E501
        if 'schema_id' in params:
            path_params['schemaId'] = params['schema_id']  # noqa: E501
        if 'table_id' in params:
            path_params['tableId'] = params['table_id']  # noqa: E501

        query_params = []
        if 'page_token' in params:
            query_params.append(('pageToken', params['page_token']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken']  # noqa: E501

        return self.api_client.call_api(
            '/public/api/v1/catalog/{catalogId}/schema/{schemaId}/table/{tableId}/column', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedColumn',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)