from enum import Enum


class DataSetNotificationTemplateDeliveryChannelsItem(str, Enum):
    EMAIL = "EMAIL"
    HTTP = "HTTP"
    SMS = "SMS"

    def __str__(self) -> str:
        return str(self.value)
