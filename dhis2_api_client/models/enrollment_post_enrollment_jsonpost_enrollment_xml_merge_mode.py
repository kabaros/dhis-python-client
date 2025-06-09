from enum import Enum


class EnrollmentPostEnrollmentJsonpostEnrollmentXmlMergeMode(str, Enum):
    MERGE = "MERGE"
    MERGE_ALWAYS = "MERGE_ALWAYS"
    MERGE_IF_NOT_NULL = "MERGE_IF_NOT_NULL"
    NONE = "NONE"
    REPLACE = "REPLACE"

    def __str__(self) -> str:
        return str(self.value)
