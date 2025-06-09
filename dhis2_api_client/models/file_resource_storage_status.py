from enum import Enum


class FileResourceStorageStatus(str, Enum):
    NONE = "NONE"
    PENDING = "PENDING"
    STORED = "STORED"

    def __str__(self) -> str:
        return str(self.value)
