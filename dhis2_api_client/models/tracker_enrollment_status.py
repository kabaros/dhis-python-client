from enum import Enum


class TrackerEnrollmentStatus(str, Enum):
    ACTIVE = "ACTIVE"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"

    def __str__(self) -> str:
        return str(self.value)
