from dataclasses import dataclass
from typing import Optional
from starburstapi.shared.models import JsonDataClass

@dataclass
class TagResponse(JsonDataClass):
    syncToken: str
    tagId: str
    name: str
    color: str
    description: Optional[str]
