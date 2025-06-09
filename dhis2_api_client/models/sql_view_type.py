from enum import Enum


class SqlViewType(str, Enum):
    MATERIALIZED_VIEW = "MATERIALIZED_VIEW"
    QUERY = "QUERY"
    VIEW = "VIEW"

    def __str__(self) -> str:
        return str(self.value)
