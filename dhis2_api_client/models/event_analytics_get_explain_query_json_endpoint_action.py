from enum import Enum


class EventAnalyticsGetExplainQueryJsonEndpointAction(str, Enum):
    AGGREGATE = "AGGREGATE"
    OTHER = "OTHER"
    QUERY = "QUERY"

    def __str__(self) -> str:
        return str(self.value)
