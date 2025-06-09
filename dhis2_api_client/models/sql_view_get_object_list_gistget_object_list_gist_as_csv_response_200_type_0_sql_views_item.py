from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SqlViewGetObjectListGistgetObjectListGistAsCsvResponse200Type0SqlViewsItem")


@_attrs_define
class SqlViewGetObjectListGistgetObjectListGistAsCsvResponse200Type0SqlViewsItem:
    """ """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        sql_view_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_sql_views_item = cls()

        sql_view_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_sql_views_item.additional_properties = d
        return sql_view_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_sql_views_item

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
