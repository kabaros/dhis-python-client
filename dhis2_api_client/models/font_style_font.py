from enum import Enum


class FontStyleFont(str, Enum):
    ARIAL = "ARIAL"
    ROBOTO = "ROBOTO"
    SANS_SERIF = "SANS_SERIF"
    VERDANA = "VERDANA"

    def __str__(self) -> str:
        return str(self.value)
