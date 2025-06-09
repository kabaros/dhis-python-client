from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.source_params_period_types_item import SourceParamsPeriodTypesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="SourceParams")


@_attrs_define
class SourceParams:
    """
    Attributes:
        period_types (Union[Unset, list[SourceParamsPeriodTypesItem]]):
    """

    period_types: Union[Unset, list[SourceParamsPeriodTypesItem]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        period_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.period_types, Unset):
            period_types = []
            for period_types_item_data in self.period_types:
                period_types_item = period_types_item_data.value
                period_types.append(period_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if period_types is not UNSET:
            field_dict["periodTypes"] = period_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        period_types = []
        _period_types = d.pop("periodTypes", UNSET)
        for period_types_item_data in _period_types or []:
            period_types_item = SourceParamsPeriodTypesItem(period_types_item_data)

            period_types.append(period_types_item)

        source_params = cls(
            period_types=period_types,
        )

        source_params.additional_properties = d
        return source_params

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
