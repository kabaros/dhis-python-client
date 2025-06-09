from enum import Enum


class PredictorOrganisationUnitDescendants(str, Enum):
    DESCENDANTS = "DESCENDANTS"
    SELECTED = "SELECTED"

    def __str__(self) -> str:
        return str(self.value)
