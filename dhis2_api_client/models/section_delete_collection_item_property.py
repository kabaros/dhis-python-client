from enum import Enum


class SectionDeleteCollectionItemProperty(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    CATEGORYCOMBOS = "categoryCombos"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DATAELEMENTS = "dataElements"
    DATASET = "dataSet"
    DESCRIPTION = "description"
    DISABLEDATAELEMENTAUTOGROUP = "disableDataElementAutoGroup"
    DISPLAYNAME = "displayName"
    DISPLAYOPTIONS = "displayOptions"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    GREYEDFIELDS = "greyedFields"
    HREF = "href"
    ID = "id"
    INDICATORS = "indicators"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    NAME = "name"
    SHARING = "sharing"
    SHOWCOLUMNTOTALS = "showColumnTotals"
    SHOWROWTOTALS = "showRowTotals"
    SORTORDER = "sortOrder"
    TRANSLATIONS = "translations"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
