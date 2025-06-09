from enum import Enum


class ApiTokenAddCollectionItem2Property(str, Enum):
    ACCESS = "access"
    ATTRIBUTES = "attributes"
    ATTRIBUTEVALUES = "attributeValues"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DISPLAYNAME = "displayName"
    EXPIRE = "expire"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    HREF = "href"
    ID = "id"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    NAME = "name"
    SHARING = "sharing"
    TRANSLATIONS = "translations"
    TYPE = "type"
    USER = "user"
    VERSION = "version"

    def __str__(self) -> str:
        return str(self.value)
