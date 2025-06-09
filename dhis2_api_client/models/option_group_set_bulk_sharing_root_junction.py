from enum import Enum


class OptionGroupSetBulkSharingRootJunction(str, Enum):
    AND = "AND"
    OR = "OR"

    def __str__(self) -> str:
        return str(self.value)
