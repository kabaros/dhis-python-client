from enum import Enum


class EnrollmentAnalyticsGetQueryXmlEndpointAction(str, Enum):
    AGGREGATE = "AGGREGATE"
    OTHER = "OTHER"
    QUERY = "QUERY"

    def __str__(self) -> str:
        return str(self.value)
