from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ForgotPasswordRequest")


@_attrs_define
class ForgotPasswordRequest:
    """
    Attributes:
        email_or_username (Union[Unset, str]):
    """

    email_or_username: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email_or_username = self.email_or_username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email_or_username is not UNSET:
            field_dict["emailOrUsername"] = email_or_username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        email_or_username = d.pop("emailOrUsername", UNSET)

        forgot_password_request = cls(
            email_or_username=email_or_username,
        )

        forgot_password_request.additional_properties = d
        return forgot_password_request

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
