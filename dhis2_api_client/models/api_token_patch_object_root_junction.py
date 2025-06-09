from enum import Enum


class ApiTokenPatchObjectRootJunction(str, Enum):
    AND = "AND"
    OR = "OR"

    def __str__(self) -> str:
        return str(self.value)
