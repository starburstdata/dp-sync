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

class User(object):
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
        'sync_token': 'str',
        'user_id': 'str',
        'email': 'str',
        'default_role_id': 'str',
        'created_on': 'datetime',
        'scim_managed': 'bool',
        'directly_granted_roles': 'list[DirectlyGrantedRoles]',
        'all_roles': 'list[DirectlyGrantedRoles]'
    }

    attribute_map = {
        'sync_token': 'syncToken',
        'user_id': 'userId',
        'email': 'email',
        'default_role_id': 'defaultRoleId',
        'created_on': 'createdOn',
        'scim_managed': 'scimManaged',
        'directly_granted_roles': 'directlyGrantedRoles',
        'all_roles': 'allRoles'
    }

    def __init__(self, sync_token=None, user_id=None, email=None, default_role_id=None, created_on=None, scim_managed=None, directly_granted_roles=None, all_roles=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501
        self._sync_token = None
        self._user_id = None
        self._email = None
        self._default_role_id = None
        self._created_on = None
        self._scim_managed = None
        self._directly_granted_roles = None
        self._all_roles = None
        self.discriminator = None
        self.sync_token = sync_token
        self.user_id = user_id
        self.email = email
        if default_role_id is not None:
            self.default_role_id = default_role_id
        self.created_on = created_on
        self.scim_managed = scim_managed
        self.directly_granted_roles = directly_granted_roles
        self.all_roles = all_roles

    @property
    def sync_token(self):
        """Gets the sync_token of this User.  # noqa: E501

        Used to ensure consistency for resource updates. A syncToken that is returned from the server is valid until the resource is updated when a new syncToken will be generated. Only the latest version of the object is maintained.  (read only)  # noqa: E501

        :return: The sync_token of this User.  # noqa: E501
        :rtype: str
        """
        return self._sync_token

    @sync_token.setter
    def sync_token(self, sync_token):
        """Sets the sync_token of this User.

        Used to ensure consistency for resource updates. A syncToken that is returned from the server is valid until the resource is updated when a new syncToken will be generated. Only the latest version of the object is maintained.  (read only)  # noqa: E501

        :param sync_token: The sync_token of this User.  # noqa: E501
        :type: str
        """
        if sync_token is None:
            raise ValueError("Invalid value for `sync_token`, must not be `None`")  # noqa: E501

        self._sync_token = sync_token

    @property
    def user_id(self):
        """Gets the user_id of this User.  # noqa: E501

        User ID (read only)  # noqa: E501

        :return: The user_id of this User.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this User.

        User ID (read only)  # noqa: E501

        :param user_id: The user_id of this User.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501

        User email (read only)  # noqa: E501

        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.

        User email (read only)  # noqa: E501

        :param email: The email of this User.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def default_role_id(self):
        """Gets the default_role_id of this User.  # noqa: E501

        Default role id (read only)  # noqa: E501

        :return: The default_role_id of this User.  # noqa: E501
        :rtype: str
        """
        return self._default_role_id

    @default_role_id.setter
    def default_role_id(self, default_role_id):
        """Sets the default_role_id of this User.

        Default role id (read only)  # noqa: E501

        :param default_role_id: The default_role_id of this User.  # noqa: E501
        :type: str
        """

        self._default_role_id = default_role_id

    @property
    def created_on(self):
        """Gets the created_on of this User.  # noqa: E501

        Creation date (read only)  # noqa: E501

        :return: The created_on of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this User.

        Creation date (read only)  # noqa: E501

        :param created_on: The created_on of this User.  # noqa: E501
        :type: datetime
        """
        if created_on is None:
            raise ValueError("Invalid value for `created_on`, must not be `None`")  # noqa: E501

        self._created_on = created_on

    @property
    def scim_managed(self):
        """Gets the scim_managed of this User.  # noqa: E501

        SCIM managed (read only)  # noqa: E501

        :return: The scim_managed of this User.  # noqa: E501
        :rtype: bool
        """
        return self._scim_managed

    @scim_managed.setter
    def scim_managed(self, scim_managed):
        """Sets the scim_managed of this User.

        SCIM managed (read only)  # noqa: E501

        :param scim_managed: The scim_managed of this User.  # noqa: E501
        :type: bool
        """
        if scim_managed is None:
            raise ValueError("Invalid value for `scim_managed`, must not be `None`")  # noqa: E501

        self._scim_managed = scim_managed

    @property
    def directly_granted_roles(self):
        """Gets the directly_granted_roles of this User.  # noqa: E501


        :return: The directly_granted_roles of this User.  # noqa: E501
        :rtype: list[DirectlyGrantedRoles]
        """
        return self._directly_granted_roles

    @directly_granted_roles.setter
    def directly_granted_roles(self, directly_granted_roles):
        """Sets the directly_granted_roles of this User.


        :param directly_granted_roles: The directly_granted_roles of this User.  # noqa: E501
        :type: list[DirectlyGrantedRoles]
        """
        if directly_granted_roles is None:
            raise ValueError("Invalid value for `directly_granted_roles`, must not be `None`")  # noqa: E501

        self._directly_granted_roles = directly_granted_roles

    @property
    def all_roles(self):
        """Gets the all_roles of this User.  # noqa: E501


        :return: The all_roles of this User.  # noqa: E501
        :rtype: list[DirectlyGrantedRoles]
        """
        return self._all_roles

    @all_roles.setter
    def all_roles(self, all_roles):
        """Sets the all_roles of this User.


        :param all_roles: The all_roles of this User.  # noqa: E501
        :type: list[DirectlyGrantedRoles]
        """
        if all_roles is None:
            raise ValueError("Invalid value for `all_roles`, must not be `None`")  # noqa: E501

        self._all_roles = all_roles

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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
