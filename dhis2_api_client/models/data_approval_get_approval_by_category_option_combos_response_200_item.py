from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.data_approval_get_approval_by_category_option_combos_response_200_item_additional_property import (
        DataApprovalGetApprovalByCategoryOptionCombosResponse200ItemAdditionalProperty,
    )


T = TypeVar("T", bound="DataApprovalGetApprovalByCategoryOptionCombosResponse200Item")


@_attrs_define
class DataApprovalGetApprovalByCategoryOptionCombosResponse200Item:
    """ """

    additional_properties: dict[
        str, "DataApprovalGetApprovalByCategoryOptionCombosResponse200ItemAdditionalProperty"
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.data_approval_get_approval_by_category_option_combos_response_200_item_additional_property import (
            DataApprovalGetApprovalByCategoryOptionCombosResponse200ItemAdditionalProperty,
        )

        d = src_dict.copy()
        data_approval_get_approval_by_category_option_combos_response_200_item = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = (
                DataApprovalGetApprovalByCategoryOptionCombosResponse200ItemAdditionalProperty.from_dict(prop_dict)
            )

            additional_properties[prop_name] = additional_property

        data_approval_get_approval_by_category_option_combos_response_200_item.additional_properties = (
            additional_properties
        )
        return data_approval_get_approval_by_category_option_combos_response_200_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "DataApprovalGetApprovalByCategoryOptionCombosResponse200ItemAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: "DataApprovalGetApprovalByCategoryOptionCombosResponse200ItemAdditionalProperty"
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
