from enum import Enum


class DataEntryFormPostJsonObjectpostXmlObjectUserOverrideMode(str, Enum):
    CURRENT = "CURRENT"
    NONE = "NONE"
    SELECTED = "SELECTED"

    def __str__(self) -> str:
        return str(self.value)
