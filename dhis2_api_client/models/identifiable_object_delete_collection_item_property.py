from enum import Enum


class IdentifiableObjectDeleteCollectionItemProperty(str, Enum):
    ID = "id"

    def __str__(self) -> str:
        return str(self.value)
