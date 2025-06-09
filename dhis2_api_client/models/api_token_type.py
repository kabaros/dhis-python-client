from enum import Enum


class ApiTokenType(str, Enum):
    PERSONAL_ACCESS_TOKEN_V1 = "PERSONAL_ACCESS_TOKEN_V1"
    PERSONAL_ACCESS_TOKEN_V2 = "PERSONAL_ACCESS_TOKEN_V2"

    def __str__(self) -> str:
        return str(self.value)
