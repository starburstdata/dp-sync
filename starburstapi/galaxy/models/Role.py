#needed for recursive class definitions
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime


@dataclass
class Role:
    syncToken: Optional
    userId: str
    email: str
    defaultRoleId: str
    createdOn: datetime
    scimManaged: bool
    directlyGrantedRoles: List[Role]
    allRoles: List[Role]
