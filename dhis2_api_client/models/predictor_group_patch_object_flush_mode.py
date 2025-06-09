from enum import Enum


class PredictorGroupPatchObjectFlushMode(str, Enum):
    AUTO = "AUTO"
    OBJECT = "OBJECT"

    def __str__(self) -> str:
        return str(self.value)
