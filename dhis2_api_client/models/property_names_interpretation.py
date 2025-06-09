from enum import Enum


class PropertyNamesInterpretation(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    CODE = "code"
    COMMENTS = "comments"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DATASET = "dataSet"
    DISPLAYNAME = "displayName"
    EVENTCHART = "eventChart"
    EVENTREPORT = "eventReport"
    EVENTVISUALIZATION = "eventVisualization"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    HREF = "href"
    ID = "id"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    LIKEDBY = "likedBy"
    LIKES = "likes"
    MAP = "map"
    MENTIONS = "mentions"
    ORGANISATIONUNIT = "organisationUnit"
    PERIOD = "period"
    SHARING = "sharing"
    TEXT = "text"
    TRANSLATIONS = "translations"
    TYPE = "type"
    USER = "user"
    VISUALIZATION = "visualization"

    def __str__(self) -> str:
        return str(self.value)
