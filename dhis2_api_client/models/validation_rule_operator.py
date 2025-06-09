from enum import Enum


class ValidationRuleOperator(str, Enum):
    COMPULSORY_PAIR = "compulsory_pair"
    EQUAL_TO = "equal_to"
    EXCLUSIVE_PAIR = "exclusive_pair"
    GREATER_THAN = "greater_than"
    GREATER_THAN_OR_EQUAL_TO = "greater_than_or_equal_to"
    LESS_THAN = "less_than"
    LESS_THAN_OR_EQUAL_TO = "less_than_or_equal_to"
    NOT_EQUAL_TO = "not_equal_to"

    def __str__(self) -> str:
        return str(self.value)
