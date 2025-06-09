from enum import Enum


class DataEntryFormReplaceCollectionItemsJsonreplaceCollectionItemsXmlProperty(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DISPLAYNAME = "displayName"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    FORMAT = "format"
    HREF = "href"
    HTMLCODE = "htmlCode"
    ID = "id"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    NAME = "name"
    SHARING = "sharing"
    STYLE = "style"
    TRANSLATIONS = "translations"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
