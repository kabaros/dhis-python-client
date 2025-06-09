from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_conversation_info_attachments_item import MessageConversationInfoAttachmentsItem
    from ..models.message_conversation_info_organisation_units_item import MessageConversationInfoOrganisationUnitsItem
    from ..models.message_conversation_info_user_groups_item import MessageConversationInfoUserGroupsItem
    from ..models.message_conversation_info_users_item import MessageConversationInfoUsersItem


T = TypeVar("T", bound="MessageConversationInfo")


@_attrs_define
class MessageConversationInfo:
    """
    Attributes:
        attachments (Union[Unset, list['MessageConversationInfoAttachmentsItem']]):
        organisation_units (Union[Unset, list['MessageConversationInfoOrganisationUnitsItem']]):
        subject (Union[Unset, str]):
        text (Union[Unset, str]):
        user_groups (Union[Unset, list['MessageConversationInfoUserGroupsItem']]):
        users (Union[Unset, list['MessageConversationInfoUsersItem']]):
    """

    attachments: Union[Unset, list["MessageConversationInfoAttachmentsItem"]] = UNSET
    organisation_units: Union[Unset, list["MessageConversationInfoOrganisationUnitsItem"]] = UNSET
    subject: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    user_groups: Union[Unset, list["MessageConversationInfoUserGroupsItem"]] = UNSET
    users: Union[Unset, list["MessageConversationInfoUsersItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attachments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        organisation_units: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.organisation_units, Unset):
            organisation_units = []
            for organisation_units_item_data in self.organisation_units:
                organisation_units_item = organisation_units_item_data.to_dict()
                organisation_units.append(organisation_units_item)

        subject = self.subject

        text = self.text

        user_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.user_groups, Unset):
            user_groups = []
            for user_groups_item_data in self.user_groups:
                user_groups_item = user_groups_item_data.to_dict()
                user_groups.append(user_groups_item)

        users: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if organisation_units is not UNSET:
            field_dict["organisationUnits"] = organisation_units
        if subject is not UNSET:
            field_dict["subject"] = subject
        if text is not UNSET:
            field_dict["text"] = text
        if user_groups is not UNSET:
            field_dict["userGroups"] = user_groups
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.message_conversation_info_attachments_item import MessageConversationInfoAttachmentsItem
        from ..models.message_conversation_info_organisation_units_item import (
            MessageConversationInfoOrganisationUnitsItem,
        )
        from ..models.message_conversation_info_user_groups_item import MessageConversationInfoUserGroupsItem
        from ..models.message_conversation_info_users_item import MessageConversationInfoUsersItem

        d = src_dict.copy()
        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = MessageConversationInfoAttachmentsItem.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        organisation_units = []
        _organisation_units = d.pop("organisationUnits", UNSET)
        for organisation_units_item_data in _organisation_units or []:
            organisation_units_item = MessageConversationInfoOrganisationUnitsItem.from_dict(
                organisation_units_item_data
            )

            organisation_units.append(organisation_units_item)

        subject = d.pop("subject", UNSET)

        text = d.pop("text", UNSET)

        user_groups = []
        _user_groups = d.pop("userGroups", UNSET)
        for user_groups_item_data in _user_groups or []:
            user_groups_item = MessageConversationInfoUserGroupsItem.from_dict(user_groups_item_data)

            user_groups.append(user_groups_item)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = MessageConversationInfoUsersItem.from_dict(users_item_data)

            users.append(users_item)

        message_conversation_info = cls(
            attachments=attachments,
            organisation_units=organisation_units,
            subject=subject,
            text=text,
            user_groups=user_groups,
            users=users,
        )

        message_conversation_info.additional_properties = d
        return message_conversation_info

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
