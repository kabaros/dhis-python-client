from enum import Enum


class IncomingSmsSmsencoding(str, Enum):
    ENC7BIT = "ENC7BIT"
    ENC8BIT = "ENC8BIT"
    ENCCUSTOM = "ENCCUSTOM"
    ENCUCS2 = "ENCUCS2"

    def __str__(self) -> str:
        return str(self.value)
