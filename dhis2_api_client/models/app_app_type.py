from enum import Enum


class AppAppType(str, Enum):
    APP = "APP"
    DASHBOARD_WIDGET = "DASHBOARD_WIDGET"
    RESOURCE = "RESOURCE"
    TRACKER_DASHBOARD_WIDGET = "TRACKER_DASHBOARD_WIDGET"

    def __str__(self) -> str:
        return str(self.value)
