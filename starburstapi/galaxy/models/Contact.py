from dataclasses import dataclass
from starburstapi.shared.models import JsonDataClass


@dataclass
class Contact(JsonDataClass):
    userId: str
    email: str
