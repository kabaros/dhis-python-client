from enum import Enum


class SmsInboundDeleteCollectionItemsJsondeleteCollectionItemsXmlProperty(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DISPLAYNAME = "displayName"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    GATEWAYID = "gatewayid"
    HREF = "href"
    ID = "id"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    NAME = "name"
    ORIGINATOR = "originator"
    RECEIVEDDATE = "receiveddate"
    SENTDATE = "sentdate"
    SHARING = "sharing"
    SMSENCODING = "smsencoding"
    SMSSTATUS = "smsstatus"
    TEXT = "text"
    TRANSLATIONS = "translations"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
