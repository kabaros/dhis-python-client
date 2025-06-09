from enum import Enum


class EnrollmentAnalyticsGetAggregateHtmlEndpointAction(str, Enum):
    AGGREGATE = "AGGREGATE"
    OTHER = "OTHER"
    QUERY = "QUERY"

    def __str__(self) -> str:
        return str(self.value)
