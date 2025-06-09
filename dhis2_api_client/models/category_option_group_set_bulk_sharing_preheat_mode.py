from enum import Enum


class CategoryOptionGroupSetBulkSharingPreheatMode(str, Enum):
    ALL = "ALL"
    NONE = "NONE"
    REFERENCE = "REFERENCE"

    def __str__(self) -> str:
        return str(self.value)
