from dataclasses import dataclass

from starburstapi.sep.data import View
from starburstapi.sep.data import MaterializedView
from starburstapi.sep.data import Owner
from starburstapi.sep.data import AccessMetadata
from starburstapi.sep.data import UserData
from starburstapi.sep.data import RelevantLinks

from typing import List, Optional
from datetime import datetime
from starburstapi.shared.models import JsonDataClass


@dataclass
class DataProduct(JsonDataClass):
    id: str
    name: str
    catalogName: str
    schemaName: str
    dataDomainId: str
    summary: str
    description: str
    createdBy: str
    status: str
    views: List[View]
    materializedViews: List[MaterializedView]
    owners: List[Owner]
    productOwners: Optional[List[Owner]]
    relevantLinks: List[RelevantLinks]
    createdAt: datetime
    updatedAt: datetime
    updatedBy: str
    publishedAt: datetime
    publishedBy: str
    accessMetadata: Optional[AccessMetadata]
    ratingsCount: int
    userData: UserData
    matchesTrinoDefinition: bool
    bookmarkCount: int
