from enum import Enum


class EventAnalyticsGetAggregateXmlEventStatusItem(str, Enum):
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    OVERDUE = "OVERDUE"
    SCHEDULE = "SCHEDULE"
    SKIPPED = "SKIPPED"
    VISITED = "VISITED"

    def __str__(self) -> str:
        return str(self.value)
