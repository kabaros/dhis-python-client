from enum import Enum


class MetadataExportParamsInclusionStrategy(str, Enum):
    ALWAYS = "ALWAYS"
    NON_EMPTY = "NON_EMPTY"
    NON_NULL = "NON_NULL"

    def __str__(self) -> str:
        return str(self.value)
