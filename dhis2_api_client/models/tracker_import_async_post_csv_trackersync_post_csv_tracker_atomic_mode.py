from enum import Enum


class TrackerImportAsyncPostCsvTrackersyncPostCsvTrackerAtomicMode(str, Enum):
    ALL = "ALL"
    OBJECT = "OBJECT"

    def __str__(self) -> str:
        return str(self.value)
