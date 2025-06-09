from enum import Enum


class ExpressionMissingValueStrategy(str, Enum):
    NEVER_SKIP = "NEVER_SKIP"
    SKIP_IF_ALL_VALUES_MISSING = "SKIP_IF_ALL_VALUES_MISSING"
    SKIP_IF_ANY_VALUE_MISSING = "SKIP_IF_ANY_VALUE_MISSING"

    def __str__(self) -> str:
        return str(self.value)
