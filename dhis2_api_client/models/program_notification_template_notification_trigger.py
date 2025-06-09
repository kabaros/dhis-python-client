from enum import Enum


class ProgramNotificationTemplateNotificationTrigger(str, Enum):
    COMPLETION = "COMPLETION"
    ENROLLMENT = "ENROLLMENT"
    PROGRAM_RULE = "PROGRAM_RULE"
    SCHEDULED_DAYS_DUE_DATE = "SCHEDULED_DAYS_DUE_DATE"
    SCHEDULED_DAYS_ENROLLMENT_DATE = "SCHEDULED_DAYS_ENROLLMENT_DATE"
    SCHEDULED_DAYS_INCIDENT_DATE = "SCHEDULED_DAYS_INCIDENT_DATE"

    def __str__(self) -> str:
        return str(self.value)
