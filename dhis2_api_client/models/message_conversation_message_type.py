from enum import Enum


class MessageConversationMessageType(str, Enum):
    PRIVATE = "PRIVATE"
    SYSTEM = "SYSTEM"
    SYSTEM_VERSION_UPDATE = "SYSTEM_VERSION_UPDATE"
    TICKET = "TICKET"
    VALIDATION_RESULT = "VALIDATION_RESULT"

    def __str__(self) -> str:
        return str(self.value)
