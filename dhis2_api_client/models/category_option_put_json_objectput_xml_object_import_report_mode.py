from enum import Enum


class CategoryOptionPutJsonObjectputXmlObjectImportReportMode(str, Enum):
    DEBUG = "DEBUG"
    ERRORS = "ERRORS"
    ERRORS_NOT_OWNER = "ERRORS_NOT_OWNER"
    FULL = "FULL"

    def __str__(self) -> str:
        return str(self.value)
