from enum import Enum


class RelationshipTypePatchObjectRootJunction(str, Enum):
    AND = "AND"
    OR = "OR"

    def __str__(self) -> str:
        return str(self.value)
