from enum import Enum


class DataValuesDtoLockStatus(str, Enum):
    APPROVED = "APPROVED"
    LOCKED = "LOCKED"
    OPEN = "OPEN"

    def __str__(self) -> str:
        return str(self.value)
