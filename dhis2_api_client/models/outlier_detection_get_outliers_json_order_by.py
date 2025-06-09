from enum import Enum


class OutlierDetectionGetOutliersJsonOrderBy(str, Enum):
    MEAN_ABS_DEV = "MEAN_ABS_DEV"
    Z_SCORE = "Z_SCORE"

    def __str__(self) -> str:
        return str(self.value)
