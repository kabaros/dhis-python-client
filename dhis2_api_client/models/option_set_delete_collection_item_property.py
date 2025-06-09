from enum import Enum


class OptionSetDeleteCollectionItemProperty(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DESCRIPTION = "description"
    DISPLAYNAME = "displayName"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    HREF = "href"
    ID = "id"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    NAME = "name"
    OPTIONS = "options"
    SHARING = "sharing"
    TRANSLATIONS = "translations"
    USER = "user"
    VALUETYPE = "valueType"
    VERSION = "version"

    def __str__(self) -> str:
        return str(self.value)
