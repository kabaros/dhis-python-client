from enum import Enum


class VisualizationDisplayDensity(str, Enum):
    COMFORTABLE = "COMFORTABLE"
    COMPACT = "COMPACT"
    NONE = "NONE"
    NORMAL = "NORMAL"

    def __str__(self) -> str:
        return str(self.value)
