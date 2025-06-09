from enum import Enum


class ChangeLogGetAggregateDataValueAuditAuditTypeItem(str, Enum):
    CREATE = "CREATE"
    DELETE = "DELETE"
    READ = "READ"
    SEARCH = "SEARCH"
    UPDATE = "UPDATE"

    def __str__(self) -> str:
        return str(self.value)
