from enum import Enum


class IdentifiableObjectGetObjectPropertyGistAsCsvProperty(str, Enum):
    ID = "id"

    def __str__(self) -> str:
        return str(self.value)
