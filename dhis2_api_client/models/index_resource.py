from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndexResource")


@_attrs_define
class IndexResource:
    """
    Attributes:
        display_name (Union[Unset, str]):
        href (Union[Unset, str]):
        plural (Union[Unset, str]):
        singular (Union[Unset, str]):
    """

    display_name: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    plural: Union[Unset, str] = UNSET
    singular: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        href = self.href

        plural = self.plural

        singular = self.singular

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if href is not UNSET:
            field_dict["href"] = href
        if plural is not UNSET:
            field_dict["plural"] = plural
        if singular is not UNSET:
            field_dict["singular"] = singular

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("displayName", UNSET)

        href = d.pop("href", UNSET)

        plural = d.pop("plural", UNSET)

        singular = d.pop("singular", UNSET)

        index_resource = cls(
            display_name=display_name,
            href=href,
            plural=plural,
            singular=singular,
        )

        index_resource.additional_properties = d
        return index_resource

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
