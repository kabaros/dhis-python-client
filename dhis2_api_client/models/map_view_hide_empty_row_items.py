from enum import Enum


class MapViewHideEmptyRowItems(str, Enum):
    AFTER_LAST = "AFTER_LAST"
    ALL = "ALL"
    BEFORE_FIRST = "BEFORE_FIRST"
    BEFORE_FIRST_AFTER_LAST = "BEFORE_FIRST_AFTER_LAST"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
