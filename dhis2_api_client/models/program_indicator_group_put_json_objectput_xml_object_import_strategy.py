from enum import Enum


class ProgramIndicatorGroupPutJsonObjectputXmlObjectImportStrategy(str, Enum):
    CREATE = "CREATE"
    CREATE_AND_UPDATE = "CREATE_AND_UPDATE"
    DELETE = "DELETE"
    DELETES = "DELETES"
    NEW = "NEW"
    NEW_AND_UPDATES = "NEW_AND_UPDATES"
    SYNC = "SYNC"
    UPDATE = "UPDATE"
    UPDATES = "UPDATES"

    def __str__(self) -> str:
        return str(self.value)
