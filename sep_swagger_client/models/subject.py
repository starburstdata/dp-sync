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

class Subject(object):
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
        'attributes': 'list[Attribute]',
        'subject_role_id': 'int',
        'user': 'str',
        'only_attribute': 'Attribute',
        'empty': 'bool',
        'keys': 'list[str]'
    }

    attribute_map = {
        'attributes': 'attributes',
        'subject_role_id': 'subjectRoleId',
        'user': 'user',
        'only_attribute': 'onlyAttribute',
        'empty': 'empty',
        'keys': 'keys'
    }

    def __init__(self, attributes=None, subject_role_id=None, user=None, only_attribute=None, empty=None, keys=None):  # noqa: E501
        """Subject - a model defined in Swagger"""  # noqa: E501
        self._attributes = None
        self._subject_role_id = None
        self._user = None
        self._only_attribute = None
        self._empty = None
        self._keys = None
        self.discriminator = None
        if attributes is not None:
            self.attributes = attributes
        if subject_role_id is not None:
            self.subject_role_id = subject_role_id
        if user is not None:
            self.user = user
        if only_attribute is not None:
            self.only_attribute = only_attribute
        if empty is not None:
            self.empty = empty
        if keys is not None:
            self.keys = keys

    @property
    def attributes(self):
        """Gets the attributes of this Subject.  # noqa: E501


        :return: The attributes of this Subject.  # noqa: E501
        :rtype: list[Attribute]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Subject.


        :param attributes: The attributes of this Subject.  # noqa: E501
        :type: list[Attribute]
        """

        self._attributes = attributes

    @property
    def subject_role_id(self):
        """Gets the subject_role_id of this Subject.  # noqa: E501


        :return: The subject_role_id of this Subject.  # noqa: E501
        :rtype: int
        """
        return self._subject_role_id

    @subject_role_id.setter
    def subject_role_id(self, subject_role_id):
        """Sets the subject_role_id of this Subject.


        :param subject_role_id: The subject_role_id of this Subject.  # noqa: E501
        :type: int
        """

        self._subject_role_id = subject_role_id

    @property
    def user(self):
        """Gets the user of this Subject.  # noqa: E501


        :return: The user of this Subject.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Subject.


        :param user: The user of this Subject.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def only_attribute(self):
        """Gets the only_attribute of this Subject.  # noqa: E501


        :return: The only_attribute of this Subject.  # noqa: E501
        :rtype: Attribute
        """
        return self._only_attribute

    @only_attribute.setter
    def only_attribute(self, only_attribute):
        """Sets the only_attribute of this Subject.


        :param only_attribute: The only_attribute of this Subject.  # noqa: E501
        :type: Attribute
        """

        self._only_attribute = only_attribute

    @property
    def empty(self):
        """Gets the empty of this Subject.  # noqa: E501


        :return: The empty of this Subject.  # noqa: E501
        :rtype: bool
        """
        return self._empty

    @empty.setter
    def empty(self, empty):
        """Sets the empty of this Subject.


        :param empty: The empty of this Subject.  # noqa: E501
        :type: bool
        """

        self._empty = empty

    @property
    def keys(self):
        """Gets the keys of this Subject.  # noqa: E501


        :return: The keys of this Subject.  # noqa: E501
        :rtype: list[str]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """Sets the keys of this Subject.


        :param keys: The keys of this Subject.  # noqa: E501
        :type: list[str]
        """

        self._keys = keys

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
        if issubclass(Subject, dict):
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
        if not isinstance(other, Subject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
