from enum import Enum


class DataSetPeriodType(str, Enum):
    BIMONTHLY = "BiMonthly"
    BIWEEKLY = "BiWeekly"
    DAILY = "Daily"
    FINANCIALAPRIL = "FinancialApril"
    FINANCIALJULY = "FinancialJuly"
    FINANCIALNOV = "FinancialNov"
    FINANCIALOCT = "FinancialOct"
    MONTHLY = "Monthly"
    QUARTERLY = "Quarterly"
    QUARTERLYNOV = "QuarterlyNov"
    SIXMONTHLY = "SixMonthly"
    SIXMONTHLYAPRIL = "SixMonthlyApril"
    SIXMONTHLYNOV = "SixMonthlyNov"
    TWOYEARLY = "TwoYearly"
    WEEKLY = "Weekly"
    WEEKLYSATURDAY = "WeeklySaturday"
    WEEKLYSUNDAY = "WeeklySunday"
    WEEKLYTHURSDAY = "WeeklyThursday"
    WEEKLYWEDNESDAY = "WeeklyWednesday"
    YEARLY = "Yearly"

    def __str__(self) -> str:
        return str(self.value)
