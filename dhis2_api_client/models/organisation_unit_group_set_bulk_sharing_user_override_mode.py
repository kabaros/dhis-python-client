from enum import Enum


class OrganisationUnitGroupSetBulkSharingUserOverrideMode(str, Enum):
    CURRENT = "CURRENT"
    NONE = "NONE"
    SELECTED = "SELECTED"

    def __str__(self) -> str:
        return str(self.value)
