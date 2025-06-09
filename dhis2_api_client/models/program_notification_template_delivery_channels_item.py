from enum import Enum


class ProgramNotificationTemplateDeliveryChannelsItem(str, Enum):
    EMAIL = "EMAIL"
    HTTP = "HTTP"
    SMS = "SMS"

    def __str__(self) -> str:
        return str(self.value)
