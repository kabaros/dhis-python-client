from enum import Enum


class MapViewEventStatus(str, Enum):
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    OVERDUE = "OVERDUE"
    SCHEDULE = "SCHEDULE"
    SKIPPED = "SKIPPED"

    def __str__(self) -> str:
        return str(self.value)
