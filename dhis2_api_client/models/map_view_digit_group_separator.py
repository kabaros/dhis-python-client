from enum import Enum


class MapViewDigitGroupSeparator(str, Enum):
    COMMA = "COMMA"
    NONE = "NONE"
    SPACE = "SPACE"

    def __str__(self) -> str:
        return str(self.value)
