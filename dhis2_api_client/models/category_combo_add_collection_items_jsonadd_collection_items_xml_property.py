from enum import Enum


class CategoryComboAddCollectionItemsJsonaddCollectionItemsXmlProperty(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    CATEGORIES = "categories"
    CATEGORYOPTIONCOMBOS = "categoryOptionCombos"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DATADIMENSIONTYPE = "dataDimensionType"
    DISPLAYNAME = "displayName"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    HREF = "href"
    ID = "id"
    ISDEFAULT = "isDefault"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    NAME = "name"
    SHARING = "sharing"
    SKIPTOTAL = "skipTotal"
    TRANSLATIONS = "translations"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
