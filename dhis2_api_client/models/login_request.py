from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoginRequest")


@_attrs_define
class LoginRequest:
    """
    Attributes:
        password (Union[Unset, str]):
        two_factor_code (Union[Unset, str]):
        username (Union[Unset, str]):
    """

    password: Union[Unset, str] = UNSET
    two_factor_code: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        password = self.password

        two_factor_code = self.two_factor_code

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if password is not UNSET:
            field_dict["password"] = password
        if two_factor_code is not UNSET:
            field_dict["twoFactorCode"] = two_factor_code
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        password = d.pop("password", UNSET)

        two_factor_code = d.pop("twoFactorCode", UNSET)

        username = d.pop("username", UNSET)

        login_request = cls(
            password=password,
            two_factor_code=two_factor_code,
            username=username,
        )

        login_request.additional_properties = d
        return login_request

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
