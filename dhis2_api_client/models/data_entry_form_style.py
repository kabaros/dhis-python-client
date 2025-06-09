from enum import Enum


class DataEntryFormStyle(str, Enum):
    COMFORTABLE = "COMFORTABLE"
    COMPACT = "COMPACT"
    NONE = "NONE"
    NORMAL = "NORMAL"

    def __str__(self) -> str:
        return str(self.value)
