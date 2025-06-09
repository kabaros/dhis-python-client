from enum import Enum


class IndicatorBulkSharingUserOverrideMode(str, Enum):
    CURRENT = "CURRENT"
    NONE = "NONE"
    SELECTED = "SELECTED"

    def __str__(self) -> str:
        return str(self.value)
