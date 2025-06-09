from enum import Enum


class TrackedEntityTypeFeatureType(str, Enum):
    MULTI_POLYGON = "MULTI_POLYGON"
    NONE = "NONE"
    POINT = "POINT"
    POLYGON = "POLYGON"
    SYMBOL = "SYMBOL"

    def __str__(self) -> str:
        return str(self.value)
