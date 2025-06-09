from enum import Enum


class MapViewRegressionType(str, Enum):
    LINEAR = "LINEAR"
    LOESS = "LOESS"
    NONE = "NONE"
    POLYNOMIAL = "POLYNOMIAL"

    def __str__(self) -> str:
        return str(self.value)
