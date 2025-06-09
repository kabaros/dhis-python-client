from enum import Enum


class DataElementDomainType(str, Enum):
    AGGREGATE = "AGGREGATE"
    TRACKER = "TRACKER"

    def __str__(self) -> str:
        return str(self.value)
