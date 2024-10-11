from dataclasses import dataclass
from typing import List
from datetime import datetime
from starburstapi.galaxy.models import Role


@dataclass
class UserPrincipal:
    id: str
    type: str

@dataclass
class UserRole:
    roleName: str
    roleId: str
    principal: UserPrincipal
    adminOption: bool


@dataclass
class User:
    syncToken: str
    userId: str
    email: str
    defaultRoleId: str
    createdOn: datetime
    scimManaged: bool
    directlyGrantedRoles: List[UserRole]
    allRoles: List[UserRole]
