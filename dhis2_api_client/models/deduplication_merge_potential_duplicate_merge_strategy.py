from enum import Enum


class DeduplicationMergePotentialDuplicateMergeStrategy(str, Enum):
    AUTO = "AUTO"
    MANUAL = "MANUAL"

    def __str__(self) -> str:
        return str(self.value)
