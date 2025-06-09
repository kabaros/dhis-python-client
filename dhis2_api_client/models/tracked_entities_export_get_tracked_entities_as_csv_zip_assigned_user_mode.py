from enum import Enum


class TrackedEntitiesExportGetTrackedEntitiesAsCsvZipAssignedUserMode(str, Enum):
    ALL = "ALL"
    ANY = "ANY"
    CURRENT = "CURRENT"
    NONE = "NONE"
    PROVIDED = "PROVIDED"

    def __str__(self) -> str:
        return str(self.value)
