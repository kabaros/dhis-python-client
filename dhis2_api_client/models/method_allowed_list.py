from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodAllowedList")


@_attrs_define
class MethodAllowedList:
    """
    Attributes:
        allowed_methods (Union[Unset, list[str]]):
        type_ (Union[Unset, str]):
    """

    allowed_methods: Union[Unset, list[str]] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_methods: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allowed_methods, Unset):
            allowed_methods = self.allowed_methods

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowed_methods is not UNSET:
            field_dict["allowedMethods"] = allowed_methods
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        allowed_methods = cast(list[str], d.pop("allowedMethods", UNSET))

        type_ = d.pop("type", UNSET)

        method_allowed_list = cls(
            allowed_methods=allowed_methods,
            type_=type_,
        )

        method_allowed_list.additional_properties = d
        return method_allowed_list

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
