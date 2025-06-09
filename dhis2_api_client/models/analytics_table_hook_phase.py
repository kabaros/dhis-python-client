from enum import Enum


class AnalyticsTableHookPhase(str, Enum):
    ANALYTICS_TABLE_POPULATED = "ANALYTICS_TABLE_POPULATED"
    RESOURCE_TABLE_POPULATED = "RESOURCE_TABLE_POPULATED"

    def __str__(self) -> str:
        return str(self.value)
