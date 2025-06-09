from enum import Enum


class LegendDefinitionsStrategy(str, Enum):
    BY_DATA_ITEM = "BY_DATA_ITEM"
    FIXED = "FIXED"

    def __str__(self) -> str:
        return str(self.value)
