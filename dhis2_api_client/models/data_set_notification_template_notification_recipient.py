from enum import Enum


class DataSetNotificationTemplateNotificationRecipient(str, Enum):
    ORGANISATION_UNIT_CONTACT = "ORGANISATION_UNIT_CONTACT"
    USER_GROUP = "USER_GROUP"

    def __str__(self) -> str:
        return str(self.value)
