from enum import Enum


class EventAnalyticsGetAggregateHtmlCssOutputType(str, Enum):
    ENROLLMENT = "ENROLLMENT"
    EVENT = "EVENT"
    TRACKED_ENTITY_INSTANCE = "TRACKED_ENTITY_INSTANCE"

    def __str__(self) -> str:
        return str(self.value)
