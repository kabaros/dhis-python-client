from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gist_pager import GistPager
    from ..models.message_conversation_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_message_conversations_item import (
        MessageConversationGetObjectListGistgetObjectListGistAsCsvResponse200Type0MessageConversationsItem,
    )


T = TypeVar("T", bound="MessageConversationGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class MessageConversationGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        message_conversations (Union[Unset,
            list['MessageConversationGetObjectListGistgetObjectListGistAsCsvResponse200Type0MessageConversationsItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    message_conversations: Union[
        Unset,
        list["MessageConversationGetObjectListGistgetObjectListGistAsCsvResponse200Type0MessageConversationsItem"],
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        message_conversations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.message_conversations, Unset):
            message_conversations = []
            for message_conversations_item_data in self.message_conversations:
                message_conversations_item = message_conversations_item_data.to_dict()
                message_conversations.append(message_conversations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if message_conversations is not UNSET:
            field_dict["messageConversations"] = message_conversations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.gist_pager import GistPager
        from ..models.message_conversation_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_message_conversations_item import (
            MessageConversationGetObjectListGistgetObjectListGistAsCsvResponse200Type0MessageConversationsItem,
        )

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        message_conversations = []
        _message_conversations = d.pop("messageConversations", UNSET)
        for message_conversations_item_data in _message_conversations or []:
            message_conversations_item = MessageConversationGetObjectListGistgetObjectListGistAsCsvResponse200Type0MessageConversationsItem.from_dict(
                message_conversations_item_data
            )

            message_conversations.append(message_conversations_item)

        message_conversation_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            message_conversations=message_conversations,
        )

        message_conversation_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return message_conversation_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
