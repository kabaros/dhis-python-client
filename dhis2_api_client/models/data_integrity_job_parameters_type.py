from enum import Enum


class DataIntegrityJobParametersType(str, Enum):
    DETAILS = "DETAILS"
    REPORT = "REPORT"
    SUMMARY = "SUMMARY"

    def __str__(self) -> str:
        return str(self.value)
