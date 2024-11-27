# needed for recursive class definitions
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime
from starburstapi.shared.models import PaginatedJsonDataClass

@dataclass
class Role(PaginatedJsonDataClass):
    syncToken: Optional[str]
    userId: str
    email: str
    defaultRoleId: str
    createdOn: datetime
    scimManaged: bool
    directlyGrantedRoles: List[Role]
    allRoles: List[Role]
