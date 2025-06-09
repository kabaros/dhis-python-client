from enum import Enum


class ProgramPatchObjectFlushMode(str, Enum):
    AUTO = "AUTO"
    OBJECT = "OBJECT"

    def __str__(self) -> str:
        return str(self.value)
