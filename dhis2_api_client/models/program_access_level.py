from enum import Enum


class ProgramAccessLevel(str, Enum):
    AUDITED = "AUDITED"
    CLOSED = "CLOSED"
    OPEN = "OPEN"
    PROTECTED = "PROTECTED"

    def __str__(self) -> str:
        return str(self.value)
