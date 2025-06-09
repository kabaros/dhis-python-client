from enum import Enum


class PushAnalysisGetObjectPropertyGistgetObjectPropertyGistAsCsvProperty(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DASHBOARD = "dashboard"
    DISPLAYNAME = "displayName"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    HREF = "href"
    ID = "id"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    MESSAGE = "message"
    NAME = "name"
    RECIPIENTUSERGROUPS = "recipientUserGroups"
    SHARING = "sharing"
    TITLE = "title"
    TRANSLATIONS = "translations"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
