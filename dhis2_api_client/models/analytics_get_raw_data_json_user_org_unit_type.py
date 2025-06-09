from enum import Enum


class AnalyticsGetRawDataJsonUserOrgUnitType(str, Enum):
    DATA_CAPTURE = "DATA_CAPTURE"
    DATA_OUTPUT = "DATA_OUTPUT"
    TEI_SEARCH = "TEI_SEARCH"

    def __str__(self) -> str:
        return str(self.value)
