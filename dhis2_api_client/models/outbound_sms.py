import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.outbound_sms_status import OutboundSmsStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.outbound_sms_created_by import OutboundSmsCreatedBy
    from ..models.outbound_sms_last_updated_by import OutboundSmsLastUpdatedBy
    from ..models.outbound_sms_user import OutboundSmsUser
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="OutboundSms")


@_attrs_define
class OutboundSms:
    """
    Attributes:
        status (OutboundSmsStatus):
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, OutboundSmsCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        date (Union[Unset, datetime.datetime]):
        display_name (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, OutboundSmsLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        message (Union[Unset, str]):
        name (Union[Unset, str]):
        recipients (Union[Unset, list[str]]):
        sender (Union[Unset, str]):
        sharing (Union[Unset, Sharing]):
        subject (Union[Unset, str]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, OutboundSmsUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    status: OutboundSmsStatus
    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "OutboundSmsCreatedBy"] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    display_name: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "OutboundSmsLastUpdatedBy"] = UNSET
    message: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    recipients: Union[Unset, list[str]] = UNSET
    sender: Union[Unset, str] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    subject: Union[Unset, str] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "OutboundSmsUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

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

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        display_name = self.display_name

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

        message = self.message

        name = self.name

        recipients: Union[Unset, list[str]] = UNSET
        if not isinstance(self.recipients, Unset):
            recipients = self.recipients

        sender = self.sender

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
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
        if date is not UNSET:
            field_dict["date"] = date
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
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
        if message is not UNSET:
            field_dict["message"] = message
        if name is not UNSET:
            field_dict["name"] = name
        if recipients is not UNSET:
            field_dict["recipients"] = recipients
        if sender is not UNSET:
            field_dict["sender"] = sender
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if subject is not UNSET:
            field_dict["subject"] = subject
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.outbound_sms_created_by import OutboundSmsCreatedBy
        from ..models.outbound_sms_last_updated_by import OutboundSmsLastUpdatedBy
        from ..models.outbound_sms_user import OutboundSmsUser
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        status = OutboundSmsStatus(d.pop("status"))

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
        created_by: Union[Unset, OutboundSmsCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = OutboundSmsCreatedBy.from_dict(_created_by)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        display_name = d.pop("displayName", UNSET)

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
        last_updated_by: Union[Unset, OutboundSmsLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = OutboundSmsLastUpdatedBy.from_dict(_last_updated_by)

        message = d.pop("message", UNSET)

        name = d.pop("name", UNSET)

        recipients = cast(list[str], d.pop("recipients", UNSET))

        sender = d.pop("sender", UNSET)

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
        user: Union[Unset, OutboundSmsUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = OutboundSmsUser.from_dict(_user)

        outbound_sms = cls(
            status=status,
            access=access,
            attribute_values=attribute_values,
            code=code,
            created=created,
            created_by=created_by,
            date=date,
            display_name=display_name,
            favorite=favorite,
            favorites=favorites,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            message=message,
            name=name,
            recipients=recipients,
            sender=sender,
            sharing=sharing,
            subject=subject,
            translations=translations,
            user=user,
        )

        outbound_sms.additional_properties = d
        return outbound_sms

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
