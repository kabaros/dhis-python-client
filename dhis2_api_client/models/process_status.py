from enum import Enum


class ProcessStatus(str, Enum):
    CANCELLED = "CANCELLED"
    ERROR = "ERROR"
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"

    def __str__(self) -> str:
        return str(self.value)
