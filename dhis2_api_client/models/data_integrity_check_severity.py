from enum import Enum


class DataIntegrityCheckSeverity(str, Enum):
    CRITICAL = "CRITICAL"
    INFO = "INFO"
    SEVERE = "SEVERE"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
