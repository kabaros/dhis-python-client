from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebLocale")


@_attrs_define
class WebLocale:
    """
    Attributes:
        display_name (Union[Unset, str]):
        locale (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    display_name: Union[Unset, str] = UNSET
    locale: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        locale = self.locale

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if locale is not UNSET:
            field_dict["locale"] = locale
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("displayName", UNSET)

        locale = d.pop("locale", UNSET)

        name = d.pop("name", UNSET)

        web_locale = cls(
            display_name=display_name,
            locale=locale,
            name=name,
        )

        web_locale.additional_properties = d
        return web_locale

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
