from enum import Enum


class MapViewGetObjectPropertyGistgetObjectPropertyGistAsCsvRootJunction(str, Enum):
    AND = "AND"
    OR = "OR"

    def __str__(self) -> str:
        return str(self.value)
