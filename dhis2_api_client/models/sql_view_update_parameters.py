from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SqlViewUpdateParameters")


@_attrs_define
class SqlViewUpdateParameters:
    """
    Attributes:
        sql_views (Union[Unset, list[str]]):
    """

    sql_views: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sql_views: Union[Unset, list[str]] = UNSET
        if not isinstance(self.sql_views, Unset):
            sql_views = self.sql_views

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sql_views is not UNSET:
            field_dict["sqlViews"] = sql_views

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        sql_views = cast(list[str], d.pop("sqlViews", UNSET))

        sql_view_update_parameters = cls(
            sql_views=sql_views,
        )

        sql_view_update_parameters.additional_properties = d
        return sql_view_update_parameters

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
