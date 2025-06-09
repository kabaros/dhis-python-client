from enum import Enum


class OrganisationUnitGroupSetPostJsonObjectpostXmlObjectFlushMode(str, Enum):
    AUTO = "AUTO"
    OBJECT = "OBJECT"

    def __str__(self) -> str:
        return str(self.value)
