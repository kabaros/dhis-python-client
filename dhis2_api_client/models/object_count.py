from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.object_count_object_counts import ObjectCountObjectCounts


T = TypeVar("T", bound="ObjectCount")


@_attrs_define
class ObjectCount:
    """
    Attributes:
        object_counts (Union[Unset, ObjectCountObjectCounts]):
    """

    object_counts: Union[Unset, "ObjectCountObjectCounts"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_counts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.object_counts, Unset):
            object_counts = self.object_counts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_counts is not UNSET:
            field_dict["objectCounts"] = object_counts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.object_count_object_counts import ObjectCountObjectCounts

        d = src_dict.copy()
        _object_counts = d.pop("objectCounts", UNSET)
        object_counts: Union[Unset, ObjectCountObjectCounts]
        if isinstance(_object_counts, Unset):
            object_counts = UNSET
        else:
            object_counts = ObjectCountObjectCounts.from_dict(_object_counts)

        object_count = cls(
            object_counts=object_counts,
        )

        object_count.additional_properties = d
        return object_count

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
