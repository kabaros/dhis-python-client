from enum import Enum


class UserRoleDeleteCollectionItemProperty(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    AUTHORITIES = "authorities"
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
    RESTRICTIONS = "restrictions"
    SHARING = "sharing"
    TRANSLATIONS = "translations"
    USER = "user"
    USERS = "users"

    def __str__(self) -> str:
        return str(self.value)
