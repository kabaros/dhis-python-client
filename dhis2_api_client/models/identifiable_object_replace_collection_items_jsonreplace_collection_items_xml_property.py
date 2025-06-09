from enum import Enum


class IdentifiableObjectReplaceCollectionItemsJsonreplaceCollectionItemsXmlProperty(str, Enum):
    ID = "id"

    def __str__(self) -> str:
        return str(self.value)
