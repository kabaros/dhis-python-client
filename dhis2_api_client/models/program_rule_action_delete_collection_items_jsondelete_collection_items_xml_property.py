from enum import Enum


class ProgramRuleActionDeleteCollectionItemsJsondeleteCollectionItemsXmlProperty(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    CODE = "code"
    CONTENT = "content"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DATA = "data"
    DATAELEMENT = "dataElement"
    DISPLAYCONTENT = "displayContent"
    DISPLAYNAME = "displayName"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    HREF = "href"
    ID = "id"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    LOCATION = "location"
    NAME = "name"
    OPTION = "option"
    OPTIONGROUP = "optionGroup"
    PROGRAMINDICATOR = "programIndicator"
    PROGRAMRULE = "programRule"
    PROGRAMRULEACTIONEVALUATIONENVIRONMENTS = "programRuleActionEvaluationEnvironments"
    PROGRAMRULEACTIONEVALUATIONTIME = "programRuleActionEvaluationTime"
    PROGRAMRULEACTIONTYPE = "programRuleActionType"
    PROGRAMSTAGE = "programStage"
    PROGRAMSTAGESECTION = "programStageSection"
    SHARING = "sharing"
    TEMPLATEUID = "templateUid"
    TRACKEDENTITYATTRIBUTE = "trackedEntityAttribute"
    TRANSLATIONS = "translations"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
