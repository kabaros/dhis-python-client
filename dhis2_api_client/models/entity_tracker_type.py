from enum import Enum


class EntityTrackerType(str, Enum):
    ENROLLMENT = "ENROLLMENT"
    EVENT = "EVENT"
    RELATIONSHIP = "RELATIONSHIP"
    TRACKED_ENTITY = "TRACKED_ENTITY"

    def __str__(self) -> str:
        return str(self.value)
