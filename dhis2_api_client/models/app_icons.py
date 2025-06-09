from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppIcons")


@_attrs_define
class AppIcons:
    """
    Attributes:
        field_128 (Union[Unset, str]):
        field_16 (Union[Unset, str]):
        field_48 (Union[Unset, str]):
    """

    field_128: Union[Unset, str] = UNSET
    field_16: Union[Unset, str] = UNSET
    field_48: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_128 = self.field_128

        field_16 = self.field_16

        field_48 = self.field_48

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_128 is not UNSET:
            field_dict["128"] = field_128
        if field_16 is not UNSET:
            field_dict["16"] = field_16
        if field_48 is not UNSET:
            field_dict["48"] = field_48

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        field_128 = d.pop("128", UNSET)

        field_16 = d.pop("16", UNSET)

        field_48 = d.pop("48", UNSET)

        app_icons = cls(
            field_128=field_128,
            field_16=field_16,
            field_48=field_48,
        )

        app_icons.additional_properties = d
        return app_icons

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
