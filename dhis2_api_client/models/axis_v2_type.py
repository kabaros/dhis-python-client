from enum import Enum


class AxisV2Type(str, Enum):
    DOMAIN = "DOMAIN"
    RANGE = "RANGE"

    def __str__(self) -> str:
        return str(self.value)
