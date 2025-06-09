from enum import Enum


class IdentifiableObjectBulkSharingAtomicMode(str, Enum):
    ALL = "ALL"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
