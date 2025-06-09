from enum import Enum


class PropertyNamesDataElementGroup(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DATAELEMENTS = "dataElements"
    DESCRIPTION = "description"
    DIMENSIONITEM = "dimensionItem"
    DISPLAYDESCRIPTION = "displayDescription"
    DISPLAYFORMNAME = "displayFormName"
    DISPLAYNAME = "displayName"
    DISPLAYSHORTNAME = "displayShortName"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    FORMNAME = "formName"
    GROUPSETS = "groupSets"
    HREF = "href"
    ID = "id"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    LEGENDSET = "legendSet"
    LEGENDSETS = "legendSets"
    NAME = "name"
    QUERYMODS = "queryMods"
    SHARING = "sharing"
    SHORTNAME = "shortName"
    TRANSLATIONS = "translations"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
