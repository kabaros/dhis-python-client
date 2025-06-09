from enum import Enum


class OutlierDetectionMetadataAlgorithm(str, Enum):
    MIN_MAX = "MIN_MAX"
    MOD_Z_SCORE = "MOD_Z_SCORE"
    Z_SCORE = "Z_SCORE"

    def __str__(self) -> str:
        return str(self.value)
