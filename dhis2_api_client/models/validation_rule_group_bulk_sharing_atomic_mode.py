from enum import Enum


class ValidationRuleGroupBulkSharingAtomicMode(str, Enum):
    ALL = "ALL"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
