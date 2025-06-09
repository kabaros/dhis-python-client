from enum import Enum


class ReportAddCollectionItemProperty(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    CACHESTRATEGY = "cacheStrategy"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DESIGNCONTENT = "designContent"
    DISPLAYNAME = "displayName"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    HREF = "href"
    ID = "id"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    NAME = "name"
    RELATIVEPERIODS = "relativePeriods"
    REPORTPARAMS = "reportParams"
    SHARING = "sharing"
    TRANSLATIONS = "translations"
    TYPE = "type"
    USER = "user"
    VISUALIZATION = "visualization"

    def __str__(self) -> str:
        return str(self.value)
