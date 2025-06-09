from enum import Enum


class ExternalMapLayerMapLayerPosition(str, Enum):
    BASEMAP = "BASEMAP"
    OVERLAY = "OVERLAY"

    def __str__(self) -> str:
        return str(self.value)
