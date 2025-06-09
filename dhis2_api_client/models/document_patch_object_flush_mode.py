from enum import Enum


class DocumentPatchObjectFlushMode(str, Enum):
    AUTO = "AUTO"
    OBJECT = "OBJECT"

    def __str__(self) -> str:
        return str(self.value)
