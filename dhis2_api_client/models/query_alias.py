from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryAlias")


@_attrs_define
class QueryAlias:
    """
    Attributes:
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        path (Union[Unset, str]):
        target (Union[Unset, str]):
    """

    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    target: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        href = self.href

        id = self.id

        path = self.path

        target = self.target

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if path is not UNSET:
            field_dict["path"] = path
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        path = d.pop("path", UNSET)

        target = d.pop("target", UNSET)

        query_alias = cls(
            href=href,
            id=id,
            path=path,
            target=target,
        )

        query_alias.additional_properties = d
        return query_alias

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
