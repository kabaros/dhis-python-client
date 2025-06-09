from enum import Enum


class ApiTokenPutJsonObjectputXmlObject2Identifier(str, Enum):
    CODE = "CODE"
    UID = "UID"

    def __str__(self) -> str:
        return str(self.value)
