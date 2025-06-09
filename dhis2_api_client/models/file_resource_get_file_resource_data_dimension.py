from enum import Enum


class FileResourceGetFileResourceDataDimension(str, Enum):
    LARGE = "LARGE"
    MEDIUM = "MEDIUM"
    ORIGINAL = "ORIGINAL"
    SMALL = "SMALL"

    def __str__(self) -> str:
        return str(self.value)
