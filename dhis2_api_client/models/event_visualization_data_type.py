from enum import Enum


class EventVisualizationDataType(str, Enum):
    AGGREGATED_VALUES = "AGGREGATED_VALUES"
    EVENTS = "EVENTS"

    def __str__(self) -> str:
        return str(self.value)
