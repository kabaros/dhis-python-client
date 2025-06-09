from enum import Enum


class ProgramStageFormType(str, Enum):
    CUSTOM = "CUSTOM"
    DEFAULT = "DEFAULT"
    SECTION = "SECTION"
    SECTION_MULTIORG = "SECTION_MULTIORG"

    def __str__(self) -> str:
        return str(self.value)
