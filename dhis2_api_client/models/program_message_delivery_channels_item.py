from enum import Enum


class ProgramMessageDeliveryChannelsItem(str, Enum):
    EMAIL = "EMAIL"
    HTTP = "HTTP"
    SMS = "SMS"

    def __str__(self) -> str:
        return str(self.value)
