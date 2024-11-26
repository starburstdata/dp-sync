from dataclasses import dataclass
from typing import List
from starburstapi.galaxy.models import Catalog
from starburstapi.shared.models import JsonDataClass


@dataclass
class CatalogSearchResult(JsonDataClass):
    clusters: List[Catalog]
