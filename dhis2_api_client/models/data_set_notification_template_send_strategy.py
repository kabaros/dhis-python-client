from enum import Enum


class DataSetNotificationTemplateSendStrategy(str, Enum):
    COLLECTIVE_SUMMARY = "COLLECTIVE_SUMMARY"
    SINGLE_NOTIFICATION = "SINGLE_NOTIFICATION"

    def __str__(self) -> str:
        return str(self.value)
