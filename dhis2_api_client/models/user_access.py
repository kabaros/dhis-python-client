from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAccess")


@_attrs_define
class UserAccess:
    """
    Attributes:
        access (Union[Unset, str]):
        display_name (Union[Unset, str]):
        id (Union[Unset, str]):
    """

    access: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access = self.access

        display_name = self.display_name

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access is not UNSET:
            field_dict["access"] = access
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        access = d.pop("access", UNSET)

        display_name = d.pop("displayName", UNSET)

        id = d.pop("id", UNSET)

        user_access = cls(
            access=access,
            display_name=display_name,
            id=id,
        )

        user_access.additional_properties = d
        return user_access

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
