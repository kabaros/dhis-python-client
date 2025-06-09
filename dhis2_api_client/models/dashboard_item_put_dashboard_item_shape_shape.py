from enum import Enum


class DashboardItemPutDashboardItemShapeShape(str, Enum):
    DOUBLE_WIDTH = "DOUBLE_WIDTH"
    FULL_WIDTH = "FULL_WIDTH"
    NORMAL = "NORMAL"

    def __str__(self) -> str:
        return str(self.value)
