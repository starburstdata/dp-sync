from dataclasses import dataclass
from typing import Optional
from starburstapi.shared.models import JsonDataClass


@dataclass
class MaterializedViewProperties(JsonDataClass):
    refresh_interval: str
    grace_period: Optional[str]
