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

class RevokePrivilege(object):
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
        'entity_id': 'str',
        'entity_kind': 'str',
        'privilege': 'str',
        'schema_name': 'str',
        'table_name': 'str',
        'column_name': 'str',
        'revoke_action': 'str'
    }

    attribute_map = {
        'entity_id': 'entityId',
        'entity_kind': 'entityKind',
        'privilege': 'privilege',
        'schema_name': 'schemaName',
        'table_name': 'tableName',
        'column_name': 'columnName',
        'revoke_action': 'revokeAction'
    }

    def __init__(self, entity_id=None, entity_kind=None, privilege=None, schema_name=None, table_name=None, column_name=None, revoke_action=None):  # noqa: E501
        """RevokePrivilege - a model defined in Swagger"""  # noqa: E501
        self._entity_id = None
        self._entity_kind = None
        self._privilege = None
        self._schema_name = None
        self._table_name = None
        self._column_name = None
        self._revoke_action = None
        self.discriminator = None
        self.entity_id = entity_id
        self.entity_kind = entity_kind
        self.privilege = privilege
        if schema_name is not None:
            self.schema_name = schema_name
        if table_name is not None:
            self.table_name = table_name
        if column_name is not None:
            self.column_name = column_name
        self.revoke_action = revoke_action

    @property
    def entity_id(self):
        """Gets the entity_id of this RevokePrivilege.  # noqa: E501

        Entity ID  # noqa: E501

        :return: The entity_id of this RevokePrivilege.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this RevokePrivilege.

        Entity ID  # noqa: E501

        :param entity_id: The entity_id of this RevokePrivilege.  # noqa: E501
        :type: str
        """
        if entity_id is None:
            raise ValueError("Invalid value for `entity_id`, must not be `None`")  # noqa: E501

        self._entity_id = entity_id

    @property
    def entity_kind(self):
        """Gets the entity_kind of this RevokePrivilege.  # noqa: E501

        Entity kind  # noqa: E501

        :return: The entity_kind of this RevokePrivilege.  # noqa: E501
        :rtype: str
        """
        return self._entity_kind

    @entity_kind.setter
    def entity_kind(self, entity_kind):
        """Sets the entity_kind of this RevokePrivilege.

        Entity kind  # noqa: E501

        :param entity_kind: The entity_kind of this RevokePrivilege.  # noqa: E501
        :type: str
        """
        if entity_kind is None:
            raise ValueError("Invalid value for `entity_kind`, must not be `None`")  # noqa: E501
        allowed_values = ["Account", "Cluster", "Catalog", "Schema", "Table", "Column", "Location", "Function", "Tag", "Policy", "RowFilter", "DataProduct"]  # noqa: E501
        if entity_kind not in allowed_values:
            raise ValueError(
                "Invalid value for `entity_kind` ({0}), must be one of {1}"  # noqa: E501
                .format(entity_kind, allowed_values)
            )

        self._entity_kind = entity_kind

    @property
    def privilege(self):
        """Gets the privilege of this RevokePrivilege.  # noqa: E501

        Privilege  # noqa: E501

        :return: The privilege of this RevokePrivilege.  # noqa: E501
        :rtype: str
        """
        return self._privilege

    @privilege.setter
    def privilege(self, privilege):
        """Sets the privilege of this RevokePrivilege.

        Privilege  # noqa: E501

        :param privilege: The privilege of this RevokePrivilege.  # noqa: E501
        :type: str
        """
        if privilege is None:
            raise ValueError("Invalid value for `privilege`, must not be `None`")  # noqa: E501
        allowed_values = ["ManageSecurity", "CreateRole", "CreateUser", "CreateCluster", "CreateCatalog", "ViewAuditLog", "ManageBilling", "ManageNotifications", "ViewAllQueryHistory", "ManageSso", "SsoUserPasswordLogin", "ViewAllDataLineage", "UseCluster", "EnableDisableCluster", "MonitorCluster", "CreateSchema", "CreateTable", "Insert", "Delete", "Select", "Update", "ManageDataObservability", "CreateSql", "Execute", "ManageServiceAccount", "ManageServiceAccountToken", "ManageOauthClient", "ViewPublicOauthClient", "ManageAccountWork", "CreateTag", "ApplyTag", "ApplyTagInPath", "GenerativeAiFeatures", "ManageIngestStreams", "CreateFunction", "CancelQuery", "ViewDataProduct", "DownloadQueryResults", "ManageQueryRoutingRules"]  # noqa: E501
        if privilege not in allowed_values:
            raise ValueError(
                "Invalid value for `privilege` ({0}), must be one of {1}"  # noqa: E501
                .format(privilege, allowed_values)
            )

        self._privilege = privilege

    @property
    def schema_name(self):
        """Gets the schema_name of this RevokePrivilege.  # noqa: E501

        Schema name  # noqa: E501

        :return: The schema_name of this RevokePrivilege.  # noqa: E501
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this RevokePrivilege.

        Schema name  # noqa: E501

        :param schema_name: The schema_name of this RevokePrivilege.  # noqa: E501
        :type: str
        """

        self._schema_name = schema_name

    @property
    def table_name(self):
        """Gets the table_name of this RevokePrivilege.  # noqa: E501

        Table name  # noqa: E501

        :return: The table_name of this RevokePrivilege.  # noqa: E501
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this RevokePrivilege.

        Table name  # noqa: E501

        :param table_name: The table_name of this RevokePrivilege.  # noqa: E501
        :type: str
        """

        self._table_name = table_name

    @property
    def column_name(self):
        """Gets the column_name of this RevokePrivilege.  # noqa: E501

        Column name  # noqa: E501

        :return: The column_name of this RevokePrivilege.  # noqa: E501
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """Sets the column_name of this RevokePrivilege.

        Column name  # noqa: E501

        :param column_name: The column_name of this RevokePrivilege.  # noqa: E501
        :type: str
        """

        self._column_name = column_name

    @property
    def revoke_action(self):
        """Gets the revoke_action of this RevokePrivilege.  # noqa: E501

        Revoke grant option or remove role privilege  # noqa: E501

        :return: The revoke_action of this RevokePrivilege.  # noqa: E501
        :rtype: str
        """
        return self._revoke_action

    @revoke_action.setter
    def revoke_action(self, revoke_action):
        """Sets the revoke_action of this RevokePrivilege.

        Revoke grant option or remove role privilege  # noqa: E501

        :param revoke_action: The revoke_action of this RevokePrivilege.  # noqa: E501
        :type: str
        """
        if revoke_action is None:
            raise ValueError("Invalid value for `revoke_action`, must not be `None`")  # noqa: E501
        allowed_values = ["RevokeGrantOption", "RemoveRoleGrant"]  # noqa: E501
        if revoke_action not in allowed_values:
            raise ValueError(
                "Invalid value for `revoke_action` ({0}), must be one of {1}"  # noqa: E501
                .format(revoke_action, allowed_values)
            )

        self._revoke_action = revoke_action

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
        if issubclass(RevokePrivilege, dict):
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
        if not isinstance(other, RevokePrivilege):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other