from enum import Enum


class DataElementGroupSetDataDimensionType(str, Enum):
    ATTRIBUTE = "ATTRIBUTE"
    DISAGGREGATION = "DISAGGREGATION"

    def __str__(self) -> str:
        return str(self.value)
