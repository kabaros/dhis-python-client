from enum import Enum


class VisualizationDigitGroupSeparator(str, Enum):
    COMMA = "COMMA"
    NONE = "NONE"
    SPACE = "SPACE"

    def __str__(self) -> str:
        return str(self.value)
