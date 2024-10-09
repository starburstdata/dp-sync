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

class CreateUser(object):
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
        'email': 'str',
        'role_ids': 'list[str]',
        'role_id': 'str'
    }

    attribute_map = {
        'email': 'email',
        'role_ids': 'roleIds',
        'role_id': 'roleId'
    }

    def __init__(self, email=None, role_ids=None, role_id=None):  # noqa: E501
        """CreateUser - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._role_ids = None
        self._role_id = None
        self.discriminator = None
        self.email = email
        self.role_ids = role_ids
        self.role_id = role_id

    @property
    def email(self):
        """Gets the email of this CreateUser.  # noqa: E501

        Email (read only)  # noqa: E501

        :return: The email of this CreateUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CreateUser.

        Email (read only)  # noqa: E501

        :param email: The email of this CreateUser.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def role_ids(self):
        """Gets the role_ids of this CreateUser.  # noqa: E501


        :return: The role_ids of this CreateUser.  # noqa: E501
        :rtype: list[str]
        """
        return self._role_ids

    @role_ids.setter
    def role_ids(self, role_ids):
        """Sets the role_ids of this CreateUser.


        :param role_ids: The role_ids of this CreateUser.  # noqa: E501
        :type: list[str]
        """
        if role_ids is None:
            raise ValueError("Invalid value for `role_ids`, must not be `None`")  # noqa: E501

        self._role_ids = role_ids

    @property
    def role_id(self):
        """Gets the role_id of this CreateUser.  # noqa: E501

        Default role (read only)  # noqa: E501

        :return: The role_id of this CreateUser.  # noqa: E501
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this CreateUser.

        Default role (read only)  # noqa: E501

        :param role_id: The role_id of this CreateUser.  # noqa: E501
        :type: str
        """
        if role_id is None:
            raise ValueError("Invalid value for `role_id`, must not be `None`")  # noqa: E501

        self._role_id = role_id

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
        if issubclass(CreateUser, dict):
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
        if not isinstance(other, CreateUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other