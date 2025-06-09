from enum import Enum


class CategoryOptionGroupPostJsonObjectpostXmlObjectFlushMode(str, Enum):
    AUTO = "AUTO"
    OBJECT = "OBJECT"

    def __str__(self) -> str:
        return str(self.value)
