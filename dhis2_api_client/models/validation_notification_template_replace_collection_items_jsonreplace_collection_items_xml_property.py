from enum import Enum


class ValidationNotificationTemplateReplaceCollectionItemsJsonreplaceCollectionItemsXmlProperty(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DISPLAYMESSAGETEMPLATE = "displayMessageTemplate"
    DISPLAYNAME = "displayName"
    DISPLAYSUBJECTTEMPLATE = "displaySubjectTemplate"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    HREF = "href"
    ID = "id"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    MESSAGETEMPLATE = "messageTemplate"
    NAME = "name"
    NOTIFYPARENTORGANISATIONUNITONLY = "notifyParentOrganisationUnitOnly"
    NOTIFYUSERSINHIERARCHYONLY = "notifyUsersInHierarchyOnly"
    RECIPIENTUSERGROUPS = "recipientUserGroups"
    SENDSTRATEGY = "sendStrategy"
    SHARING = "sharing"
    SUBJECTTEMPLATE = "subjectTemplate"
    TRANSLATIONS = "translations"
    USER = "user"
    VALIDATIONRULES = "validationRules"

    def __str__(self) -> str:
        return str(self.value)
