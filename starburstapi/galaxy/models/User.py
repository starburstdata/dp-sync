from dataclasses import dataclass
from typing import List
from datetime import datetime
from starburstapi.shared.models import JsonDataClass


@dataclass
class UserPrincipal(JsonDataClass):
    id: str
    type: str


@dataclass
class UserRole(JsonDataClass):
    roleName: str
    roleId: str
    principal: UserPrincipal
    adminOption: bool


@dataclass
class User(JsonDataClass):
    syncToken: str
    userId: str
    email: str
    defaultRoleId: str
    createdOn: datetime
    scimManaged: bool
    directlyGrantedRoles: List[UserRole]
    allRoles: List[UserRole]
