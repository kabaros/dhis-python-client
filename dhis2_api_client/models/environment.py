from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Environment")


@_attrs_define
class Environment:
    """
    Attributes:
        active_profiles (Union[Unset, list[str]]):
        default_profiles (Union[Unset, list[str]]):
    """

    active_profiles: Union[Unset, list[str]] = UNSET
    default_profiles: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_profiles: Union[Unset, list[str]] = UNSET
        if not isinstance(self.active_profiles, Unset):
            active_profiles = self.active_profiles

        default_profiles: Union[Unset, list[str]] = UNSET
        if not isinstance(self.default_profiles, Unset):
            default_profiles = self.default_profiles

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_profiles is not UNSET:
            field_dict["activeProfiles"] = active_profiles
        if default_profiles is not UNSET:
            field_dict["defaultProfiles"] = default_profiles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        active_profiles = cast(list[str], d.pop("activeProfiles", UNSET))

        default_profiles = cast(list[str], d.pop("defaultProfiles", UNSET))

        environment = cls(
            active_profiles=active_profiles,
            default_profiles=default_profiles,
        )

        environment.additional_properties = d
        return environment

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
