from enum import Enum


class ProgramStageValidationStrategy(str, Enum):
    ON_COMPLETE = "ON_COMPLETE"
    ON_UPDATE_AND_INSERT = "ON_UPDATE_AND_INSERT"

    def __str__(self) -> str:
        return str(self.value)
