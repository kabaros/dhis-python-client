from enum import Enum


class ProgramNotificationTemplateDeleteCollectionItemProperty(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DELIVERYCHANNELS = "deliveryChannels"
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
    NOTIFICATIONRECIPIENT = "notificationRecipient"
    NOTIFICATIONTRIGGER = "notificationTrigger"
    NOTIFYPARENTORGANISATIONUNITONLY = "notifyParentOrganisationUnitOnly"
    NOTIFYUSERSINHIERARCHYONLY = "notifyUsersInHierarchyOnly"
    RECIPIENTDATAELEMENT = "recipientDataElement"
    RECIPIENTPROGRAMATTRIBUTE = "recipientProgramAttribute"
    RECIPIENTUSERGROUP = "recipientUserGroup"
    RELATIVESCHEDULEDDAYS = "relativeScheduledDays"
    SENDREPEATABLE = "sendRepeatable"
    SHARING = "sharing"
    SUBJECTTEMPLATE = "subjectTemplate"
    TRANSLATIONS = "translations"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
