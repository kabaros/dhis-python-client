from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.series_type import SeriesType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Series")


@_attrs_define
class Series:
    """
    Attributes:
        type_ (SeriesType):
        axis (Union[Unset, int]):
        dimension_item (Union[Unset, str]):
    """

    type_: SeriesType
    axis: Union[Unset, int] = UNSET
    dimension_item: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        axis = self.axis

        dimension_item = self.dimension_item

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if axis is not UNSET:
            field_dict["axis"] = axis
        if dimension_item is not UNSET:
            field_dict["dimensionItem"] = dimension_item

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        type_ = SeriesType(d.pop("type"))

        axis = d.pop("axis", UNSET)

        dimension_item = d.pop("dimensionItem", UNSET)

        series = cls(
            type_=type_,
            axis=axis,
            dimension_item=dimension_item,
        )

        series.additional_properties = d
        return series

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
