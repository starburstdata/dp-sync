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

class DataProductCatalogDetails(object):
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
        'catalog_id': 'str',
        'catalog_name': 'str',
        'catalog_kind': 'str',
        'local_regions': 'list[str]'
    }

    attribute_map = {
        'catalog_id': 'catalogId',
        'catalog_name': 'catalogName',
        'catalog_kind': 'catalogKind',
        'local_regions': 'localRegions'
    }

    def __init__(self, catalog_id=None, catalog_name=None, catalog_kind=None, local_regions=None):  # noqa: E501
        """DataProductCatalogDetails - a model defined in Swagger"""  # noqa: E501
        self._catalog_id = None
        self._catalog_name = None
        self._catalog_kind = None
        self._local_regions = None
        self.discriminator = None
        self.catalog_id = catalog_id
        self.catalog_name = catalog_name
        self.catalog_kind = catalog_kind
        self.local_regions = local_regions

    @property
    def catalog_id(self):
        """Gets the catalog_id of this DataProductCatalogDetails.  # noqa: E501

        Catalog Id (read only)  # noqa: E501

        :return: The catalog_id of this DataProductCatalogDetails.  # noqa: E501
        :rtype: str
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        """Sets the catalog_id of this DataProductCatalogDetails.

        Catalog Id (read only)  # noqa: E501

        :param catalog_id: The catalog_id of this DataProductCatalogDetails.  # noqa: E501
        :type: str
        """
        if catalog_id is None:
            raise ValueError("Invalid value for `catalog_id`, must not be `None`")  # noqa: E501

        self._catalog_id = catalog_id

    @property
    def catalog_name(self):
        """Gets the catalog_name of this DataProductCatalogDetails.  # noqa: E501

        Name of the catalog (read only)  # noqa: E501

        :return: The catalog_name of this DataProductCatalogDetails.  # noqa: E501
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        """Sets the catalog_name of this DataProductCatalogDetails.

        Name of the catalog (read only)  # noqa: E501

        :param catalog_name: The catalog_name of this DataProductCatalogDetails.  # noqa: E501
        :type: str
        """
        if catalog_name is None:
            raise ValueError("Invalid value for `catalog_name`, must not be `None`")  # noqa: E501

        self._catalog_name = catalog_name

    @property
    def catalog_kind(self):
        """Gets the catalog_kind of this DataProductCatalogDetails.  # noqa: E501

        Kind of catalog (read only)  # noqa: E501

        :return: The catalog_kind of this DataProductCatalogDetails.  # noqa: E501
        :rtype: str
        """
        return self._catalog_kind

    @catalog_kind.setter
    def catalog_kind(self, catalog_kind):
        """Sets the catalog_kind of this DataProductCatalogDetails.

        Kind of catalog (read only)  # noqa: E501

        :param catalog_kind: The catalog_kind of this DataProductCatalogDetails.  # noqa: E501
        :type: str
        """
        if catalog_kind is None:
            raise ValueError("Invalid value for `catalog_kind`, must not be `None`")  # noqa: E501

        self._catalog_kind = catalog_kind

    @property
    def local_regions(self):
        """Gets the local_regions of this DataProductCatalogDetails.  # noqa: E501


        :return: The local_regions of this DataProductCatalogDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._local_regions

    @local_regions.setter
    def local_regions(self, local_regions):
        """Sets the local_regions of this DataProductCatalogDetails.


        :param local_regions: The local_regions of this DataProductCatalogDetails.  # noqa: E501
        :type: list[str]
        """
        if local_regions is None:
            raise ValueError("Invalid value for `local_regions`, must not be `None`")  # noqa: E501

        self._local_regions = local_regions

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
        if issubclass(DataProductCatalogDetails, dict):
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
        if not isinstance(other, DataProductCatalogDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other