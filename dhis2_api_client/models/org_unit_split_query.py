from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgUnitSplitQuery")


@_attrs_define
class OrgUnitSplitQuery:
    """
    Attributes:
        delete_source (Union[Unset, bool]):
        primary_target (Union[Unset, str]):
        source (Union[Unset, str]):
        targets (Union[Unset, list[str]]):
    """

    delete_source: Union[Unset, bool] = UNSET
    primary_target: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    targets: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delete_source = self.delete_source

        primary_target = self.primary_target

        source = self.source

        targets: Union[Unset, list[str]] = UNSET
        if not isinstance(self.targets, Unset):
            targets = self.targets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delete_source is not UNSET:
            field_dict["deleteSource"] = delete_source
        if primary_target is not UNSET:
            field_dict["primaryTarget"] = primary_target
        if source is not UNSET:
            field_dict["source"] = source
        if targets is not UNSET:
            field_dict["targets"] = targets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        delete_source = d.pop("deleteSource", UNSET)

        primary_target = d.pop("primaryTarget", UNSET)

        source = d.pop("source", UNSET)

        targets = cast(list[str], d.pop("targets", UNSET))

        org_unit_split_query = cls(
            delete_source=delete_source,
            primary_target=primary_target,
            source=source,
            targets=targets,
        )

        org_unit_split_query.additional_properties = d
        return org_unit_split_query

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
