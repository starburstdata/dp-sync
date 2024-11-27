from dataclasses import dataclass
from typing import List
from datetime import datetime
from starburstapi.galaxy.models import Contact, Link
from starburstapi.shared.models import PaginatedJsonDataClass

@dataclass
class DataProductCatalogDetails(PaginatedJsonDataClass):
    catalogId: str
    catalogName: str
    catalogKind: str
    localRegions: List[str]


@dataclass
class DataProduct(PaginatedJsonDataClass):
    syncToken: str
    dataProductId: str
    name: str
    summary: str
    description: str
    catalog: DataProductCatalogDetails
    schemaName: str
    contacts: List[Contact]
    links: List[Link]
    defaultClusterId: str
    createdOn: datetime
    modifiedOn: datetime
    createdBy: Contact
    modifiedBy: Contact
