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

class Policy(object):
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
        'policy_id': 'str',
        'role_id': 'str',
        'name': 'str',
        'predicate': 'str',
        'description': 'str',
        'expiration': 'datetime',
        'scopes': 'list[Scopes]',
        'created': 'datetime',
        'modified': 'datetime'
    }

    attribute_map = {
        'sync_token': 'syncToken',
        'policy_id': 'policyId',
        'role_id': 'roleId',
        'name': 'name',
        'predicate': 'predicate',
        'description': 'description',
        'expiration': 'expiration',
        'scopes': 'scopes',
        'created': 'created',
        'modified': 'modified'
    }

    def __init__(self, sync_token=None, policy_id=None, role_id=None, name=None, predicate=None, description=None, expiration=None, scopes=None, created=None, modified=None):  # noqa: E501
        """Policy - a model defined in Swagger"""  # noqa: E501
        self._sync_token = None
        self._policy_id = None
        self._role_id = None
        self._name = None
        self._predicate = None
        self._description = None
        self._expiration = None
        self._scopes = None
        self._created = None
        self._modified = None
        self.discriminator = None
        self.sync_token = sync_token
        self.policy_id = policy_id
        self.role_id = role_id
        self.name = name
        self.predicate = predicate
        self.description = description
        if expiration is not None:
            self.expiration = expiration
        self.scopes = scopes
        self.created = created
        self.modified = modified

    @property
    def sync_token(self):
        """Gets the sync_token of this Policy.  # noqa: E501

        Used to ensure consistency for resource updates. A syncToken that is returned from the server is valid until the resource is updated when a new syncToken will be generated. Only the latest version of the object is maintained.  (read only)  # noqa: E501

        :return: The sync_token of this Policy.  # noqa: E501
        :rtype: str
        """
        return self._sync_token

    @sync_token.setter
    def sync_token(self, sync_token):
        """Sets the sync_token of this Policy.

        Used to ensure consistency for resource updates. A syncToken that is returned from the server is valid until the resource is updated when a new syncToken will be generated. Only the latest version of the object is maintained.  (read only)  # noqa: E501

        :param sync_token: The sync_token of this Policy.  # noqa: E501
        :type: str
        """
        if sync_token is None:
            raise ValueError("Invalid value for `sync_token`, must not be `None`")  # noqa: E501

        self._sync_token = sync_token

    @property
    def policy_id(self):
        """Gets the policy_id of this Policy.  # noqa: E501

        Policy ID (read only)  # noqa: E501

        :return: The policy_id of this Policy.  # noqa: E501
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this Policy.

        Policy ID (read only)  # noqa: E501

        :param policy_id: The policy_id of this Policy.  # noqa: E501
        :type: str
        """
        if policy_id is None:
            raise ValueError("Invalid value for `policy_id`, must not be `None`")  # noqa: E501

        self._policy_id = policy_id

    @property
    def role_id(self):
        """Gets the role_id of this Policy.  # noqa: E501

        Enabling role ID  # noqa: E501

        :return: The role_id of this Policy.  # noqa: E501
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this Policy.

        Enabling role ID  # noqa: E501

        :param role_id: The role_id of this Policy.  # noqa: E501
        :type: str
        """
        if role_id is None:
            raise ValueError("Invalid value for `role_id`, must not be `None`")  # noqa: E501

        self._role_id = role_id

    @property
    def name(self):
        """Gets the name of this Policy.  # noqa: E501

        Policy name  # noqa: E501

        :return: The name of this Policy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Policy.

        Policy name  # noqa: E501

        :param name: The name of this Policy.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def predicate(self):
        """Gets the predicate of this Policy.  # noqa: E501

        Policy predicate  # noqa: E501

        :return: The predicate of this Policy.  # noqa: E501
        :rtype: str
        """
        return self._predicate

    @predicate.setter
    def predicate(self, predicate):
        """Sets the predicate of this Policy.

        Policy predicate  # noqa: E501

        :param predicate: The predicate of this Policy.  # noqa: E501
        :type: str
        """
        if predicate is None:
            raise ValueError("Invalid value for `predicate`, must not be `None`")  # noqa: E501

        self._predicate = predicate

    @property
    def description(self):
        """Gets the description of this Policy.  # noqa: E501

        Policy description  # noqa: E501

        :return: The description of this Policy.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Policy.

        Policy description  # noqa: E501

        :param description: The description of this Policy.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def expiration(self):
        """Gets the expiration of this Policy.  # noqa: E501

        Policy expiration  # noqa: E501

        :return: The expiration of this Policy.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this Policy.

        Policy expiration  # noqa: E501

        :param expiration: The expiration of this Policy.  # noqa: E501
        :type: datetime
        """

        self._expiration = expiration

    @property
    def scopes(self):
        """Gets the scopes of this Policy.  # noqa: E501


        :return: The scopes of this Policy.  # noqa: E501
        :rtype: list[Scopes]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this Policy.


        :param scopes: The scopes of this Policy.  # noqa: E501
        :type: list[Scopes]
        """
        if scopes is None:
            raise ValueError("Invalid value for `scopes`, must not be `None`")  # noqa: E501

        self._scopes = scopes

    @property
    def created(self):
        """Gets the created of this Policy.  # noqa: E501

        Created on (read only)  # noqa: E501

        :return: The created of this Policy.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Policy.

        Created on (read only)  # noqa: E501

        :param created: The created of this Policy.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this Policy.  # noqa: E501

        Modified on (read only)  # noqa: E501

        :return: The modified of this Policy.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this Policy.

        Modified on (read only)  # noqa: E501

        :param modified: The modified of this Policy.  # noqa: E501
        :type: datetime
        """
        if modified is None:
            raise ValueError("Invalid value for `modified`, must not be `None`")  # noqa: E501

        self._modified = modified

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
        if issubclass(Policy, dict):
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
        if not isinstance(other, Policy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other