from enum import Enum


class OrgUnitMergeQueryDataValueMergeStrategy(str, Enum):
    DISCARD = "DISCARD"
    LAST_UPDATED = "LAST_UPDATED"

    def __str__(self) -> str:
        return str(self.value)
