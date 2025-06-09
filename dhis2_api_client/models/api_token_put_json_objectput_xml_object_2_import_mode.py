from enum import Enum


class ApiTokenPutJsonObjectputXmlObject2ImportMode(str, Enum):
    COMMIT = "COMMIT"
    VALIDATE = "VALIDATE"

    def __str__(self) -> str:
        return str(self.value)
