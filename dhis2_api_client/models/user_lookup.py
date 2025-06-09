from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserLookup")


@_attrs_define
class UserLookup:
    """
    Attributes:
        display_name (Union[Unset, str]):
        first_name (Union[Unset, str]):
        groups (Union[Unset, list[str]]):
        id (Union[Unset, str]):
        roles (Union[Unset, list[str]]):
        surname (Union[Unset, str]):
        username (Union[Unset, str]):
    """

    display_name: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    groups: Union[Unset, list[str]] = UNSET
    id: Union[Unset, str] = UNSET
    roles: Union[Unset, list[str]] = UNSET
    surname: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        first_name = self.first_name

        groups: Union[Unset, list[str]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        id = self.id

        roles: Union[Unset, list[str]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles

        surname = self.surname

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if groups is not UNSET:
            field_dict["groups"] = groups
        if id is not UNSET:
            field_dict["id"] = id
        if roles is not UNSET:
            field_dict["roles"] = roles
        if surname is not UNSET:
            field_dict["surname"] = surname
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("displayName", UNSET)

        first_name = d.pop("firstName", UNSET)

        groups = cast(list[str], d.pop("groups", UNSET))

        id = d.pop("id", UNSET)

        roles = cast(list[str], d.pop("roles", UNSET))

        surname = d.pop("surname", UNSET)

        username = d.pop("username", UNSET)

        user_lookup = cls(
            display_name=display_name,
            first_name=first_name,
            groups=groups,
            id=id,
            roles=roles,
            surname=surname,
            username=username,
        )

        user_lookup.additional_properties = d
        return user_lookup

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
