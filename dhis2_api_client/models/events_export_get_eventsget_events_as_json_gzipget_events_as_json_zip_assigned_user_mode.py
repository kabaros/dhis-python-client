from enum import Enum


class EventsExportGetEventsgetEventsAsJsonGzipgetEventsAsJsonZipAssignedUserMode(str, Enum):
    ALL = "ALL"
    ANY = "ANY"
    CURRENT = "CURRENT"
    NONE = "NONE"
    PROVIDED = "PROVIDED"

    def __str__(self) -> str:
        return str(self.value)
