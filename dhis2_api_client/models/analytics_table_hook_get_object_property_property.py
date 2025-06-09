from enum import Enum


class AnalyticsTableHookGetObjectPropertyProperty(str, Enum):
    ACCESS = "access"
    ANALYTICSTABLETYPE = "analyticsTableType"
    ATTRIBUTEVALUES = "attributeValues"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DISPLAYNAME = "displayName"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    HREF = "href"
    ID = "id"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    NAME = "name"
    PHASE = "phase"
    RESOURCETABLETYPE = "resourceTableType"
    SHARING = "sharing"
    SQL = "sql"
    TRANSLATIONS = "translations"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
