from enum import Enum


class InterpretationType(str, Enum):
    DATASET_REPORT = "DATASET_REPORT"
    EVENT_CHART = "EVENT_CHART"
    EVENT_REPORT = "EVENT_REPORT"
    EVENT_VISUALIZATION = "EVENT_VISUALIZATION"
    MAP = "MAP"
    VISUALIZATION = "VISUALIZATION"

    def __str__(self) -> str:
        return str(self.value)
