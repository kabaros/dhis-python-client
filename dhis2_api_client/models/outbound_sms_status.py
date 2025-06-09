from enum import Enum


class OutboundSmsStatus(str, Enum):
    DELIVERED = "DELIVERED"
    ERROR = "ERROR"
    FAILED = "FAILED"
    OUTBOUND = "OUTBOUND"
    PENDING = "PENDING"
    SCHEDULED = "SCHEDULED"
    SENT = "SENT"

    def __str__(self) -> str:
        return str(self.value)
