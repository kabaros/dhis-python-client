from enum import Enum


class SmsInboundPostJsonObjectAtomicMode(str, Enum):
    ALL = "ALL"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
