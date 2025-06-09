from enum import Enum


class ApiTokenPutJsonObjectputXmlObject2FlushMode(str, Enum):
    AUTO = "AUTO"
    OBJECT = "OBJECT"

    def __str__(self) -> str:
        return str(self.value)
