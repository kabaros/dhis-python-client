from enum import Enum


class TrackerImportAsyncPostCsvTrackersyncPostCsvTrackerDataElementIdScheme(str, Enum):
    ATTRIBUTE = "ATTRIBUTE"
    CODE = "CODE"
    NAME = "NAME"
    UID = "UID"

    def __str__(self) -> str:
        return str(self.value)
