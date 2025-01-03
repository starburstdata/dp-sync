from dataclasses import dataclass
from typing import List
from starburstapi.galaxy.models import Contact, Link
from starburstapi.shared.models import PaginatedJsonDataClass


@dataclass
class CreateDataProductRequest(PaginatedJsonDataClass):
    name: str
    summary: str
    description: str
    catalogId: str
    schemaName: str
    contacts: List[Contact]
    links: List[Link]
    defaultClusterId: str
