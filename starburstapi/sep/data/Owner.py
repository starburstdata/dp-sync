from dataclasses import dataclass
from starburstapi.shared.models import JsonDataClass


@dataclass
class Owner(JsonDataClass):
    name: str
    email: str
