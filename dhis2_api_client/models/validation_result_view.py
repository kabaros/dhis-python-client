from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidationResultView")


@_attrs_define
class ValidationResultView:
    """
    Attributes:
        attribute_option_combo_display_name (Union[Unset, str]):
        attribute_option_combo_id (Union[Unset, str]):
        importance (Union[Unset, str]):
        left_side_value (Union[Unset, float]):
        operator (Union[Unset, str]):
        organisation_unit_ancestor_names (Union[Unset, str]):
        organisation_unit_display_name (Union[Unset, str]):
        organisation_unit_id (Union[Unset, str]):
        organisation_unit_path (Union[Unset, str]):
        period_display_name (Union[Unset, str]):
        period_id (Union[Unset, str]):
        right_side_value (Union[Unset, float]):
        validation_rule_description (Union[Unset, str]):
        validation_rule_id (Union[Unset, str]):
    """

    attribute_option_combo_display_name: Union[Unset, str] = UNSET
    attribute_option_combo_id: Union[Unset, str] = UNSET
    importance: Union[Unset, str] = UNSET
    left_side_value: Union[Unset, float] = UNSET
    operator: Union[Unset, str] = UNSET
    organisation_unit_ancestor_names: Union[Unset, str] = UNSET
    organisation_unit_display_name: Union[Unset, str] = UNSET
    organisation_unit_id: Union[Unset, str] = UNSET
    organisation_unit_path: Union[Unset, str] = UNSET
    period_display_name: Union[Unset, str] = UNSET
    period_id: Union[Unset, str] = UNSET
    right_side_value: Union[Unset, float] = UNSET
    validation_rule_description: Union[Unset, str] = UNSET
    validation_rule_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribute_option_combo_display_name = self.attribute_option_combo_display_name

        attribute_option_combo_id = self.attribute_option_combo_id

        importance = self.importance

        left_side_value = self.left_side_value

        operator = self.operator

        organisation_unit_ancestor_names = self.organisation_unit_ancestor_names

        organisation_unit_display_name = self.organisation_unit_display_name

        organisation_unit_id = self.organisation_unit_id

        organisation_unit_path = self.organisation_unit_path

        period_display_name = self.period_display_name

        period_id = self.period_id

        right_side_value = self.right_side_value

        validation_rule_description = self.validation_rule_description

        validation_rule_id = self.validation_rule_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attribute_option_combo_display_name is not UNSET:
            field_dict["attributeOptionComboDisplayName"] = attribute_option_combo_display_name
        if attribute_option_combo_id is not UNSET:
            field_dict["attributeOptionComboId"] = attribute_option_combo_id
        if importance is not UNSET:
            field_dict["importance"] = importance
        if left_side_value is not UNSET:
            field_dict["leftSideValue"] = left_side_value
        if operator is not UNSET:
            field_dict["operator"] = operator
        if organisation_unit_ancestor_names is not UNSET:
            field_dict["organisationUnitAncestorNames"] = organisation_unit_ancestor_names
        if organisation_unit_display_name is not UNSET:
            field_dict["organisationUnitDisplayName"] = organisation_unit_display_name
        if organisation_unit_id is not UNSET:
            field_dict["organisationUnitId"] = organisation_unit_id
        if organisation_unit_path is not UNSET:
            field_dict["organisationUnitPath"] = organisation_unit_path
        if period_display_name is not UNSET:
            field_dict["periodDisplayName"] = period_display_name
        if period_id is not UNSET:
            field_dict["periodId"] = period_id
        if right_side_value is not UNSET:
            field_dict["rightSideValue"] = right_side_value
        if validation_rule_description is not UNSET:
            field_dict["validationRuleDescription"] = validation_rule_description
        if validation_rule_id is not UNSET:
            field_dict["validationRuleId"] = validation_rule_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        attribute_option_combo_display_name = d.pop("attributeOptionComboDisplayName", UNSET)

        attribute_option_combo_id = d.pop("attributeOptionComboId", UNSET)

        importance = d.pop("importance", UNSET)

        left_side_value = d.pop("leftSideValue", UNSET)

        operator = d.pop("operator", UNSET)

        organisation_unit_ancestor_names = d.pop("organisationUnitAncestorNames", UNSET)

        organisation_unit_display_name = d.pop("organisationUnitDisplayName", UNSET)

        organisation_unit_id = d.pop("organisationUnitId", UNSET)

        organisation_unit_path = d.pop("organisationUnitPath", UNSET)

        period_display_name = d.pop("periodDisplayName", UNSET)

        period_id = d.pop("periodId", UNSET)

        right_side_value = d.pop("rightSideValue", UNSET)

        validation_rule_description = d.pop("validationRuleDescription", UNSET)

        validation_rule_id = d.pop("validationRuleId", UNSET)

        validation_result_view = cls(
            attribute_option_combo_display_name=attribute_option_combo_display_name,
            attribute_option_combo_id=attribute_option_combo_id,
            importance=importance,
            left_side_value=left_side_value,
            operator=operator,
            organisation_unit_ancestor_names=organisation_unit_ancestor_names,
            organisation_unit_display_name=organisation_unit_display_name,
            organisation_unit_id=organisation_unit_id,
            organisation_unit_path=organisation_unit_path,
            period_display_name=period_display_name,
            period_id=period_id,
            right_side_value=right_side_value,
            validation_rule_description=validation_rule_description,
            validation_rule_id=validation_rule_id,
        )

        validation_result_view.additional_properties = d
        return validation_result_view

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
