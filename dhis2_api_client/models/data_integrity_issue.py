from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataIntegrityIssue")


@_attrs_define
class DataIntegrityIssue:
    """
    Attributes:
        comment (Union[Unset, str]):
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        refs (Union[Unset, list[str]]):
    """

    comment: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    refs: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        id = self.id

        name = self.name

        refs: Union[Unset, list[str]] = UNSET
        if not isinstance(self.refs, Unset):
            refs = self.refs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if refs is not UNSET:
            field_dict["refs"] = refs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        comment = d.pop("comment", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        refs = cast(list[str], d.pop("refs", UNSET))

        data_integrity_issue = cls(
            comment=comment,
            id=id,
            name=name,
            refs=refs,
        )

        data_integrity_issue.additional_properties = d
        return data_integrity_issue

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
