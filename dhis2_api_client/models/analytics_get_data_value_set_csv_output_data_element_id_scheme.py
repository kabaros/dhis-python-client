from enum import Enum


class AnalyticsGetDataValueSetCsvOutputDataElementIdScheme(str, Enum):
    ATTRIBUTE = "ATTRIBUTE"
    CODE = "CODE"
    ID = "ID"
    NAME = "NAME"
    UID = "UID"
    UUID = "UUID"

    def __str__(self) -> str:
        return str(self.value)
