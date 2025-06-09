from enum import Enum


class DateFilterPeriodType(str, Enum):
    ABSOLUTE = "ABSOLUTE"
    RELATIVE = "RELATIVE"

    def __str__(self) -> str:
        return str(self.value)
