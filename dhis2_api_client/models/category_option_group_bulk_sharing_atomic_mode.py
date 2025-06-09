from enum import Enum


class CategoryOptionGroupBulkSharingAtomicMode(str, Enum):
    ALL = "ALL"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
