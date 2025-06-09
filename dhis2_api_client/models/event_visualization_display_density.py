from enum import Enum


class EventVisualizationDisplayDensity(str, Enum):
    COMFORTABLE = "COMFORTABLE"
    COMPACT = "COMPACT"
    NONE = "NONE"
    NORMAL = "NORMAL"

    def __str__(self) -> str:
        return str(self.value)
