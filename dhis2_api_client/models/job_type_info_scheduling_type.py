from enum import Enum


class JobTypeInfoSchedulingType(str, Enum):
    CRON = "CRON"
    FIXED_DELAY = "FIXED_DELAY"
    ONCE_ASAP = "ONCE_ASAP"

    def __str__(self) -> str:
        return str(self.value)
