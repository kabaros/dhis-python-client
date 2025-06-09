from enum import Enum


class TeiAnalyticsQueryHtmlDataIdScheme(str, Enum):
    ATTRIBUTE = "ATTRIBUTE"
    CODE = "CODE"
    ID = "ID"
    NAME = "NAME"
    UID = "UID"
    UUID = "UUID"

    def __str__(self) -> str:
        return str(self.value)
