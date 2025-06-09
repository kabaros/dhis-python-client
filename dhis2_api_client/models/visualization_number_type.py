from enum import Enum


class VisualizationNumberType(str, Enum):
    COLUMN_PERCENTAGE = "COLUMN_PERCENTAGE"
    ROW_PERCENTAGE = "ROW_PERCENTAGE"
    VALUE = "VALUE"

    def __str__(self) -> str:
        return str(self.value)
