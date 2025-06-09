from enum import Enum


class ProgramProgramType(str, Enum):
    WITHOUT_REGISTRATION = "WITHOUT_REGISTRATION"
    WITH_REGISTRATION = "WITH_REGISTRATION"

    def __str__(self) -> str:
        return str(self.value)
