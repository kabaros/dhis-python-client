from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.object_value_type_rendering_option_rendering_types_item import (
    ObjectValueTypeRenderingOptionRenderingTypesItem,
)
from ..models.object_value_type_rendering_option_value_type import ObjectValueTypeRenderingOptionValueType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectValueTypeRenderingOption")


@_attrs_define
class ObjectValueTypeRenderingOption:
    """
    Attributes:
        value_type (ObjectValueTypeRenderingOptionValueType):
        clazz (Union[Unset, str]):
        has_option_set (Union[Unset, bool]):
        rendering_types (Union[Unset, list[ObjectValueTypeRenderingOptionRenderingTypesItem]]):
    """

    value_type: ObjectValueTypeRenderingOptionValueType
    clazz: Union[Unset, str] = UNSET
    has_option_set: Union[Unset, bool] = UNSET
    rendering_types: Union[Unset, list[ObjectValueTypeRenderingOptionRenderingTypesItem]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value_type = self.value_type.value

        clazz = self.clazz

        has_option_set = self.has_option_set

        rendering_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.rendering_types, Unset):
            rendering_types = []
            for rendering_types_item_data in self.rendering_types:
                rendering_types_item = rendering_types_item_data.value
                rendering_types.append(rendering_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "valueType": value_type,
            }
        )
        if clazz is not UNSET:
            field_dict["clazz"] = clazz
        if has_option_set is not UNSET:
            field_dict["hasOptionSet"] = has_option_set
        if rendering_types is not UNSET:
            field_dict["renderingTypes"] = rendering_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        value_type = ObjectValueTypeRenderingOptionValueType(d.pop("valueType"))

        clazz = d.pop("clazz", UNSET)

        has_option_set = d.pop("hasOptionSet", UNSET)

        rendering_types = []
        _rendering_types = d.pop("renderingTypes", UNSET)
        for rendering_types_item_data in _rendering_types or []:
            rendering_types_item = ObjectValueTypeRenderingOptionRenderingTypesItem(rendering_types_item_data)

            rendering_types.append(rendering_types_item)

        object_value_type_rendering_option = cls(
            value_type=value_type,
            clazz=clazz,
            has_option_set=has_option_set,
            rendering_types=rendering_types,
        )

        object_value_type_rendering_option.additional_properties = d
        return object_value_type_rendering_option

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
