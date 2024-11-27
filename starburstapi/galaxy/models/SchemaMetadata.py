from dataclasses import dataclass
from typing import List, Optional
from starburstapi.galaxy.models import Contact, Link
from starburstapi.shared.models import PaginatedJsonDataClass

@dataclass
class TagIdentifier(PaginatedJsonDataClass):
    tagId: str
    name: str


@dataclass
class RoleIdentifier(PaginatedJsonDataClass):
    roleId: str
    roleName: str


@dataclass
class SchemaMetadata(PaginatedJsonDataClass):
    schemaId: str
    description: Optional[str]
    owner: RoleIdentifier
    tags: List[TagIdentifier]
    contacts: List[Contact]
    links: List[Link]
