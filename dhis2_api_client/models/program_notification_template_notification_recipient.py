from enum import Enum


class ProgramNotificationTemplateNotificationRecipient(str, Enum):
    DATA_ELEMENT = "DATA_ELEMENT"
    ORGANISATION_UNIT_CONTACT = "ORGANISATION_UNIT_CONTACT"
    PROGRAM_ATTRIBUTE = "PROGRAM_ATTRIBUTE"
    TRACKED_ENTITY_INSTANCE = "TRACKED_ENTITY_INSTANCE"
    USERS_AT_ORGANISATION_UNIT = "USERS_AT_ORGANISATION_UNIT"
    USER_GROUP = "USER_GROUP"
    WEB_HOOK = "WEB_HOOK"

    def __str__(self) -> str:
        return str(self.value)
