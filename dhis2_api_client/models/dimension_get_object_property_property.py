from enum import Enum


class DimensionGetObjectPropertyProperty(str, Enum):
    ID = "id"

    def __str__(self) -> str:
        return str(self.value)
