from enum import Enum


class MessageConversationGetObjectGistAsCsvAuto(str, Enum):
    L = "L"
    M = "M"
    S = "S"
    XL = "XL"
    XS = "XS"

    def __str__(self) -> str:
        return str(self.value)
