from enum import Enum


class MetadataItemDimensionType(str, Enum):
    ATTRIBUTE_OPTION_COMBO = "ATTRIBUTE_OPTION_COMBO"
    CATEGORY = "CATEGORY"
    CATEGORY_OPTION_COMBO = "CATEGORY_OPTION_COMBO"
    CATEGORY_OPTION_GROUP_SET = "CATEGORY_OPTION_GROUP_SET"
    DATA_COLLAPSED = "DATA_COLLAPSED"
    DATA_ELEMENT_GROUP_SET = "DATA_ELEMENT_GROUP_SET"
    DATA_X = "DATA_X"
    OPTION_GROUP_SET = "OPTION_GROUP_SET"
    ORGANISATION_UNIT = "ORGANISATION_UNIT"
    ORGANISATION_UNIT_GROUP = "ORGANISATION_UNIT_GROUP"
    ORGANISATION_UNIT_GROUP_SET = "ORGANISATION_UNIT_GROUP_SET"
    ORGANISATION_UNIT_LEVEL = "ORGANISATION_UNIT_LEVEL"
    PERIOD = "PERIOD"
    PROGRAM_ATTRIBUTE = "PROGRAM_ATTRIBUTE"
    PROGRAM_DATA_ELEMENT = "PROGRAM_DATA_ELEMENT"
    PROGRAM_INDICATOR = "PROGRAM_INDICATOR"
    STATIC = "STATIC"
    VALIDATION_RULE = "VALIDATION_RULE"

    def __str__(self) -> str:
        return str(self.value)
