from dataclasses import dataclass
from starburstapi.shared.models import JsonDataClass


@dataclass
class RelevantLinks(JsonDataClass):
    label: str
    url: str
