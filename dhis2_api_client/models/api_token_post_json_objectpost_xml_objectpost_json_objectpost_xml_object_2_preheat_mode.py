from enum import Enum


class ApiTokenPostJsonObjectpostXmlObjectpostJsonObjectpostXmlObject2PreheatMode(str, Enum):
    ALL = "ALL"
    NONE = "NONE"
    REFERENCE = "REFERENCE"

    def __str__(self) -> str:
        return str(self.value)
