from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserRegistrationParams")


@_attrs_define
class UserRegistrationParams:
    """
    Attributes:
        email (Union[Unset, str]):
        first_name (Union[Unset, str]):
        g_recaptcha_response (Union[Unset, str]):
        password (Union[Unset, str]):
        surname (Union[Unset, str]):
        username (Union[Unset, str]):
    """

    email: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    g_recaptcha_response: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    surname: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        first_name = self.first_name

        g_recaptcha_response = self.g_recaptcha_response

        password = self.password

        surname = self.surname

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if g_recaptcha_response is not UNSET:
            field_dict["g-recaptcha-response"] = g_recaptcha_response
        if password is not UNSET:
            field_dict["password"] = password
        if surname is not UNSET:
            field_dict["surname"] = surname
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email", UNSET)

        first_name = d.pop("firstName", UNSET)

        g_recaptcha_response = d.pop("g-recaptcha-response", UNSET)

        password = d.pop("password", UNSET)

        surname = d.pop("surname", UNSET)

        username = d.pop("username", UNSET)

        user_registration_params = cls(
            email=email,
            first_name=first_name,
            g_recaptcha_response=g_recaptcha_response,
            password=password,
            surname=surname,
            username=username,
        )

        user_registration_params.additional_properties = d
        return user_registration_params

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
