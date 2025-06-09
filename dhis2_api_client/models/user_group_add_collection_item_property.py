from enum import Enum


class UserGroupAddCollectionItemProperty(str, Enum):
    ACCESS = "access"
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
    MANAGEDBYGROUPS = "managedByGroups"
    MANAGEDGROUPS = "managedGroups"
    NAME = "name"
    SHARING = "sharing"
    TRANSLATIONS = "translations"
    USER = "user"
    USERS = "users"

    def __str__(self) -> str:
        return str(self.value)
