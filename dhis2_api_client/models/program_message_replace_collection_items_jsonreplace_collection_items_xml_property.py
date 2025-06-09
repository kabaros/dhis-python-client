from enum import Enum


class ProgramMessageReplaceCollectionItemsJsonreplaceCollectionItemsXmlProperty(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DELIVERYCHANNELS = "deliveryChannels"
    DISPLAYNAME = "displayName"
    ENROLLMENT = "enrollment"
    EVENT = "event"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    HREF = "href"
    ID = "id"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    MESSAGESTATUS = "messageStatus"
    NAME = "name"
    NOTIFICATIONTEMPLATE = "notificationTemplate"
    PROCESSEDDATE = "processedDate"
    RECIPIENTS = "recipients"
    SHARING = "sharing"
    STORECOPY = "storeCopy"
    SUBJECT = "subject"
    TEXT = "text"
    TRANSLATIONS = "translations"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
