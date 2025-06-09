from enum import Enum


class ExternalMapLayerDeleteCollectionItemsJsondeleteCollectionItemsXmlProperty(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    ATTRIBUTION = "attribution"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DISPLAYNAME = "displayName"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    HREF = "href"
    ID = "id"
    IMAGEFORMAT = "imageFormat"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    LAYERS = "layers"
    LEGENDSET = "legendSet"
    LEGENDSETURL = "legendSetUrl"
    MAPLAYERPOSITION = "mapLayerPosition"
    MAPSERVICE = "mapService"
    NAME = "name"
    SHARING = "sharing"
    TRANSLATIONS = "translations"
    URL = "url"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
