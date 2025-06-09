from enum import Enum


class AnalyticsOutlierDetectionGetOutliersHtmlCssAlgorithm(str, Enum):
    MIN_MAX = "MIN_MAX"
    MODIFIED_Z_SCORE = "MODIFIED_Z_SCORE"
    Z_SCORE = "Z_SCORE"

    def __str__(self) -> str:
        return str(self.value)
