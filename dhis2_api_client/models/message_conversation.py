import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.message_conversation_message_type import MessageConversationMessageType
from ..models.message_conversation_priority import MessageConversationPriority
from ..models.message_conversation_status import MessageConversationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.message_conversation_assignee import MessageConversationAssignee
    from ..models.message_conversation_created_by import MessageConversationCreatedBy
    from ..models.message_conversation_last_sender import MessageConversationLastSender
    from ..models.message_conversation_last_updated_by import MessageConversationLastUpdatedBy
    from ..models.message_conversation_messages_item import MessageConversationMessagesItem
    from ..models.message_conversation_user import MessageConversationUser
    from ..models.sharing import Sharing
    from ..models.translation import Translation
    from ..models.user_message import UserMessage


T = TypeVar("T", bound="MessageConversation")


@_attrs_define
class MessageConversation:
    """
    Attributes:
        message_count (int):
        message_type (MessageConversationMessageType):
        priority (MessageConversationPriority):
        status (MessageConversationStatus):
        access (Union[Unset, Access]):
        assignee (Union[Unset, MessageConversationAssignee]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, MessageConversationCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        display_name (Union[Unset, str]):
        ext_message_id (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        follow_up (Union[Unset, bool]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_message (Union[Unset, datetime.datetime]):
        last_sender (Union[Unset, MessageConversationLastSender]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        last_sender_firstname (Union[Unset, str]):
        last_sender_surname (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, MessageConversationLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        messages (Union[Unset, list['MessageConversationMessagesItem']]):
        read (Union[Unset, bool]):
        sharing (Union[Unset, Sharing]):
        subject (Union[Unset, str]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, MessageConversationUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        user_firstname (Union[Unset, str]):
        user_messages (Union[Unset, list['UserMessage']]):
        user_surname (Union[Unset, str]):
    """

    message_count: int
    message_type: MessageConversationMessageType
    priority: MessageConversationPriority
    status: MessageConversationStatus
    access: Union[Unset, "Access"] = UNSET
    assignee: Union[Unset, "MessageConversationAssignee"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "MessageConversationCreatedBy"] = UNSET
    display_name: Union[Unset, str] = UNSET
    ext_message_id: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    follow_up: Union[Unset, bool] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_message: Union[Unset, datetime.datetime] = UNSET
    last_sender: Union[Unset, "MessageConversationLastSender"] = UNSET
    last_sender_firstname: Union[Unset, str] = UNSET
    last_sender_surname: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "MessageConversationLastUpdatedBy"] = UNSET
    messages: Union[Unset, list["MessageConversationMessagesItem"]] = UNSET
    read: Union[Unset, bool] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    subject: Union[Unset, str] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "MessageConversationUser"] = UNSET
    user_firstname: Union[Unset, str] = UNSET
    user_messages: Union[Unset, list["UserMessage"]] = UNSET
    user_surname: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message_count = self.message_count

        message_type = self.message_type.value

        priority = self.priority.value

        status = self.status.value

        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        assignee: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        attribute_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_values, Unset):
            attribute_values = []
            for attribute_values_item_data in self.attribute_values:
                attribute_values_item = attribute_values_item_data.to_dict()
                attribute_values.append(attribute_values_item)

        code = self.code

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        display_name = self.display_name

        ext_message_id = self.ext_message_id

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        follow_up = self.follow_up

        href = self.href

        id = self.id

        last_message: Union[Unset, str] = UNSET
        if not isinstance(self.last_message, Unset):
            last_message = self.last_message.isoformat()

        last_sender: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_sender, Unset):
            last_sender = self.last_sender.to_dict()

        last_sender_firstname = self.last_sender_firstname

        last_sender_surname = self.last_sender_surname

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        messages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)

        read = self.read

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        subject = self.subject

        translations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        user_firstname = self.user_firstname

        user_messages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.user_messages, Unset):
            user_messages = []
            for user_messages_item_data in self.user_messages:
                user_messages_item = user_messages_item_data.to_dict()
                user_messages.append(user_messages_item)

        user_surname = self.user_surname

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messageCount": message_count,
                "messageType": message_type,
                "priority": priority,
                "status": status,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if code is not UNSET:
            field_dict["code"] = code
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if ext_message_id is not UNSET:
            field_dict["extMessageId"] = ext_message_id
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if follow_up is not UNSET:
            field_dict["followUp"] = follow_up
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if last_message is not UNSET:
            field_dict["lastMessage"] = last_message
        if last_sender is not UNSET:
            field_dict["lastSender"] = last_sender
        if last_sender_firstname is not UNSET:
            field_dict["lastSenderFirstname"] = last_sender_firstname
        if last_sender_surname is not UNSET:
            field_dict["lastSenderSurname"] = last_sender_surname
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if messages is not UNSET:
            field_dict["messages"] = messages
        if read is not UNSET:
            field_dict["read"] = read
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if subject is not UNSET:
            field_dict["subject"] = subject
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user
        if user_firstname is not UNSET:
            field_dict["userFirstname"] = user_firstname
        if user_messages is not UNSET:
            field_dict["userMessages"] = user_messages
        if user_surname is not UNSET:
            field_dict["userSurname"] = user_surname

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.message_conversation_assignee import MessageConversationAssignee
        from ..models.message_conversation_created_by import MessageConversationCreatedBy
        from ..models.message_conversation_last_sender import MessageConversationLastSender
        from ..models.message_conversation_last_updated_by import MessageConversationLastUpdatedBy
        from ..models.message_conversation_messages_item import MessageConversationMessagesItem
        from ..models.message_conversation_user import MessageConversationUser
        from ..models.sharing import Sharing
        from ..models.translation import Translation
        from ..models.user_message import UserMessage

        d = src_dict.copy()
        message_count = d.pop("messageCount")

        message_type = MessageConversationMessageType(d.pop("messageType"))

        priority = MessageConversationPriority(d.pop("priority"))

        status = MessageConversationStatus(d.pop("status"))

        _access = d.pop("access", UNSET)
        access: Union[Unset, Access]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

        _assignee = d.pop("assignee", UNSET)
        assignee: Union[Unset, MessageConversationAssignee]
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = MessageConversationAssignee.from_dict(_assignee)

        attribute_values = []
        _attribute_values = d.pop("attributeValues", UNSET)
        for attribute_values_item_data in _attribute_values or []:
            attribute_values_item = AttributeValue.from_dict(attribute_values_item_data)

            attribute_values.append(attribute_values_item)

        code = d.pop("code", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, MessageConversationCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = MessageConversationCreatedBy.from_dict(_created_by)

        display_name = d.pop("displayName", UNSET)

        ext_message_id = d.pop("extMessageId", UNSET)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        follow_up = d.pop("followUp", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _last_message = d.pop("lastMessage", UNSET)
        last_message: Union[Unset, datetime.datetime]
        if isinstance(_last_message, Unset):
            last_message = UNSET
        else:
            last_message = isoparse(_last_message)

        _last_sender = d.pop("lastSender", UNSET)
        last_sender: Union[Unset, MessageConversationLastSender]
        if isinstance(_last_sender, Unset):
            last_sender = UNSET
        else:
            last_sender = MessageConversationLastSender.from_dict(_last_sender)

        last_sender_firstname = d.pop("lastSenderFirstname", UNSET)

        last_sender_surname = d.pop("lastSenderSurname", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, MessageConversationLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = MessageConversationLastUpdatedBy.from_dict(_last_updated_by)

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = MessageConversationMessagesItem.from_dict(messages_item_data)

            messages.append(messages_item)

        read = d.pop("read", UNSET)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        subject = d.pop("subject", UNSET)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, MessageConversationUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = MessageConversationUser.from_dict(_user)

        user_firstname = d.pop("userFirstname", UNSET)

        user_messages = []
        _user_messages = d.pop("userMessages", UNSET)
        for user_messages_item_data in _user_messages or []:
            user_messages_item = UserMessage.from_dict(user_messages_item_data)

            user_messages.append(user_messages_item)

        user_surname = d.pop("userSurname", UNSET)

        message_conversation = cls(
            message_count=message_count,
            message_type=message_type,
            priority=priority,
            status=status,
            access=access,
            assignee=assignee,
            attribute_values=attribute_values,
            code=code,
            created=created,
            created_by=created_by,
            display_name=display_name,
            ext_message_id=ext_message_id,
            favorite=favorite,
            favorites=favorites,
            follow_up=follow_up,
            href=href,
            id=id,
            last_message=last_message,
            last_sender=last_sender,
            last_sender_firstname=last_sender_firstname,
            last_sender_surname=last_sender_surname,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            messages=messages,
            read=read,
            sharing=sharing,
            subject=subject,
            translations=translations,
            user=user,
            user_firstname=user_firstname,
            user_messages=user_messages,
            user_surname=user_surname,
        )

        message_conversation.additional_properties = d
        return message_conversation

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
