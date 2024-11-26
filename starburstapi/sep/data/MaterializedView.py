from dataclasses import dataclass
from starburstapi.sep.data import Column
from starburstapi.sep.data import MaterializedViewProperties

from typing import List
from datetime import datetime
from starburstapi.shared.models import JsonDataClass


@dataclass
class MaterializedView(JsonDataClass):
    name: str
    description: str
    createdBy: str
    definitionQuery: str
    definitionProperties: MaterializedViewProperties
    status: str
    columns: List[Column]
    markedForDeletion: bool
    createdAt: datetime
    updatedAt: datetime
    updatedBy: str
    publishedAt: datetime
    publishedBy: str
    matchesTrinoDefinition: bool
