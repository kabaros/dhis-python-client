from enum import Enum


class EventAnalyticsGetQueryCsvSortOrder(str, Enum):
    ASC = "ASC"
    DESC = "DESC"

    def __str__(self) -> str:
        return str(self.value)
