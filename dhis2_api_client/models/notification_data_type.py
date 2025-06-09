from enum import Enum


class NotificationDataType(str, Enum):
    PARAMETERS = "PARAMETERS"

    def __str__(self) -> str:
        return str(self.value)
