from enum import Enum


class EventAnalyticsGetQueryHtmlCssEndpointAction(str, Enum):
    AGGREGATE = "AGGREGATE"
    OTHER = "OTHER"
    QUERY = "QUERY"

    def __str__(self) -> str:
        return str(self.value)
