from enum import Enum


class IdentifiableObjectGetObjectPropertyRootJunction(str, Enum):
    AND = "AND"
    OR = "OR"

    def __str__(self) -> str:
        return str(self.value)
