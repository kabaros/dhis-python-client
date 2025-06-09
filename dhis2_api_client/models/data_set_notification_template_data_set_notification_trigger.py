from enum import Enum


class DataSetNotificationTemplateDataSetNotificationTrigger(str, Enum):
    DATA_SET_COMPLETION = "DATA_SET_COMPLETION"
    SCHEDULED_DAYS = "SCHEDULED_DAYS"

    def __str__(self) -> str:
        return str(self.value)
