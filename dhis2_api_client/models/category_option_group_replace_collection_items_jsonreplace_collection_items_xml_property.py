from enum import Enum


class CategoryOptionGroupReplaceCollectionItemsJsonreplaceCollectionItemsXmlProperty(str, Enum):
    ACCESS = "access"
    AGGREGATIONTYPE = "aggregationType"
    ATTRIBUTEVALUES = "attributeValues"
    CATEGORYOPTIONS = "categoryOptions"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DATADIMENSIONTYPE = "dataDimensionType"
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
