from enum import Enum


class GistPreferencesTransformation(str, Enum):
    AUTO = "AUTO"
    FROM = "FROM"
    IDS = "IDS"
    ID_OBJECTS = "ID_OBJECTS"
    IS_EMPTY = "IS_EMPTY"
    IS_NOT_EMPTY = "IS_NOT_EMPTY"
    MEMBER = "MEMBER"
    NONE = "NONE"
    NOT_MEMBER = "NOT_MEMBER"
    PLUCK = "PLUCK"
    SIZE = "SIZE"

    def __str__(self) -> str:
        return str(self.value)
