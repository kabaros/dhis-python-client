from enum import Enum


class OrganisationUnitGroupPutJsonObjectputXmlObjectIdentifier(str, Enum):
    CODE = "CODE"
    UID = "UID"

    def __str__(self) -> str:
        return str(self.value)
