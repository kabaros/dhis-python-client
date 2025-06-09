from enum import Enum


class OptionGroupSetPatchObjectImportMode(str, Enum):
    COMMIT = "COMMIT"
    VALIDATE = "VALIDATE"

    def __str__(self) -> str:
        return str(self.value)
