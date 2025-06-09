from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FollowupParams")


@_attrs_define
class FollowupParams:
    """
    Attributes:
        attribute_option_combo_id (int):
        category_option_combo_id (int):
        data_element_id (int):
        organisation_unit_id (int):
        period_id (int):
        followup (Union[Unset, bool]):
    """

    attribute_option_combo_id: int
    category_option_combo_id: int
    data_element_id: int
    organisation_unit_id: int
    period_id: int
    followup: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribute_option_combo_id = self.attribute_option_combo_id

        category_option_combo_id = self.category_option_combo_id

        data_element_id = self.data_element_id

        organisation_unit_id = self.organisation_unit_id

        period_id = self.period_id

        followup = self.followup

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributeOptionComboId": attribute_option_combo_id,
                "categoryOptionComboId": category_option_combo_id,
                "dataElementId": data_element_id,
                "organisationUnitId": organisation_unit_id,
                "periodId": period_id,
            }
        )
        if followup is not UNSET:
            field_dict["followup"] = followup

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        attribute_option_combo_id = d.pop("attributeOptionComboId")

        category_option_combo_id = d.pop("categoryOptionComboId")

        data_element_id = d.pop("dataElementId")

        organisation_unit_id = d.pop("organisationUnitId")

        period_id = d.pop("periodId")

        followup = d.pop("followup", UNSET)

        followup_params = cls(
            attribute_option_combo_id=attribute_option_combo_id,
            category_option_combo_id=category_option_combo_id,
            data_element_id=data_element_id,
            organisation_unit_id=organisation_unit_id,
            period_id=period_id,
            followup=followup,
        )

        followup_params.additional_properties = d
        return followup_params

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
