from dataclasses import dataclass
from starburstapi.shared.models import PaginatedJsonDataClass


@dataclass
class Contact(PaginatedJsonDataClass):
    userId: str
    email: str
