from enum import Enum


class EnrollmentAnalyticsGetQueryCsvSortOrder(str, Enum):
    ASC = "ASC"
    DESC = "DESC"

    def __str__(self) -> str:
        return str(self.value)
