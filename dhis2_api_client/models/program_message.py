import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.program_message_delivery_channels_item import ProgramMessageDeliveryChannelsItem
from ..models.program_message_message_status import ProgramMessageMessageStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.program_message_created_by import ProgramMessageCreatedBy
    from ..models.program_message_enrollment import ProgramMessageEnrollment
    from ..models.program_message_event import ProgramMessageEvent
    from ..models.program_message_last_updated_by import ProgramMessageLastUpdatedBy
    from ..models.program_message_recipients import ProgramMessageRecipients
    from ..models.program_message_user import ProgramMessageUser
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="ProgramMessage")


@_attrs_define
class ProgramMessage:
    """
    Attributes:
        message_status (ProgramMessageMessageStatus):
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, ProgramMessageCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        delivery_channels (Union[Unset, list[ProgramMessageDeliveryChannelsItem]]):
        display_name (Union[Unset, str]):
        enrollment (Union[Unset, ProgramMessageEnrollment]): A UID reference to a Enrollment
            (Java name `org.hisp.dhis.program.Enrollment`)
        event (Union[Unset, ProgramMessageEvent]): A UID reference to a Event
            (Java name `org.hisp.dhis.program.Event`)
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, ProgramMessageLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        name (Union[Unset, str]):
        notification_template (Union[Unset, str]):
        processed_date (Union[Unset, datetime.datetime]):
        recipients (Union[Unset, ProgramMessageRecipients]):
        sharing (Union[Unset, Sharing]):
        store_copy (Union[Unset, bool]):
        subject (Union[Unset, str]):
        text (Union[Unset, str]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, ProgramMessageUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    message_status: ProgramMessageMessageStatus
    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "ProgramMessageCreatedBy"] = UNSET
    delivery_channels: Union[Unset, list[ProgramMessageDeliveryChannelsItem]] = UNSET
    display_name: Union[Unset, str] = UNSET
    enrollment: Union[Unset, "ProgramMessageEnrollment"] = UNSET
    event: Union[Unset, "ProgramMessageEvent"] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "ProgramMessageLastUpdatedBy"] = UNSET
    name: Union[Unset, str] = UNSET
    notification_template: Union[Unset, str] = UNSET
    processed_date: Union[Unset, datetime.datetime] = UNSET
    recipients: Union[Unset, "ProgramMessageRecipients"] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    store_copy: Union[Unset, bool] = UNSET
    subject: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "ProgramMessageUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message_status = self.message_status.value

        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

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

        delivery_channels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.delivery_channels, Unset):
            delivery_channels = []
            for delivery_channels_item_data in self.delivery_channels:
                delivery_channels_item = delivery_channels_item_data.value
                delivery_channels.append(delivery_channels_item)

        display_name = self.display_name

        enrollment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.enrollment, Unset):
            enrollment = self.enrollment.to_dict()

        event: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.to_dict()

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        href = self.href

        id = self.id

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        name = self.name

        notification_template = self.notification_template

        processed_date: Union[Unset, str] = UNSET
        if not isinstance(self.processed_date, Unset):
            processed_date = self.processed_date.isoformat()

        recipients: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.recipients, Unset):
            recipients = self.recipients.to_dict()

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        store_copy = self.store_copy

        subject = self.subject

        text = self.text

        translations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messageStatus": message_status,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if code is not UNSET:
            field_dict["code"] = code
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if delivery_channels is not UNSET:
            field_dict["deliveryChannels"] = delivery_channels
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if enrollment is not UNSET:
            field_dict["enrollment"] = enrollment
        if event is not UNSET:
            field_dict["event"] = event
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if name is not UNSET:
            field_dict["name"] = name
        if notification_template is not UNSET:
            field_dict["notificationTemplate"] = notification_template
        if processed_date is not UNSET:
            field_dict["processedDate"] = processed_date
        if recipients is not UNSET:
            field_dict["recipients"] = recipients
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if store_copy is not UNSET:
            field_dict["storeCopy"] = store_copy
        if subject is not UNSET:
            field_dict["subject"] = subject
        if text is not UNSET:
            field_dict["text"] = text
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.program_message_created_by import ProgramMessageCreatedBy
        from ..models.program_message_enrollment import ProgramMessageEnrollment
        from ..models.program_message_event import ProgramMessageEvent
        from ..models.program_message_last_updated_by import ProgramMessageLastUpdatedBy
        from ..models.program_message_recipients import ProgramMessageRecipients
        from ..models.program_message_user import ProgramMessageUser
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        message_status = ProgramMessageMessageStatus(d.pop("messageStatus"))

        _access = d.pop("access", UNSET)
        access: Union[Unset, Access]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

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
        created_by: Union[Unset, ProgramMessageCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = ProgramMessageCreatedBy.from_dict(_created_by)

        delivery_channels = []
        _delivery_channels = d.pop("deliveryChannels", UNSET)
        for delivery_channels_item_data in _delivery_channels or []:
            delivery_channels_item = ProgramMessageDeliveryChannelsItem(delivery_channels_item_data)

            delivery_channels.append(delivery_channels_item)

        display_name = d.pop("displayName", UNSET)

        _enrollment = d.pop("enrollment", UNSET)
        enrollment: Union[Unset, ProgramMessageEnrollment]
        if isinstance(_enrollment, Unset):
            enrollment = UNSET
        else:
            enrollment = ProgramMessageEnrollment.from_dict(_enrollment)

        _event = d.pop("event", UNSET)
        event: Union[Unset, ProgramMessageEvent]
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = ProgramMessageEvent.from_dict(_event)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, ProgramMessageLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = ProgramMessageLastUpdatedBy.from_dict(_last_updated_by)

        name = d.pop("name", UNSET)

        notification_template = d.pop("notificationTemplate", UNSET)

        _processed_date = d.pop("processedDate", UNSET)
        processed_date: Union[Unset, datetime.datetime]
        if isinstance(_processed_date, Unset):
            processed_date = UNSET
        else:
            processed_date = isoparse(_processed_date)

        _recipients = d.pop("recipients", UNSET)
        recipients: Union[Unset, ProgramMessageRecipients]
        if isinstance(_recipients, Unset):
            recipients = UNSET
        else:
            recipients = ProgramMessageRecipients.from_dict(_recipients)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        store_copy = d.pop("storeCopy", UNSET)

        subject = d.pop("subject", UNSET)

        text = d.pop("text", UNSET)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, ProgramMessageUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ProgramMessageUser.from_dict(_user)

        program_message = cls(
            message_status=message_status,
            access=access,
            attribute_values=attribute_values,
            code=code,
            created=created,
            created_by=created_by,
            delivery_channels=delivery_channels,
            display_name=display_name,
            enrollment=enrollment,
            event=event,
            favorite=favorite,
            favorites=favorites,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            name=name,
            notification_template=notification_template,
            processed_date=processed_date,
            recipients=recipients,
            sharing=sharing,
            store_copy=store_copy,
            subject=subject,
            text=text,
            translations=translations,
            user=user,
        )

        program_message.additional_properties = d
        return program_message

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
