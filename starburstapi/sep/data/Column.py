from dataclasses import dataclass
from starburstapi.shared.models import JsonDataClass


@dataclass
class Column(JsonDataClass):
    name: str
    type: str
    description: str
