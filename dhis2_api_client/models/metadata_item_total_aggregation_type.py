from enum import Enum


class MetadataItemTotalAggregationType(str, Enum):
    AVERAGE = "AVERAGE"
    NONE = "NONE"
    SUM = "SUM"

    def __str__(self) -> str:
        return str(self.value)
