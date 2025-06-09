from enum import Enum


class EventsExportGetEventDataValueImageDimension(str, Enum):
    LARGE = "LARGE"
    MEDIUM = "MEDIUM"
    ORIGINAL = "ORIGINAL"
    SMALL = "SMALL"

    def __str__(self) -> str:
        return str(self.value)
