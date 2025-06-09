from enum import Enum


class TrackedEntityInstanceUpdateTrackedEntityInstanceJsonupdateTrackedEntityInstanceXmlNotificationLevel(str, Enum):
    DEBUG = "DEBUG"
    ERROR = "ERROR"
    INFO = "INFO"
    LOOP = "LOOP"
    OFF = "OFF"
    WARN = "WARN"

    def __str__(self) -> str:
        return str(self.value)
