from enum import Enum


class SchedulerEntryJobStatus(str, Enum):
    COMPLETED = "COMPLETED"
    DISABLED = "DISABLED"
    FAILED = "FAILED"
    NOT_STARTED = "NOT_STARTED"
    RUNNING = "RUNNING"
    SCHEDULED = "SCHEDULED"
    STOPPED = "STOPPED"

    def __str__(self) -> str:
        return str(self.value)
