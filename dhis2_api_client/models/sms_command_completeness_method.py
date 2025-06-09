from enum import Enum


class SMSCommandCompletenessMethod(str, Enum):
    ALL_DATAVALUE = "ALL_DATAVALUE"
    AT_LEAST_ONE_DATAVALUE = "AT_LEAST_ONE_DATAVALUE"
    DO_NOT_MARK_COMPLETE = "DO_NOT_MARK_COMPLETE"

    def __str__(self) -> str:
        return str(self.value)
