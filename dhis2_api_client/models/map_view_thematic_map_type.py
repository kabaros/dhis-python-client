from enum import Enum


class MapViewThematicMapType(str, Enum):
    BUBBLE = "BUBBLE"
    CHOROPLETH = "CHOROPLETH"

    def __str__(self) -> str:
        return str(self.value)
