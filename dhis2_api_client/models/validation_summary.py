from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_element_operand import DataElementOperand
    from ..models.validation_result import ValidationResult


T = TypeVar("T", bound="ValidationSummary")


@_attrs_define
class ValidationSummary:
    """
    Attributes:
        comment_required_violations (Union[Unset, list['DataElementOperand']]):
        validation_rule_violations (Union[Unset, list['ValidationResult']]):
    """

    comment_required_violations: Union[Unset, list["DataElementOperand"]] = UNSET
    validation_rule_violations: Union[Unset, list["ValidationResult"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment_required_violations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.comment_required_violations, Unset):
            comment_required_violations = []
            for comment_required_violations_item_data in self.comment_required_violations:
                comment_required_violations_item = comment_required_violations_item_data.to_dict()
                comment_required_violations.append(comment_required_violations_item)

        validation_rule_violations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.validation_rule_violations, Unset):
            validation_rule_violations = []
            for validation_rule_violations_item_data in self.validation_rule_violations:
                validation_rule_violations_item = validation_rule_violations_item_data.to_dict()
                validation_rule_violations.append(validation_rule_violations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment_required_violations is not UNSET:
            field_dict["commentRequiredViolations"] = comment_required_violations
        if validation_rule_violations is not UNSET:
            field_dict["validationRuleViolations"] = validation_rule_violations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.data_element_operand import DataElementOperand
        from ..models.validation_result import ValidationResult

        d = src_dict.copy()
        comment_required_violations = []
        _comment_required_violations = d.pop("commentRequiredViolations", UNSET)
        for comment_required_violations_item_data in _comment_required_violations or []:
            comment_required_violations_item = DataElementOperand.from_dict(comment_required_violations_item_data)

            comment_required_violations.append(comment_required_violations_item)

        validation_rule_violations = []
        _validation_rule_violations = d.pop("validationRuleViolations", UNSET)
        for validation_rule_violations_item_data in _validation_rule_violations or []:
            validation_rule_violations_item = ValidationResult.from_dict(validation_rule_violations_item_data)

            validation_rule_violations.append(validation_rule_violations_item)

        validation_summary = cls(
            comment_required_violations=comment_required_violations,
            validation_rule_violations=validation_rule_violations,
        )

        validation_summary.additional_properties = d
        return validation_summary

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
