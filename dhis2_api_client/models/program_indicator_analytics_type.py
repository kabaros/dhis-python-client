from enum import Enum


class ProgramIndicatorAnalyticsType(str, Enum):
    ENROLLMENT = "ENROLLMENT"
    EVENT = "EVENT"

    def __str__(self) -> str:
        return str(self.value)
