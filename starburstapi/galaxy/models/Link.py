from dataclasses import dataclass
from starburstapi.shared.models import PaginatedJsonDataClass

@dataclass
class Link(PaginatedJsonDataClass):
    name: str
    uri: str
