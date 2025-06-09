from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Meta")


@_attrs_define
class Meta:
    """
    Attributes:
        allow_external_access (Union[Unset, bool]):
        allow_public_access (Union[Unset, bool]):
    """

    allow_external_access: Union[Unset, bool] = UNSET
    allow_public_access: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_external_access = self.allow_external_access

        allow_public_access = self.allow_public_access

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_external_access is not UNSET:
            field_dict["allowExternalAccess"] = allow_external_access
        if allow_public_access is not UNSET:
            field_dict["allowPublicAccess"] = allow_public_access

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        allow_external_access = d.pop("allowExternalAccess", UNSET)

        allow_public_access = d.pop("allowPublicAccess", UNSET)

        meta = cls(
            allow_external_access=allow_external_access,
            allow_public_access=allow_public_access,
        )

        meta.additional_properties = d
        return meta

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
