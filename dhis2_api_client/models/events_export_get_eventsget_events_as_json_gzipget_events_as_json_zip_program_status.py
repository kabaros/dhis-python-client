from enum import Enum


class EventsExportGetEventsgetEventsAsJsonGzipgetEventsAsJsonZipProgramStatus(str, Enum):
    ACTIVE = "ACTIVE"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"

    def __str__(self) -> str:
        return str(self.value)
