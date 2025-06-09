from enum import Enum


class EnrollmentAnalyticsGetExplainQueryJsonDisplayProperty(str, Enum):
    NAME = "NAME"
    SHORTNAME = "SHORTNAME"

    def __str__(self) -> str:
        return str(self.value)
