from dataclasses import dataclass
from starburstapi.shared.models import JsonDataClass

@dataclass
class Link(JsonDataClass):
    name: str
    uri: str
