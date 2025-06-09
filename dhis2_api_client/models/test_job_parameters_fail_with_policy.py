from enum import Enum


class TestJobParametersFailWithPolicy(str, Enum):
    FAIL = "FAIL"
    PARENT = "PARENT"
    SKIP_ITEM = "SKIP_ITEM"
    SKIP_ITEM_OUTLIER = "SKIP_ITEM_OUTLIER"
    SKIP_STAGE = "SKIP_STAGE"

    def __str__(self) -> str:
        return str(self.value)
