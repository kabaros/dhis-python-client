from enum import Enum


class ApiTokenGetObjectGistAsCsv2RootJunction(str, Enum):
    AND = "AND"
    OR = "OR"

    def __str__(self) -> str:
        return str(self.value)
