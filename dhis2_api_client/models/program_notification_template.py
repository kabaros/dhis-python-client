import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.program_notification_template_delivery_channels_item import (
    ProgramNotificationTemplateDeliveryChannelsItem,
)
from ..models.program_notification_template_notification_recipient import (
    ProgramNotificationTemplateNotificationRecipient,
)
from ..models.program_notification_template_notification_trigger import ProgramNotificationTemplateNotificationTrigger
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.program_notification_template_created_by import ProgramNotificationTemplateCreatedBy
    from ..models.program_notification_template_last_updated_by import ProgramNotificationTemplateLastUpdatedBy
    from ..models.program_notification_template_recipient_data_element import (
        ProgramNotificationTemplateRecipientDataElement,
    )
    from ..models.program_notification_template_recipient_program_attribute import (
        ProgramNotificationTemplateRecipientProgramAttribute,
    )
    from ..models.program_notification_template_recipient_user_group import (
        ProgramNotificationTemplateRecipientUserGroup,
    )
    from ..models.program_notification_template_user import ProgramNotificationTemplateUser
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="ProgramNotificationTemplate")


@_attrs_define
class ProgramNotificationTemplate:
    """
    Attributes:
        notification_recipient (ProgramNotificationTemplateNotificationRecipient):
        notification_trigger (ProgramNotificationTemplateNotificationTrigger):
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, ProgramNotificationTemplateCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        delivery_channels (Union[Unset, list[ProgramNotificationTemplateDeliveryChannelsItem]]):
        display_message_template (Union[Unset, str]):
        display_name (Union[Unset, str]):
        display_subject_template (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, ProgramNotificationTemplateLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        message_template (Union[Unset, str]):
        name (Union[Unset, str]):
        notify_parent_organisation_unit_only (Union[Unset, bool]):
        notify_users_in_hierarchy_only (Union[Unset, bool]):
        recipient_data_element (Union[Unset, ProgramNotificationTemplateRecipientDataElement]): A UID reference to a
            DataElement
            (Java name `org.hisp.dhis.dataelement.DataElement`)
        recipient_program_attribute (Union[Unset, ProgramNotificationTemplateRecipientProgramAttribute]): A UID
            reference to a TrackedEntityAttribute
            (Java name `org.hisp.dhis.trackedentity.TrackedEntityAttribute`)
        recipient_user_group (Union[Unset, ProgramNotificationTemplateRecipientUserGroup]): A UID reference to a
            UserGroup
            (Java name `org.hisp.dhis.user.UserGroup`)
        relative_scheduled_days (Union[Unset, int]):
        send_repeatable (Union[Unset, bool]):
        sharing (Union[Unset, Sharing]):
        subject_template (Union[Unset, str]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, ProgramNotificationTemplateUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    notification_recipient: ProgramNotificationTemplateNotificationRecipient
    notification_trigger: ProgramNotificationTemplateNotificationTrigger
    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "ProgramNotificationTemplateCreatedBy"] = UNSET
    delivery_channels: Union[Unset, list[ProgramNotificationTemplateDeliveryChannelsItem]] = UNSET
    display_message_template: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    display_subject_template: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "ProgramNotificationTemplateLastUpdatedBy"] = UNSET
    message_template: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    notify_parent_organisation_unit_only: Union[Unset, bool] = UNSET
    notify_users_in_hierarchy_only: Union[Unset, bool] = UNSET
    recipient_data_element: Union[Unset, "ProgramNotificationTemplateRecipientDataElement"] = UNSET
    recipient_program_attribute: Union[Unset, "ProgramNotificationTemplateRecipientProgramAttribute"] = UNSET
    recipient_user_group: Union[Unset, "ProgramNotificationTemplateRecipientUserGroup"] = UNSET
    relative_scheduled_days: Union[Unset, int] = UNSET
    send_repeatable: Union[Unset, bool] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    subject_template: Union[Unset, str] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "ProgramNotificationTemplateUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notification_recipient = self.notification_recipient.value

        notification_trigger = self.notification_trigger.value

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

        display_message_template = self.display_message_template

        display_name = self.display_name

        display_subject_template = self.display_subject_template

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

        message_template = self.message_template

        name = self.name

        notify_parent_organisation_unit_only = self.notify_parent_organisation_unit_only

        notify_users_in_hierarchy_only = self.notify_users_in_hierarchy_only

        recipient_data_element: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.recipient_data_element, Unset):
            recipient_data_element = self.recipient_data_element.to_dict()

        recipient_program_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.recipient_program_attribute, Unset):
            recipient_program_attribute = self.recipient_program_attribute.to_dict()

        recipient_user_group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.recipient_user_group, Unset):
            recipient_user_group = self.recipient_user_group.to_dict()

        relative_scheduled_days = self.relative_scheduled_days

        send_repeatable = self.send_repeatable

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        subject_template = self.subject_template

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
                "notificationRecipient": notification_recipient,
                "notificationTrigger": notification_trigger,
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
        if display_message_template is not UNSET:
            field_dict["displayMessageTemplate"] = display_message_template
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_subject_template is not UNSET:
            field_dict["displaySubjectTemplate"] = display_subject_template
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
        if message_template is not UNSET:
            field_dict["messageTemplate"] = message_template
        if name is not UNSET:
            field_dict["name"] = name
        if notify_parent_organisation_unit_only is not UNSET:
            field_dict["notifyParentOrganisationUnitOnly"] = notify_parent_organisation_unit_only
        if notify_users_in_hierarchy_only is not UNSET:
            field_dict["notifyUsersInHierarchyOnly"] = notify_users_in_hierarchy_only
        if recipient_data_element is not UNSET:
            field_dict["recipientDataElement"] = recipient_data_element
        if recipient_program_attribute is not UNSET:
            field_dict["recipientProgramAttribute"] = recipient_program_attribute
        if recipient_user_group is not UNSET:
            field_dict["recipientUserGroup"] = recipient_user_group
        if relative_scheduled_days is not UNSET:
            field_dict["relativeScheduledDays"] = relative_scheduled_days
        if send_repeatable is not UNSET:
            field_dict["sendRepeatable"] = send_repeatable
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if subject_template is not UNSET:
            field_dict["subjectTemplate"] = subject_template
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.program_notification_template_created_by import ProgramNotificationTemplateCreatedBy
        from ..models.program_notification_template_last_updated_by import ProgramNotificationTemplateLastUpdatedBy
        from ..models.program_notification_template_recipient_data_element import (
            ProgramNotificationTemplateRecipientDataElement,
        )
        from ..models.program_notification_template_recipient_program_attribute import (
            ProgramNotificationTemplateRecipientProgramAttribute,
        )
        from ..models.program_notification_template_recipient_user_group import (
            ProgramNotificationTemplateRecipientUserGroup,
        )
        from ..models.program_notification_template_user import ProgramNotificationTemplateUser
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        notification_recipient = ProgramNotificationTemplateNotificationRecipient(d.pop("notificationRecipient"))

        notification_trigger = ProgramNotificationTemplateNotificationTrigger(d.pop("notificationTrigger"))

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
        created_by: Union[Unset, ProgramNotificationTemplateCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = ProgramNotificationTemplateCreatedBy.from_dict(_created_by)

        delivery_channels = []
        _delivery_channels = d.pop("deliveryChannels", UNSET)
        for delivery_channels_item_data in _delivery_channels or []:
            delivery_channels_item = ProgramNotificationTemplateDeliveryChannelsItem(delivery_channels_item_data)

            delivery_channels.append(delivery_channels_item)

        display_message_template = d.pop("displayMessageTemplate", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_subject_template = d.pop("displaySubjectTemplate", UNSET)

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
        last_updated_by: Union[Unset, ProgramNotificationTemplateLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = ProgramNotificationTemplateLastUpdatedBy.from_dict(_last_updated_by)

        message_template = d.pop("messageTemplate", UNSET)

        name = d.pop("name", UNSET)

        notify_parent_organisation_unit_only = d.pop("notifyParentOrganisationUnitOnly", UNSET)

        notify_users_in_hierarchy_only = d.pop("notifyUsersInHierarchyOnly", UNSET)

        _recipient_data_element = d.pop("recipientDataElement", UNSET)
        recipient_data_element: Union[Unset, ProgramNotificationTemplateRecipientDataElement]
        if isinstance(_recipient_data_element, Unset):
            recipient_data_element = UNSET
        else:
            recipient_data_element = ProgramNotificationTemplateRecipientDataElement.from_dict(_recipient_data_element)

        _recipient_program_attribute = d.pop("recipientProgramAttribute", UNSET)
        recipient_program_attribute: Union[Unset, ProgramNotificationTemplateRecipientProgramAttribute]
        if isinstance(_recipient_program_attribute, Unset):
            recipient_program_attribute = UNSET
        else:
            recipient_program_attribute = ProgramNotificationTemplateRecipientProgramAttribute.from_dict(
                _recipient_program_attribute
            )

        _recipient_user_group = d.pop("recipientUserGroup", UNSET)
        recipient_user_group: Union[Unset, ProgramNotificationTemplateRecipientUserGroup]
        if isinstance(_recipient_user_group, Unset):
            recipient_user_group = UNSET
        else:
            recipient_user_group = ProgramNotificationTemplateRecipientUserGroup.from_dict(_recipient_user_group)

        relative_scheduled_days = d.pop("relativeScheduledDays", UNSET)

        send_repeatable = d.pop("sendRepeatable", UNSET)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        subject_template = d.pop("subjectTemplate", UNSET)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, ProgramNotificationTemplateUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ProgramNotificationTemplateUser.from_dict(_user)

        program_notification_template = cls(
            notification_recipient=notification_recipient,
            notification_trigger=notification_trigger,
            access=access,
            attribute_values=attribute_values,
            code=code,
            created=created,
            created_by=created_by,
            delivery_channels=delivery_channels,
            display_message_template=display_message_template,
            display_name=display_name,
            display_subject_template=display_subject_template,
            favorite=favorite,
            favorites=favorites,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            message_template=message_template,
            name=name,
            notify_parent_organisation_unit_only=notify_parent_organisation_unit_only,
            notify_users_in_hierarchy_only=notify_users_in_hierarchy_only,
            recipient_data_element=recipient_data_element,
            recipient_program_attribute=recipient_program_attribute,
            recipient_user_group=recipient_user_group,
            relative_scheduled_days=relative_scheduled_days,
            send_repeatable=send_repeatable,
            sharing=sharing,
            subject_template=subject_template,
            translations=translations,
            user=user,
        )

        program_notification_template.additional_properties = d
        return program_notification_template

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
