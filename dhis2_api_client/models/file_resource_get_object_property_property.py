from enum import Enum


class FileResourceGetObjectPropertyProperty(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    CODE = "code"
    CONTENTLENGTH = "contentLength"
    CONTENTMD5 = "contentMd5"
    CONTENTTYPE = "contentType"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DISPLAYNAME = "displayName"
    DOMAIN = "domain"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    HASMULTIPLESTORAGEFILES = "hasMultipleStorageFiles"
    HREF = "href"
    ID = "id"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    NAME = "name"
    SHARING = "sharing"
    STORAGESTATUS = "storageStatus"
    TRANSLATIONS = "translations"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
