from enum import Enum


class ProgramRuleActionProgramRuleActionEvaluationTime(str, Enum):
    ALWAYS = "ALWAYS"
    ON_COMPLETE = "ON_COMPLETE"
    ON_DATA_ENTRY = "ON_DATA_ENTRY"

    def __str__(self) -> str:
        return str(self.value)
