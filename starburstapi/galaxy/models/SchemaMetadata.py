from dataclasses import dataclass
from typing import List, Optional
from starburstapi.galaxy.models import Contact, Link
from starburstapi.shared.models import JsonDataClass

@dataclass
class TagIdentifier(JsonDataClass):
    tagId: str
    name: str


@dataclass
class RoleIdentifier(JsonDataClass):
    roleId: str
    roleName: str


@dataclass
class SchemaMetadata(JsonDataClass):
    schemaId: str
    description: Optional[str]
    owner: RoleIdentifier
    tags: List[TagIdentifier]
    contacts: List[Contact]
    links: List[Link]
