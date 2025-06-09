from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserInfoSnapshot")


@_attrs_define
class UserInfoSnapshot:
    """
    Attributes:
        first_name (Union[Unset, str]):
        surname (Union[Unset, str]):
        uid (Union[Unset, str]):
        username (Union[Unset, str]):
    """

    first_name: Union[Unset, str] = UNSET
    surname: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        surname = self.surname

        uid = self.uid

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if surname is not UNSET:
            field_dict["surname"] = surname
        if uid is not UNSET:
            field_dict["uid"] = uid
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        first_name = d.pop("firstName", UNSET)

        surname = d.pop("surname", UNSET)

        uid = d.pop("uid", UNSET)

        username = d.pop("username", UNSET)

        user_info_snapshot = cls(
            first_name=first_name,
            surname=surname,
            uid=uid,
            username=username,
        )

        user_info_snapshot.additional_properties = d
        return user_info_snapshot

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
