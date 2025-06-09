from enum import Enum


class IndicatorTypeAddCollectionItemProperty(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DISPLAYNAME = "displayName"
    FACTOR = "factor"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    HREF = "href"
    ID = "id"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    NAME = "name"
    NUMBER = "number"
    SHARING = "sharing"
    TRANSLATIONS = "translations"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
