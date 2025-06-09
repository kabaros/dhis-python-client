from enum import Enum


class OAuth2ClientGetObjectPropertyGistgetObjectPropertyGistAsCsvProperty(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    CID = "cid"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DISPLAYNAME = "displayName"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    GRANTTYPES = "grantTypes"
    HREF = "href"
    ID = "id"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    NAME = "name"
    REDIRECTURIS = "redirectUris"
    SECRET = "secret"
    SHARING = "sharing"
    TRANSLATIONS = "translations"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
