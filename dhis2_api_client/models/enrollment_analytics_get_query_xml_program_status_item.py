from enum import Enum


class EnrollmentAnalyticsGetQueryXmlProgramStatusItem(str, Enum):
    ACTIVE = "ACTIVE"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"

    def __str__(self) -> str:
        return str(self.value)
