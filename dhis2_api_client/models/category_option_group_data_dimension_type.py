from enum import Enum


class CategoryOptionGroupDataDimensionType(str, Enum):
    ATTRIBUTE = "ATTRIBUTE"
    DISAGGREGATION = "DISAGGREGATION"

    def __str__(self) -> str:
        return str(self.value)
