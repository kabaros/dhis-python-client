from enum import Enum


class ProgramPutJsonObjectputXmlObjectImportMode(str, Enum):
    COMMIT = "COMMIT"
    VALIDATE = "VALIDATE"

    def __str__(self) -> str:
        return str(self.value)
