from enum import Enum


class SmsOutboundPatchObjectRootJunction(str, Enum):
    AND = "AND"
    OR = "OR"

    def __str__(self) -> str:
        return str(self.value)
