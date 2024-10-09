# coding: utf-8

"""
    Starburst Galaxy Public API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PaginatedTag(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'next_page_token': 'str',
        'result': 'list[Tag]'
    }

    attribute_map = {
        'next_page_token': 'nextPageToken',
        'result': 'result'
    }

    def __init__(self, next_page_token=None, result=None):  # noqa: E501
        """PaginatedTag - a model defined in Swagger"""  # noqa: E501
        self._next_page_token = None
        self._result = None
        self.discriminator = None
        if next_page_token is not None:
            self.next_page_token = next_page_token
        if result is not None:
            self.result = result

    @property
    def next_page_token(self):
        """Gets the next_page_token of this PaginatedTag.  # noqa: E501

        The next page token to use or \"\" if there are no more pages.  # noqa: E501

        :return: The next_page_token of this PaginatedTag.  # noqa: E501
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this PaginatedTag.

        The next page token to use or \"\" if there are no more pages.  # noqa: E501

        :param next_page_token: The next_page_token of this PaginatedTag.  # noqa: E501
        :type: str
        """

        self._next_page_token = next_page_token

    @property
    def result(self):
        """Gets the result of this PaginatedTag.  # noqa: E501

        A page of results.  # noqa: E501

        :return: The result of this PaginatedTag.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this PaginatedTag.

        A page of results.  # noqa: E501

        :param result: The result of this PaginatedTag.  # noqa: E501
        :type: list[Tag]
        """

        self._result = result

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PaginatedTag, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PaginatedTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
