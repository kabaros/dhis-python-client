from enum import Enum


class EnrollmentAnalyticsGetExplainQueryJsonEndpointAction(str, Enum):
    AGGREGATE = "AGGREGATE"
    OTHER = "OTHER"
    QUERY = "QUERY"

    def __str__(self) -> str:
        return str(self.value)
