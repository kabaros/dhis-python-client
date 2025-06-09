from enum import Enum


class MessageConversationPriority(str, Enum):
    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
