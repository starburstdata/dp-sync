from dataclasses import dataclass
from starburstapi.shared.models import JsonDataClass


@dataclass
class UserData(JsonDataClass):
    isBookmarked: bool
    # TODO: check docs for additional fields
