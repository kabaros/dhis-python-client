from enum import Enum


class MapViewRenderingStrategy(str, Enum):
    SINGLE = "SINGLE"
    SPLIT_BY_PERIOD = "SPLIT_BY_PERIOD"
    TIMELINE = "TIMELINE"

    def __str__(self) -> str:
        return str(self.value)
