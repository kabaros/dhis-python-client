from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.login_response_login_status import LoginResponseLoginStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="LoginResponse")


@_attrs_define
class LoginResponse:
    """
    Attributes:
        login_status (LoginResponseLoginStatus):
        redirect_url (Union[Unset, str]):
    """

    login_status: LoginResponseLoginStatus
    redirect_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        login_status = self.login_status.value

        redirect_url = self.redirect_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "loginStatus": login_status,
            }
        )
        if redirect_url is not UNSET:
            field_dict["redirectUrl"] = redirect_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        login_status = LoginResponseLoginStatus(d.pop("loginStatus"))

        redirect_url = d.pop("redirectUrl", UNSET)

        login_response = cls(
            login_status=login_status,
            redirect_url=redirect_url,
        )

        login_response.additional_properties = d
        return login_response

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
