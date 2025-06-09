from enum import Enum


class TeiAnalyticsQueryXlsOuMode(str, Enum):
    ACCESSIBLE = "ACCESSIBLE"
    ALL = "ALL"
    CAPTURE = "CAPTURE"
    CHILDREN = "CHILDREN"
    DESCENDANTS = "DESCENDANTS"
    SELECTED = "SELECTED"

    def __str__(self) -> str:
        return str(self.value)
