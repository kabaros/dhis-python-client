from enum import Enum


class VisualizationType(str, Enum):
    AREA = "AREA"
    BAR = "BAR"
    BUBBLE = "BUBBLE"
    COLUMN = "COLUMN"
    GAUGE = "GAUGE"
    LINE = "LINE"
    OUTLIER_TABLE = "OUTLIER_TABLE"
    PIE = "PIE"
    PIVOT_TABLE = "PIVOT_TABLE"
    RADAR = "RADAR"
    SCATTER = "SCATTER"
    SINGLE_VALUE = "SINGLE_VALUE"
    STACKED_AREA = "STACKED_AREA"
    STACKED_BAR = "STACKED_BAR"
    STACKED_COLUMN = "STACKED_COLUMN"
    YEAR_OVER_YEAR_COLUMN = "YEAR_OVER_YEAR_COLUMN"
    YEAR_OVER_YEAR_LINE = "YEAR_OVER_YEAR_LINE"

    def __str__(self) -> str:
        return str(self.value)
