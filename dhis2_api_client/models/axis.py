from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Axis")


@_attrs_define
class Axis:
    """
    Attributes:
        axis (Union[Unset, int]):
        dimensional_item (Union[Unset, str]):
    """

    axis: Union[Unset, int] = UNSET
    dimensional_item: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        axis = self.axis

        dimensional_item = self.dimensional_item

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if axis is not UNSET:
            field_dict["axis"] = axis
        if dimensional_item is not UNSET:
            field_dict["dimensionalItem"] = dimensional_item

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        axis = d.pop("axis", UNSET)

        dimensional_item = d.pop("dimensionalItem", UNSET)

        axis = cls(
            axis=axis,
            dimensional_item=dimensional_item,
        )

        axis.additional_properties = d
        return axis

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
