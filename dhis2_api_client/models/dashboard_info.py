from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DashboardInfo")


@_attrs_define
class DashboardInfo:
    """
    Attributes:
        unread_interpretations (int):
        unread_message_conversations (int):
    """

    unread_interpretations: int
    unread_message_conversations: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unread_interpretations = self.unread_interpretations

        unread_message_conversations = self.unread_message_conversations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unreadInterpretations": unread_interpretations,
                "unreadMessageConversations": unread_message_conversations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        unread_interpretations = d.pop("unreadInterpretations")

        unread_message_conversations = d.pop("unreadMessageConversations")

        dashboard_info = cls(
            unread_interpretations=unread_interpretations,
            unread_message_conversations=unread_message_conversations,
        )

        dashboard_info.additional_properties = d
        return dashboard_info

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
