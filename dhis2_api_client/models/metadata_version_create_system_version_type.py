from enum import Enum


class MetadataVersionCreateSystemVersionType(str, Enum):
    ATOMIC = "ATOMIC"
    BEST_EFFORT = "BEST_EFFORT"

    def __str__(self) -> str:
        return str(self.value)
