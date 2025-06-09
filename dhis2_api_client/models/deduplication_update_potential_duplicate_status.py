from enum import Enum


class DeduplicationUpdatePotentialDuplicateStatus(str, Enum):
    ALL = "ALL"
    INVALID = "INVALID"
    MERGED = "MERGED"
    OPEN = "OPEN"

    def __str__(self) -> str:
        return str(self.value)
