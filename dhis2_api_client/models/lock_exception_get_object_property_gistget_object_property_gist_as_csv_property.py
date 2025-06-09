from enum import Enum


class LockExceptionGetObjectPropertyGistgetObjectPropertyGistAsCsvProperty(str, Enum):
    CREATED = "created"
    DATASET = "dataSet"
    NAME = "name"
    ORGANISATIONUNIT = "organisationUnit"
    PERIOD = "period"

    def __str__(self) -> str:
        return str(self.value)
