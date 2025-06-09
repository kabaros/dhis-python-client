from enum import Enum


class OrganisationUnitLevelDeleteCollectionItemsJsondeleteCollectionItemsXmlProperty(str, Enum):
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
    LEVEL = "level"
    NAME = "name"
    OFFLINELEVELS = "offlineLevels"
    SHARING = "sharing"
    TRANSLATIONS = "translations"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
