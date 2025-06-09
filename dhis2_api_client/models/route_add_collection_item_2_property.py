from enum import Enum


class RouteAddCollectionItem2Property(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    AUTH = "auth"
    AUTHORITIES = "authorities"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DESCRIPTION = "description"
    DISABLED = "disabled"
    DISPLAYNAME = "displayName"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    HEADERS = "headers"
    HREF = "href"
    ID = "id"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    NAME = "name"
    SHARING = "sharing"
    TRANSLATIONS = "translations"
    URL = "url"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
