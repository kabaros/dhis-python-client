from enum import Enum


class EventAnalyticsGetQueryXlsSortOrder(str, Enum):
    ASC = "ASC"
    DESC = "DESC"

    def __str__(self) -> str:
        return str(self.value)
