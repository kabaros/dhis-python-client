from enum import Enum


class ApiTokenPutJsonObjectputXmlObject2AtomicMode(str, Enum):
    ALL = "ALL"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
