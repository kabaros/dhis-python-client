from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MergeObject")


@_attrs_define
class MergeObject:
    """
    Attributes:
        enrollments (Union[Unset, list[str]]):
        relationships (Union[Unset, list[str]]):
        tracked_entity_attributes (Union[Unset, list[str]]):
    """

    enrollments: Union[Unset, list[str]] = UNSET
    relationships: Union[Unset, list[str]] = UNSET
    tracked_entity_attributes: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enrollments: Union[Unset, list[str]] = UNSET
        if not isinstance(self.enrollments, Unset):
            enrollments = self.enrollments

        relationships: Union[Unset, list[str]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships

        tracked_entity_attributes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tracked_entity_attributes, Unset):
            tracked_entity_attributes = self.tracked_entity_attributes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enrollments is not UNSET:
            field_dict["enrollments"] = enrollments
        if relationships is not UNSET:
            field_dict["relationships"] = relationships
        if tracked_entity_attributes is not UNSET:
            field_dict["trackedEntityAttributes"] = tracked_entity_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        enrollments = cast(list[str], d.pop("enrollments", UNSET))

        relationships = cast(list[str], d.pop("relationships", UNSET))

        tracked_entity_attributes = cast(list[str], d.pop("trackedEntityAttributes", UNSET))

        merge_object = cls(
            enrollments=enrollments,
            relationships=relationships,
            tracked_entity_attributes=tracked_entity_attributes,
        )

        merge_object.additional_properties = d
        return merge_object

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
