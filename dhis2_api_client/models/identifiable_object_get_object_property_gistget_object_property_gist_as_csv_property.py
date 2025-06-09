from enum import Enum


class IdentifiableObjectGetObjectPropertyGistgetObjectPropertyGistAsCsvProperty(str, Enum):
    ID = "id"

    def __str__(self) -> str:
        return str(self.value)
