from enum import Enum


class EventRepetitionParent(str, Enum):
    COLUMN = "COLUMN"
    FILTER = "FILTER"
    ROW = "ROW"

    def __str__(self) -> str:
        return str(self.value)
