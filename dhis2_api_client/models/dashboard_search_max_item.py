from enum import Enum


class DashboardSearchMaxItem(str, Enum):
    APP = "APP"
    EVENT_CHART = "EVENT_CHART"
    EVENT_REPORT = "EVENT_REPORT"
    EVENT_VISUALIZATION = "EVENT_VISUALIZATION"
    MAP = "MAP"
    MESSAGES = "MESSAGES"
    REPORTS = "REPORTS"
    RESOURCES = "RESOURCES"
    TEXT = "TEXT"
    USERS = "USERS"
    VISUALIZATION = "VISUALIZATION"

    def __str__(self) -> str:
        return str(self.value)
