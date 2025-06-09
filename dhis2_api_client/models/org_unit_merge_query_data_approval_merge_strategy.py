from enum import Enum


class OrgUnitMergeQueryDataApprovalMergeStrategy(str, Enum):
    DISCARD = "DISCARD"
    LAST_UPDATED = "LAST_UPDATED"

    def __str__(self) -> str:
        return str(self.value)
