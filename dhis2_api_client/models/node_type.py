from enum import Enum


class NodeType(str, Enum):
    COLLECTION = "COLLECTION"
    COMPLEX = "COMPLEX"
    SIMPLE = "SIMPLE"

    def __str__(self) -> str:
        return str(self.value)
