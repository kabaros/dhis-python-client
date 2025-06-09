from enum import Enum


class TrackedEntityTypePostJsonObjectpostXmlObjectImportMode(str, Enum):
    COMMIT = "COMMIT"
    VALIDATE = "VALIDATE"

    def __str__(self) -> str:
        return str(self.value)
