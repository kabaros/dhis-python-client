from enum import Enum


class DocumentGetObjectPropertyProperty(str, Enum):
    ACCESS = "access"
    ATTACHMENT = "attachment"
    ATTRIBUTEVALUES = "attributeValues"
    CODE = "code"
    CONTENTTYPE = "contentType"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DISPLAYNAME = "displayName"
    EXTERNAL = "external"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
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
