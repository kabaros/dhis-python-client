from enum import Enum


class ApiTokenPatchObject2ImportMode(str, Enum):
    COMMIT = "COMMIT"
    VALIDATE = "VALIDATE"

    def __str__(self) -> str:
        return str(self.value)
