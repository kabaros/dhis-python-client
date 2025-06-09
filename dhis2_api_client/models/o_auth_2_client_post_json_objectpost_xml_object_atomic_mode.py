from enum import Enum


class OAuth2ClientPostJsonObjectpostXmlObjectAtomicMode(str, Enum):
    ALL = "ALL"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
