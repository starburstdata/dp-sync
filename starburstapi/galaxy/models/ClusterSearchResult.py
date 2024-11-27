from dataclasses import dataclass
from typing import List
from starburstapi.galaxy.models import Catalog
from starburstapi.shared.models import PaginatedJsonDataClass


@dataclass
class CatalogSearchResult(PaginatedJsonDataClass):
    clusters: List[Catalog]
