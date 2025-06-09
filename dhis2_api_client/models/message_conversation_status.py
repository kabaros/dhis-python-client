from enum import Enum


class MessageConversationStatus(str, Enum):
    INVALID = "INVALID"
    NONE = "NONE"
    OPEN = "OPEN"
    PENDING = "PENDING"
    SOLVED = "SOLVED"

    def __str__(self) -> str:
        return str(self.value)
