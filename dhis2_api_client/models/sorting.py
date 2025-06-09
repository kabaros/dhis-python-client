from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sorting_direction import SortingDirection

T = TypeVar("T", bound="Sorting")


@_attrs_define
class Sorting:
    """
    Attributes:
        dimension (str):
        direction (SortingDirection):
    """

    dimension: str
    direction: SortingDirection
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dimension = self.dimension

        direction = self.direction.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dimension": dimension,
                "direction": direction,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        dimension = d.pop("dimension")

        direction = SortingDirection(d.pop("direction"))

        sorting = cls(
            dimension=dimension,
            direction=direction,
        )

        sorting.additional_properties = d
        return sorting

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
