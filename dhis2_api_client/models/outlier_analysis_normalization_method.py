from enum import Enum


class OutlierAnalysisNormalizationMethod(str, Enum):
    Y_RESIDUALS_LINEAR = "Y_RESIDUALS_LINEAR"

    def __str__(self) -> str:
        return str(self.value)
