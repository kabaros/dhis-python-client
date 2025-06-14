from enum import Enum


class LoginResponseLoginStatus(str, Enum):
    ACCOUNT_DISABLED = "ACCOUNT_DISABLED"
    ACCOUNT_EXPIRED = "ACCOUNT_EXPIRED"
    ACCOUNT_LOCKED = "ACCOUNT_LOCKED"
    INCORRECT_TWO_FACTOR_CODE = "INCORRECT_TWO_FACTOR_CODE"
    PASSWORD_EXPIRED = "PASSWORD_EXPIRED"
    REQUIRES_TWO_FACTOR_ENROLMENT = "REQUIRES_TWO_FACTOR_ENROLMENT"
    SUCCESS = "SUCCESS"

    def __str__(self) -> str:
        return str(self.value)
