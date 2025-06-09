from enum import Enum


class DataSetNotificationTemplateGetObjectPropertyGistgetObjectPropertyGistAsCsvProperty(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DATASETNOTIFICATIONTRIGGER = "dataSetNotificationTrigger"
    DATASETS = "dataSets"
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
    NOTIFYPARENTORGANISATIONUNITONLY = "notifyParentOrganisationUnitOnly"
    NOTIFYUSERSINHIERARCHYONLY = "notifyUsersInHierarchyOnly"
    RECIPIENTUSERGROUP = "recipientUserGroup"
    RELATIVESCHEDULEDDAYS = "relativeScheduledDays"
    SENDSTRATEGY = "sendStrategy"
    SHARING = "sharing"
    SUBJECTTEMPLATE = "subjectTemplate"
    TRANSLATIONS = "translations"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
