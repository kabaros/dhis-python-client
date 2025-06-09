from enum import Enum


class CategoryDataDimensionType(str, Enum):
    ATTRIBUTE = "ATTRIBUTE"
    DISAGGREGATION = "DISAGGREGATION"

    def __str__(self) -> str:
        return str(self.value)
