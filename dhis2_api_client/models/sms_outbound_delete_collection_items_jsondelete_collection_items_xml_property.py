from enum import Enum


class SmsOutboundDeleteCollectionItemsJsondeleteCollectionItemsXmlProperty(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DATE = "date"
    DISPLAYNAME = "displayName"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    HREF = "href"
    ID = "id"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    MESSAGE = "message"
    NAME = "name"
    RECIPIENTS = "recipients"
    SENDER = "sender"
    SHARING = "sharing"
    STATUS = "status"
    SUBJECT = "subject"
    TRANSLATIONS = "translations"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
