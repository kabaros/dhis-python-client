from enum import Enum


class EnrollmentAnalyticsGetAggregateXlsDisplayProperty(str, Enum):
    NAME = "NAME"
    SHORTNAME = "SHORTNAME"

    def __str__(self) -> str:
        return str(self.value)
