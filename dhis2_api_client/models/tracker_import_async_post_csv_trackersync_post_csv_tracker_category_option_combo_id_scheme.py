from enum import Enum


class TrackerImportAsyncPostCsvTrackersyncPostCsvTrackerCategoryOptionComboIdScheme(str, Enum):
    ATTRIBUTE = "ATTRIBUTE"
    CODE = "CODE"
    NAME = "NAME"
    UID = "UID"

    def __str__(self) -> str:
        return str(self.value)
