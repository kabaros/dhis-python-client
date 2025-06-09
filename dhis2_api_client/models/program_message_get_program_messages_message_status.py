from enum import Enum


class ProgramMessageGetProgramMessagesMessageStatus(str, Enum):
    FAILED = "FAILED"
    OUTBOUND = "OUTBOUND"
    SCHEDULED = "SCHEDULED"
    SENT = "SENT"

    def __str__(self) -> str:
        return str(self.value)
