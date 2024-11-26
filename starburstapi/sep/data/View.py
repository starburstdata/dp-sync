from dataclasses import dataclass
from starburstapi.sep.data import Column
from typing import List
from datetime import datetime
from starburstapi.shared.models import JsonDataClass


@dataclass
class View(JsonDataClass):
    name: str
    description: str
    createdBy: str
    definitionQuery: str
    status: str
    columns: List[Column]
    markedForDeletion: bool
    createdAt: datetime
    updatedAt: datetime
    updatedBy: str
    publishedAt: datetime
    publishedBy: str
    matchesTrinoDefinition: bool
