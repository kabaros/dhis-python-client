from enum import Enum


class OrganisationUnitGetUserDataViewOrganisationUnitsRootJunction(str, Enum):
    AND = "AND"
    OR = "OR"

    def __str__(self) -> str:
        return str(self.value)
