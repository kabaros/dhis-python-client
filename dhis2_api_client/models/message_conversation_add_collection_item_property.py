from enum import Enum


class MessageConversationAddCollectionItemProperty(str, Enum):
    ACCESS = "access"
    ASSIGNEE = "assignee"
    ATTRIBUTEVALUES = "attributeValues"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DISPLAYNAME = "displayName"
    EXTMESSAGEID = "extMessageId"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    FOLLOWUP = "followUp"
    HREF = "href"
    ID = "id"
    LASTMESSAGE = "lastMessage"
    LASTSENDER = "lastSender"
    LASTSENDERFIRSTNAME = "lastSenderFirstname"
    LASTSENDERSURNAME = "lastSenderSurname"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    MESSAGECOUNT = "messageCount"
    MESSAGES = "messages"
    MESSAGETYPE = "messageType"
    PRIORITY = "priority"
    READ = "read"
    SHARING = "sharing"
    STATUS = "status"
    SUBJECT = "subject"
    TRANSLATIONS = "translations"
    USER = "user"
    USERFIRSTNAME = "userFirstname"
    USERMESSAGES = "userMessages"
    USERSURNAME = "userSurname"

    def __str__(self) -> str:
        return str(self.value)
