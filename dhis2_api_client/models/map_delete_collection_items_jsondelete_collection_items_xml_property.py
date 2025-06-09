from enum import Enum


class MapDeleteCollectionItemsJsondeleteCollectionItemsXmlProperty(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    BASEMAP = "basemap"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DESCRIPTION = "description"
    DISPLAYDESCRIPTION = "displayDescription"
    DISPLAYFORMNAME = "displayFormName"
    DISPLAYNAME = "displayName"
    DISPLAYSHORTNAME = "displayShortName"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    FORMNAME = "formName"
    HREF = "href"
    ID = "id"
    INTERPRETATIONS = "interpretations"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    LATITUDE = "latitude"
    LONGITUDE = "longitude"
    MAPVIEWS = "mapViews"
    NAME = "name"
    SHARING = "sharing"
    SHORTNAME = "shortName"
    SUBSCRIBED = "subscribed"
    SUBSCRIBERS = "subscribers"
    TITLE = "title"
    TRANSLATIONS = "translations"
    USER = "user"
    ZOOM = "zoom"

    def __str__(self) -> str:
        return str(self.value)
