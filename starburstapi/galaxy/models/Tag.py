from dataclasses import dataclass
from typing import Optional
from starburstapi.shared.models import JsonDataClass

@dataclass
class Tag(JsonDataClass):
    name: str
    color: str
    description: Optional[str]
