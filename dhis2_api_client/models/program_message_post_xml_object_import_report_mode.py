from enum import Enum


class ProgramMessagePostXmlObjectImportReportMode(str, Enum):
    DEBUG = "DEBUG"
    ERRORS = "ERRORS"
    ERRORS_NOT_OWNER = "ERRORS_NOT_OWNER"
    FULL = "FULL"

    def __str__(self) -> str:
        return str(self.value)
