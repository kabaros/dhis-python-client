from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.grid_row_context_additional_property_additional_property import (
        GridRowContextAdditionalPropertyAdditionalProperty,
    )


T = TypeVar("T", bound="GridRowContextAdditionalProperty")


@_attrs_define
class GridRowContextAdditionalProperty:
    """ """

    additional_properties: dict[str, "GridRowContextAdditionalPropertyAdditionalProperty"] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.grid_row_context_additional_property_additional_property import (
            GridRowContextAdditionalPropertyAdditionalProperty,
        )

        d = src_dict.copy()
        grid_row_context_additional_property = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = GridRowContextAdditionalPropertyAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        grid_row_context_additional_property.additional_properties = additional_properties
        return grid_row_context_additional_property

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "GridRowContextAdditionalPropertyAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "GridRowContextAdditionalPropertyAdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
