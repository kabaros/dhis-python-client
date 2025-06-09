from enum import Enum


class ProgramStageSectionAddCollectionItemProperty(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DATAELEMENTS = "dataElements"
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
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    NAME = "name"
    PROGRAMINDICATORS = "programIndicators"
    PROGRAMSTAGE = "programStage"
    RENDERTYPE = "renderType"
    SHARING = "sharing"
    SHORTNAME = "shortName"
    SORTORDER = "sortOrder"
    STYLE = "style"
    TRANSLATIONS = "translations"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
