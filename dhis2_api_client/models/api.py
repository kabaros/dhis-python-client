from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Api")


@_attrs_define
class Api:
    """
    Attributes:
        access_token (Union[Unset, str]):
        password (Union[Unset, str]):
        url (Union[Unset, str]):
        username (Union[Unset, str]):
    """

    access_token: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        password = self.password

        url = self.url

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_token is not UNSET:
            field_dict["accessToken"] = access_token
        if password is not UNSET:
            field_dict["password"] = password
        if url is not UNSET:
            field_dict["url"] = url
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        access_token = d.pop("accessToken", UNSET)

        password = d.pop("password", UNSET)

        url = d.pop("url", UNSET)

        username = d.pop("username", UNSET)

        api = cls(
            access_token=access_token,
            password=password,
            url=url,
            username=username,
        )

        api.additional_properties = d
        return api

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
