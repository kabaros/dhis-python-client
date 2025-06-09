from enum import Enum


class AppAppStorageSource(str, Enum):
    JCLOUDS = "JCLOUDS"
    LOCAL = "LOCAL"

    def __str__(self) -> str:
        return str(self.value)
