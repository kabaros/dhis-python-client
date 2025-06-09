from enum import Enum


class OutboundMessageResponseSummaryStatus(str, Enum):
    ABORTED = "ABORTED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PENDING = "PENDING"

    def __str__(self) -> str:
        return str(self.value)
