from enum import Enum


class StyledObjectTextMode(str, Enum):
    AUTO = "AUTO"
    CUSTOM = "CUSTOM"

    def __str__(self) -> str:
        return str(self.value)
