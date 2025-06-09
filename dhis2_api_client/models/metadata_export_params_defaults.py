from enum import Enum


class MetadataExportParamsDefaults(str, Enum):
    EXCLUDE = "EXCLUDE"
    INCLUDE = "INCLUDE"

    def __str__(self) -> str:
        return str(self.value)
