from enum import Enum


class TrackedEntityFilterGetObjectPropertyProperty(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DESCRIPTION = "description"
    DISPLAYDESCRIPTION = "displayDescription"
    DISPLAYNAME = "displayName"
    ENROLLMENTCREATEDPERIOD = "enrollmentCreatedPeriod"
    ENROLLMENTSTATUS = "enrollmentStatus"
    ENTITYQUERYCRITERIA = "entityQueryCriteria"
    EVENTFILTERS = "eventFilters"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    FOLLOWUP = "followup"
    HREF = "href"
    ID = "id"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    NAME = "name"
    PROGRAM = "program"
    SHARING = "sharing"
    SORTORDER = "sortOrder"
    STYLE = "style"
    TRANSLATIONS = "translations"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
