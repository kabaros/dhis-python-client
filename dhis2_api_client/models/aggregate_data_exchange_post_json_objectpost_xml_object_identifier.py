from enum import Enum


class AggregateDataExchangePostJsonObjectpostXmlObjectIdentifier(str, Enum):
    CODE = "CODE"
    UID = "UID"

    def __str__(self) -> str:
        return str(self.value)
