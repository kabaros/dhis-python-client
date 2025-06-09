from enum import Enum


class CategoryPatchObjectFlushMode(str, Enum):
    AUTO = "AUTO"
    OBJECT = "OBJECT"

    def __str__(self) -> str:
        return str(self.value)
