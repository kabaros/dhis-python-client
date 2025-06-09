from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoginOidcProvider")


@_attrs_define
class LoginOidcProvider:
    """
    Attributes:
        icon (Union[Unset, str]):
        icon_padding (Union[Unset, str]):
        id (Union[Unset, str]):
        login_text (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    icon: Union[Unset, str] = UNSET
    icon_padding: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    login_text: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        icon = self.icon

        icon_padding = self.icon_padding

        id = self.id

        login_text = self.login_text

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if icon is not UNSET:
            field_dict["icon"] = icon
        if icon_padding is not UNSET:
            field_dict["iconPadding"] = icon_padding
        if id is not UNSET:
            field_dict["id"] = id
        if login_text is not UNSET:
            field_dict["loginText"] = login_text
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        icon = d.pop("icon", UNSET)

        icon_padding = d.pop("iconPadding", UNSET)

        id = d.pop("id", UNSET)

        login_text = d.pop("loginText", UNSET)

        url = d.pop("url", UNSET)

        login_oidc_provider = cls(
            icon=icon,
            icon_padding=icon_padding,
            id=id,
            login_text=login_text,
            url=url,
        )

        login_oidc_provider.additional_properties = d
        return login_oidc_provider

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
