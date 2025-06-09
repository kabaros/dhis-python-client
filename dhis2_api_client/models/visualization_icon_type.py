from enum import Enum


class VisualizationIconType(str, Enum):
    DATA_ITEM = "DATA_ITEM"

    def __str__(self) -> str:
        return str(self.value)
