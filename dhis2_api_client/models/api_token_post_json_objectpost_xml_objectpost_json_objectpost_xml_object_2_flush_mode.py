from enum import Enum


class ApiTokenPostJsonObjectpostXmlObjectpostJsonObjectpostXmlObject2FlushMode(str, Enum):
    AUTO = "AUTO"
    OBJECT = "OBJECT"

    def __str__(self) -> str:
        return str(self.value)
