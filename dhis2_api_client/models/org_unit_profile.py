from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgUnitProfile")


@_attrs_define
class OrgUnitProfile:
    """
    Attributes:
        attributes (Union[Unset, list[str]]):
        data_items (Union[Unset, list[str]]):
        group_sets (Union[Unset, list[str]]):
    """

    attributes: Union[Unset, list[str]] = UNSET
    data_items: Union[Unset, list[str]] = UNSET
    group_sets: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes

        data_items: Union[Unset, list[str]] = UNSET
        if not isinstance(self.data_items, Unset):
            data_items = self.data_items

        group_sets: Union[Unset, list[str]] = UNSET
        if not isinstance(self.group_sets, Unset):
            group_sets = self.group_sets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if data_items is not UNSET:
            field_dict["dataItems"] = data_items
        if group_sets is not UNSET:
            field_dict["groupSets"] = group_sets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        attributes = cast(list[str], d.pop("attributes", UNSET))

        data_items = cast(list[str], d.pop("dataItems", UNSET))

        group_sets = cast(list[str], d.pop("groupSets", UNSET))

        org_unit_profile = cls(
            attributes=attributes,
            data_items=data_items,
            group_sets=group_sets,
        )

        org_unit_profile.additional_properties = d
        return org_unit_profile

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
