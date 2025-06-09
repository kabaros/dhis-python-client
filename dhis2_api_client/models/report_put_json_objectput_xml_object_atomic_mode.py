from enum import Enum


class ReportPutJsonObjectputXmlObjectAtomicMode(str, Enum):
    ALL = "ALL"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
