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


class PolicyServiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_policy(self, body, **kwargs):  # noqa: E501
        """create_policy  # noqa: E501

        Create a policy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_policy(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreatePolicy body: (required)
        :param bool validate_only: If true validate only without taking any action
        :return: Policy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_policy_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_policy_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_policy_with_http_info(self, body, **kwargs):  # noqa: E501
        """create_policy  # noqa: E501

        Create a policy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_policy_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreatePolicy body: (required)
        :param bool validate_only: If true validate only without taking any action
        :return: Policy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'validate_only']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'validate_only' in params:
            query_params.append(('validateOnly', params['validate_only']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken']  # noqa: E501

        return self.api_client.call_api(
            '/public/api/v1/policy', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Policy',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_policy(self, policy_id, **kwargs):  # noqa: E501
        """delete_policy  # noqa: E501

        Delete a policy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_policy(policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: - A policy - This parameter can be looked up using `name` instead of its Id. Use `name=value` instead of an Id to lookup/search using the `value`. `value` must be encoded ([see RFC](https://www.rfc-editor.org/rfc/rfc3986#section-2.2) including `=`)  (required)
        :param bool validate_only: If true validate only without taking any action
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_policy_with_http_info(policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_policy_with_http_info(policy_id, **kwargs)  # noqa: E501
            return data

    def delete_policy_with_http_info(self, policy_id, **kwargs):  # noqa: E501
        """delete_policy  # noqa: E501

        Delete a policy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_policy_with_http_info(policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: - A policy - This parameter can be looked up using `name` instead of its Id. Use `name=value` instead of an Id to lookup/search using the `value`. `value` must be encoded ([see RFC](https://www.rfc-editor.org/rfc/rfc3986#section-2.2) including `=`)  (required)
        :param bool validate_only: If true validate only without taking any action
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'validate_only']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `delete_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyId'] = params['policy_id']  # noqa: E501

        query_params = []
        if 'validate_only' in params:
            query_params.append(('validateOnly', params['validate_only']))  # noqa: E501

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
            '/public/api/v1/policy/{policyId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_policy(self, policy_id, **kwargs):  # noqa: E501
        """get_policy  # noqa: E501

        Get a policy by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_policy(policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: - A policy - This parameter can be looked up using `name` instead of its Id. Use `name=value` instead of an Id to lookup/search using the `value`. `value` must be encoded ([see RFC](https://www.rfc-editor.org/rfc/rfc3986#section-2.2) including `=`)  (required)
        :return: Policy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_policy_with_http_info(policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_policy_with_http_info(policy_id, **kwargs)  # noqa: E501
            return data

    def get_policy_with_http_info(self, policy_id, **kwargs):  # noqa: E501
        """get_policy  # noqa: E501

        Get a policy by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_policy_with_http_info(policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: - A policy - This parameter can be looked up using `name` instead of its Id. Use `name=value` instead of an Id to lookup/search using the `value`. `value` must be encoded ([see RFC](https://www.rfc-editor.org/rfc/rfc3986#section-2.2) including `=`)  (required)
        :return: Policy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `get_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyId'] = params['policy_id']  # noqa: E501

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
            '/public/api/v1/policy/{policyId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Policy',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_policy(self, **kwargs):  # noqa: E501
        """list_policy  # noqa: E501

        Return all policies defined for your account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_policy(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_token: Pagination Token
        :param int page_size: Page size or 0 for default (current maximum is 100)
        :param str enabling_role_id: Query filter
        :return: PaginatedPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_policy_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_policy_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_policy_with_http_info(self, **kwargs):  # noqa: E501
        """list_policy  # noqa: E501

        Return all policies defined for your account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_policy_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_token: Pagination Token
        :param int page_size: Page size or 0 for default (current maximum is 100)
        :param str enabling_role_id: Query filter
        :return: PaginatedPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_token', 'page_size', 'enabling_role_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_policy" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_token' in params:
            query_params.append(('pageToken', params['page_token']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'enabling_role_id' in params:
            query_params.append(('enablingRoleId', params['enabling_role_id']))  # noqa: E501

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
            '/public/api/v1/policy', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedPolicy',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_update_policy(self, body, policy_id, **kwargs):  # noqa: E501
        """patch_update_policy  # noqa: E501

        Update a policy  Only include fields you wish to update. Missing or unrecognized fields are ignored.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_update_policy(body, policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdatePolicyPatch body: (required)
        :param str policy_id: - A policy - This parameter can be looked up using `name` instead of its Id. Use `name=value` instead of an Id to lookup/search using the `value`. `value` must be encoded ([see RFC](https://www.rfc-editor.org/rfc/rfc3986#section-2.2) including `=`)  (required)
        :param bool validate_only: If true validate only without taking any action
        :return: Policy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_update_policy_with_http_info(body, policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_update_policy_with_http_info(body, policy_id, **kwargs)  # noqa: E501
            return data

    def patch_update_policy_with_http_info(self, body, policy_id, **kwargs):  # noqa: E501
        """patch_update_policy  # noqa: E501

        Update a policy  Only include fields you wish to update. Missing or unrecognized fields are ignored.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_update_policy_with_http_info(body, policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdatePolicyPatch body: (required)
        :param str policy_id: - A policy - This parameter can be looked up using `name` instead of its Id. Use `name=value` instead of an Id to lookup/search using the `value`. `value` must be encoded ([see RFC](https://www.rfc-editor.org/rfc/rfc3986#section-2.2) including `=`)  (required)
        :param bool validate_only: If true validate only without taking any action
        :return: Policy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'policy_id', 'validate_only']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_update_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_update_policy`")  # noqa: E501
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `patch_update_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyId'] = params['policy_id']  # noqa: E501

        query_params = []
        if 'validate_only' in params:
            query_params.append(('validateOnly', params['validate_only']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken']  # noqa: E501

        return self.api_client.call_api(
            '/public/api/v1/policy/{policyId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Policy',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
