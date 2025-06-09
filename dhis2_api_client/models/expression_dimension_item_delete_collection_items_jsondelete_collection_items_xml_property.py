from enum import Enum


class ExpressionDimensionItemDeleteCollectionItemsJsondeleteCollectionItemsXmlProperty(str, Enum):
    ACCESS = "access"
    AGGREGATEEXPORTATTRIBUTEOPTIONCOMBO = "aggregateExportAttributeOptionCombo"
    AGGREGATEEXPORTCATEGORYOPTIONCOMBO = "aggregateExportCategoryOptionCombo"
    AGGREGATIONTYPE = "aggregationType"
    ATTRIBUTEVALUES = "attributeValues"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DESCRIPTION = "description"
    DIMENSIONITEM = "dimensionItem"
    DISPLAYDESCRIPTION = "displayDescription"
    DISPLAYFORMNAME = "displayFormName"
    DISPLAYNAME = "displayName"
    DISPLAYSHORTNAME = "displayShortName"
    EXPRESSION = "expression"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    FORMNAME = "formName"
    HREF = "href"
    ID = "id"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    LEGENDSET = "legendSet"
    LEGENDSETS = "legendSets"
    MISSINGVALUESTRATEGY = "missingValueStrategy"
    NAME = "name"
    QUERYMODS = "queryMods"
    SHARING = "sharing"
    SHORTNAME = "shortName"
    SLIDINGWINDOW = "slidingWindow"
    TRANSLATIONS = "translations"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
