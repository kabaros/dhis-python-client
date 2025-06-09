from enum import Enum


class DataApprovalWorkflowGetObjectPropertyGistgetObjectPropertyGistAsCsvProperty(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    CATEGORYCOMBO = "categoryCombo"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DATAAPPROVALLEVELS = "dataApprovalLevels"
    DATASETS = "dataSets"
    DISPLAYNAME = "displayName"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    HREF = "href"
    ID = "id"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    NAME = "name"
    PERIODTYPE = "periodType"
    SHARING = "sharing"
    TRANSLATIONS = "translations"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
