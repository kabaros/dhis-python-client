from enum import Enum


class GistPreferencesIncluded(str, Enum):
    AUTO = "AUTO"
    FALSE = "FALSE"
    TRUE = "TRUE"

    def __str__(self) -> str:
        return str(self.value)
