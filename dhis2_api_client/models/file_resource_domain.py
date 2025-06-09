from enum import Enum


class FileResourceDomain(str, Enum):
    DATA_VALUE = "DATA_VALUE"
    DOCUMENT = "DOCUMENT"
    ICON = "ICON"
    JOB_DATA = "JOB_DATA"
    MESSAGE_ATTACHMENT = "MESSAGE_ATTACHMENT"
    ORG_UNIT = "ORG_UNIT"
    PUSH_ANALYSIS = "PUSH_ANALYSIS"
    USER_AVATAR = "USER_AVATAR"

    def __str__(self) -> str:
        return str(self.value)
