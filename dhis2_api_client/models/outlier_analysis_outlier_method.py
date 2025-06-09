from enum import Enum


class OutlierAnalysisOutlierMethod(str, Enum):
    IQR = "IQR"
    MODIFIED_Z_SCORE = "MODIFIED_Z_SCORE"
    STANDARD_Z_SCORE = "STANDARD_Z_SCORE"

    def __str__(self) -> str:
        return str(self.value)
