from enum import Enum


class EventVisualizationFontSize(str, Enum):
    LARGE = "LARGE"
    NORMAL = "NORMAL"
    SMALL = "SMALL"

    def __str__(self) -> str:
        return str(self.value)
