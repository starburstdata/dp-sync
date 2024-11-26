from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from starburstapi.shared.models import JsonDataClass


@dataclass
class DataProductSearchResult(JsonDataClass):
    id: str
    name: str
    catalogName: str
    schemaName: str
    dataDomainId: str
    summary: str
    description: str
    createdBy: str
    status: str
    createdAt: datetime
    updatedAt: datetime
    publishedAt: datetime
    publishedBy: str
    lastQueriedAt: Optional[datetime]
    lastQueriedBy: Optional[str]
    ratingsCount: int
    userData: dict
