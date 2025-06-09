from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Filter")


@_attrs_define
class Filter:
    """
    Attributes:
        dimension (Union[Unset, str]):
        items (Union[Unset, list[str]]):
    """

    dimension: Union[Unset, str] = UNSET
    items: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dimension = self.dimension

        items: Union[Unset, list[str]] = UNSET
        if not isinstance(self.items, Unset):
            items = self.items

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dimension is not UNSET:
            field_dict["dimension"] = dimension
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        dimension = d.pop("dimension", UNSET)

        items = cast(list[str], d.pop("items", UNSET))

        filter_ = cls(
            dimension=dimension,
            items=items,
        )

        filter_.additional_properties = d
        return filter_

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
