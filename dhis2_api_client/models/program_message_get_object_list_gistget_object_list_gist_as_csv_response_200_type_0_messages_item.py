from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProgramMessageGetObjectListGistgetObjectListGistAsCsvResponse200Type0MessagesItem")


@_attrs_define
class ProgramMessageGetObjectListGistgetObjectListGistAsCsvResponse200Type0MessagesItem:
    """ """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        program_message_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_messages_item = cls()

        program_message_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_messages_item.additional_properties = d
        return program_message_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_messages_item

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
