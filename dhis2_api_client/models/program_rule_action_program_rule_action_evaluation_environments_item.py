from enum import Enum


class ProgramRuleActionProgramRuleActionEvaluationEnvironmentsItem(str, Enum):
    ANDROID = "ANDROID"
    WEB = "WEB"

    def __str__(self) -> str:
        return str(self.value)
