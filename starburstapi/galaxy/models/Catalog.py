from dataclasses import dataclass
from starburstapi.shared.models import JsonDataClass

@dataclass
class Catalog(JsonDataClass):
    catalogId: str
    catalogName: str
