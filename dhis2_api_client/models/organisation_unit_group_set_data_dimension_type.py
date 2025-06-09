from enum import Enum


class OrganisationUnitGroupSetDataDimensionType(str, Enum):
    ATTRIBUTE = "ATTRIBUTE"
    DISAGGREGATION = "DISAGGREGATION"

    def __str__(self) -> str:
        return str(self.value)
