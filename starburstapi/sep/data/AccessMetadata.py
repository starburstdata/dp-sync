from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from starburstapi.shared.models import JsonDataClass


@dataclass
class AccessMetadata(JsonDataClass):
    lastQueriedAt: Optional[datetime]
    lastQueriedBy: Optional[str]
