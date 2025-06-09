from enum import Enum


class MessageConversationSetMessageStatusMessageConversationStatus(str, Enum):
    INVALID = "INVALID"
    NONE = "NONE"
    OPEN = "OPEN"
    PENDING = "PENDING"
    SOLVED = "SOLVED"

    def __str__(self) -> str:
        return str(self.value)
