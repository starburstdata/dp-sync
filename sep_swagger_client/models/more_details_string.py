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
from sep_swagger_client.models.error_detail_type import ErrorDetailType  # noqa: F401,E501

class MoreDetailsString(ErrorDetailType):
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
        'message': 'str'
    }
    if hasattr(ErrorDetailType, "swagger_types"):
        swagger_types.update(ErrorDetailType.swagger_types)

    attribute_map = {
        'message': 'message'
    }
    if hasattr(ErrorDetailType, "attribute_map"):
        attribute_map.update(ErrorDetailType.attribute_map)

    def __init__(self, message=None, *args, **kwargs):  # noqa: E501
        """MoreDetailsString - a model defined in Swagger"""  # noqa: E501
        self._message = None
        self.discriminator = None
        if message is not None:
            self.message = message
        ErrorDetailType.__init__(self, *args, **kwargs)

    @property
    def message(self):
        """Gets the message of this MoreDetailsString.  # noqa: E501


        :return: The message of this MoreDetailsString.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this MoreDetailsString.


        :param message: The message of this MoreDetailsString.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if issubclass(MoreDetailsString, dict):
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
        if not isinstance(other, MoreDetailsString):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
