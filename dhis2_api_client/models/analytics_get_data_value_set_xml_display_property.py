from enum import Enum


class AnalyticsGetDataValueSetXmlDisplayProperty(str, Enum):
    NAME = "NAME"
    SHORTNAME = "SHORTNAME"

    def __str__(self) -> str:
        return str(self.value)
