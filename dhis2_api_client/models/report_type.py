from enum import Enum


class ReportType(str, Enum):
    HTML = "HTML"
    JASPER_JDBC = "JASPER_JDBC"
    JASPER_REPORT_TABLE = "JASPER_REPORT_TABLE"

    def __str__(self) -> str:
        return str(self.value)
