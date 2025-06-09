from enum import Enum


class DataStatisticsGetReportsInterval(str, Enum):
    DAY = "DAY"
    MONTH = "MONTH"
    WEEK = "WEEK"
    YEAR = "YEAR"

    def __str__(self) -> str:
        return str(self.value)
