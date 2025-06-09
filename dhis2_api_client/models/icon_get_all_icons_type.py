from enum import Enum


class IconGetAllIconsType(str, Enum):
    ALL = "ALL"
    CUSTOM = "CUSTOM"
    DEFAULT = "DEFAULT"

    def __str__(self) -> str:
        return str(self.value)
