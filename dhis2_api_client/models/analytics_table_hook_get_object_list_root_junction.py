from enum import Enum


class AnalyticsTableHookGetObjectListRootJunction(str, Enum):
    AND = "AND"
    OR = "OR"

    def __str__(self) -> str:
        return str(self.value)
