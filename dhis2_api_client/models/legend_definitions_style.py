from enum import Enum


class LegendDefinitionsStyle(str, Enum):
    FILL = "FILL"
    TEXT = "TEXT"

    def __str__(self) -> str:
        return str(self.value)
