from enum import Enum


class SqlViewGetObjectPropertyGistAsCsvProperty(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    CACHESTRATEGY = "cacheStrategy"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DESCRIPTION = "description"
    DISPLAYNAME = "displayName"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    HREF = "href"
    ID = "id"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    NAME = "name"
    SHARING = "sharing"
    SQLQUERY = "sqlQuery"
    TRANSLATIONS = "translations"
    TYPE = "type"
    UPDATEJOBID = "updateJobId"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
