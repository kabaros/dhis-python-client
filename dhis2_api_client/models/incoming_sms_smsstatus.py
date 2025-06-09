from enum import Enum


class IncomingSmsSmsstatus(str, Enum):
    FAILED = "FAILED"
    INCOMING = "INCOMING"
    PROCESSED = "PROCESSED"
    PROCESSING = "PROCESSING"
    SENT = "SENT"
    UNHANDLED = "UNHANDLED"

    def __str__(self) -> str:
        return str(self.value)
