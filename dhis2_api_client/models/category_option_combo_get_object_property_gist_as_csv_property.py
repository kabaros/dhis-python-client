from enum import Enum


class CategoryOptionComboGetObjectPropertyGistAsCsvProperty(str, Enum):
    ACCESS = "access"
    AGGREGATIONTYPE = "aggregationType"
    ATTRIBUTEVALUES = "attributeValues"
    CATEGORYCOMBO = "categoryCombo"
    CATEGORYOPTIONS = "categoryOptions"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DESCRIPTION = "description"
    DIMENSIONITEM = "dimensionItem"
    DIMENSIONITEMTYPE = "dimensionItemType"
    DISPLAYDESCRIPTION = "displayDescription"
    DISPLAYFORMNAME = "displayFormName"
    DISPLAYNAME = "displayName"
    DISPLAYSHORTNAME = "displayShortName"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    FORMNAME = "formName"
    HREF = "href"
    ID = "id"
    IGNOREAPPROVAL = "ignoreApproval"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    LEGENDSET = "legendSet"
    LEGENDSETS = "legendSets"
    QUERYMODS = "queryMods"
    SHARING = "sharing"
    TRANSLATIONS = "translations"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
