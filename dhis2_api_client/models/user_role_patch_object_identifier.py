from enum import Enum


class UserRolePatchObjectIdentifier(str, Enum):
    CODE = "CODE"
    UID = "UID"

    def __str__(self) -> str:
        return str(self.value)
