from dataclasses import dataclass, asdict
from typing import List
from starburstapi.galaxy.models import Contact, Link
import json


@dataclass
class CreateDataProductRequest:
    name: str
    summary: str
    description: str
    catalogId: str
    schemaName: str
    contacts: List[Contact]
    links: List[Link]
    defaultClusterId: str

    def to_json(self):
        return json.dumps(asdict(self))
