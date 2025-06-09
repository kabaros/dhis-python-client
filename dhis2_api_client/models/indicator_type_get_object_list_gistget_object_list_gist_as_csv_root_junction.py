from enum import Enum


class IndicatorTypeGetObjectListGistgetObjectListGistAsCsvRootJunction(str, Enum):
    AND = "AND"
    OR = "OR"

    def __str__(self) -> str:
        return str(self.value)
