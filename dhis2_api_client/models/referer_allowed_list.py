from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RefererAllowedList")


@_attrs_define
class RefererAllowedList:
    """
    Attributes:
        allowed_referrers (Union[Unset, list[str]]):
        type_ (Union[Unset, str]):
    """

    allowed_referrers: Union[Unset, list[str]] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_referrers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allowed_referrers, Unset):
            allowed_referrers = self.allowed_referrers

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowed_referrers is not UNSET:
            field_dict["allowedReferrers"] = allowed_referrers
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        allowed_referrers = cast(list[str], d.pop("allowedReferrers", UNSET))

        type_ = d.pop("type", UNSET)

        referer_allowed_list = cls(
            allowed_referrers=allowed_referrers,
            type_=type_,
        )

        referer_allowed_list.additional_properties = d
        return referer_allowed_list

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
