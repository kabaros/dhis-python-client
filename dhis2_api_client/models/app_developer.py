from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppDeveloper")


@_attrs_define
class AppDeveloper:
    """
    Attributes:
        company (Union[Unset, str]):
        email (Union[Unset, str]):
        name (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    company: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company = self.company

        email = self.email

        name = self.name

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company is not UNSET:
            field_dict["company"] = company
        if email is not UNSET:
            field_dict["email"] = email
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        company = d.pop("company", UNSET)

        email = d.pop("email", UNSET)

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        app_developer = cls(
            company=company,
            email=email,
            name=name,
            url=url,
        )

        app_developer.additional_properties = d
        return app_developer

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
