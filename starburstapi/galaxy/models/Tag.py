from dataclasses import dataclass
from typing import Optional
from starburstapi.shared.models import PaginatedJsonDataClass

@dataclass
class Tag(PaginatedJsonDataClass):
    name: str
    color: str
    description: Optional[str]
