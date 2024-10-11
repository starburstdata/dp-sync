from dataclasses import dataclass
from typing import List
from starburstapi.galaxy.models import Catalog


@dataclass
class CatalogSearchResult:
    clusters: List[Catalog]
