from enum import Enum


class ReportingRateMetric(str, Enum):
    ACTUAL_REPORTS = "ACTUAL_REPORTS"
    ACTUAL_REPORTS_ON_TIME = "ACTUAL_REPORTS_ON_TIME"
    EXPECTED_REPORTS = "EXPECTED_REPORTS"
    REPORTING_RATE = "REPORTING_RATE"
    REPORTING_RATE_ON_TIME = "REPORTING_RATE_ON_TIME"

    def __str__(self) -> str:
        return str(self.value)
