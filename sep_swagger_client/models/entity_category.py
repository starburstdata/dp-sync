# coding: utf-8

"""
    Starburst Enterprise API documentation

    Documentation with details about endpoints and entities.  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EntityCategory(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    TABLES = "TABLES"
    SCHEMA_PROPERTIES = "SCHEMA_PROPERTIES"
    TABLE_PROPERTIES = "TABLE_PROPERTIES"
    SYSTEM_SESSION_PROPERTIES = "SYSTEM_SESSION_PROPERTIES"
    CATALOG_SESSION_PROPERTIES = "CATALOG_SESSION_PROPERTIES"
    FUNCTIONS = "FUNCTIONS"
    PROCEDURES = "PROCEDURES"
    QUERIES = "QUERIES"
    ROLES = "ROLES"
    USERS = "USERS"
    DATA_PRODUCTS = "DATA_PRODUCTS"
    AUDIT_LOGS = "AUDIT_LOGS"
    SYSTEM_INFORMATION = "SYSTEM_INFORMATION"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """EntityCategory - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None

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
        if issubclass(EntityCategory, dict):
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
        if not isinstance(other, EntityCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
