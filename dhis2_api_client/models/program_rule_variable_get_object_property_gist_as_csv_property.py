from enum import Enum


class ProgramRuleVariableGetObjectPropertyGistAsCsvProperty(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DATAELEMENT = "dataElement"
    DISPLAYNAME = "displayName"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    HREF = "href"
    ID = "id"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    NAME = "name"
    PROGRAM = "program"
    PROGRAMRULEVARIABLESOURCETYPE = "programRuleVariableSourceType"
    PROGRAMSTAGE = "programStage"
    SHARING = "sharing"
    TRACKEDENTITYATTRIBUTE = "trackedEntityAttribute"
    TRANSLATIONS = "translations"
    USECODEFOROPTIONSET = "useCodeForOptionSet"
    USER = "user"
    VALUETYPE = "valueType"

    def __str__(self) -> str:
        return str(self.value)
