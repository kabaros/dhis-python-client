from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResetPasswordRequest")


@_attrs_define
class ResetPasswordRequest:
    """
    Attributes:
        new_password (Union[Unset, str]):
        token (Union[Unset, str]):
    """

    new_password: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_password = self.new_password

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new_password is not UNSET:
            field_dict["newPassword"] = new_password
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        new_password = d.pop("newPassword", UNSET)

        token = d.pop("token", UNSET)

        reset_password_request = cls(
            new_password=new_password,
            token=token,
        )

        reset_password_request.additional_properties = d
        return reset_password_request

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
