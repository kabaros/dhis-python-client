from enum import Enum


class ItemConfigInsertPosition(str, Enum):
    END = "END"
    START = "START"

    def __str__(self) -> str:
        return str(self.value)
