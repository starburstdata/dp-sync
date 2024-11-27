from dataclasses import dataclass
from starburstapi.shared.models import PaginatedJsonDataClass

@dataclass
class Catalog(PaginatedJsonDataClass):
    catalogId: str
    catalogName: str
