from enum import Enum


class DashboardGetObjectPropertyGistAsCsvProperty(str, Enum):
    ACCESS = "access"
    ALLOWEDFILTERS = "allowedFilters"
    ATTRIBUTEVALUES = "attributeValues"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DASHBOARDITEMS = "dashboardItems"
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
    ITEMCONFIG = "itemConfig"
    ITEMCOUNT = "itemCount"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    LAYOUT = "layout"
    NAME = "name"
    RESTRICTFILTERS = "restrictFilters"
    SHARING = "sharing"
    SHORTNAME = "shortName"
    TRANSLATIONS = "translations"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
