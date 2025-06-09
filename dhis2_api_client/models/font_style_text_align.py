from enum import Enum


class FontStyleTextAlign(str, Enum):
    CENTER = "CENTER"
    LEFT = "LEFT"
    RIGHT = "RIGHT"

    def __str__(self) -> str:
        return str(self.value)
