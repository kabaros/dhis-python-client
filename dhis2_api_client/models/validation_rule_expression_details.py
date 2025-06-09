from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.validation_rule_expression_details_left_side_item import ValidationRuleExpressionDetailsLeftSideItem
    from ..models.validation_rule_expression_details_right_side_item import ValidationRuleExpressionDetailsRightSideItem


T = TypeVar("T", bound="ValidationRuleExpressionDetails")


@_attrs_define
class ValidationRuleExpressionDetails:
    """
    Attributes:
        left_side (Union[Unset, list['ValidationRuleExpressionDetailsLeftSideItem']]):
        right_side (Union[Unset, list['ValidationRuleExpressionDetailsRightSideItem']]):
    """

    left_side: Union[Unset, list["ValidationRuleExpressionDetailsLeftSideItem"]] = UNSET
    right_side: Union[Unset, list["ValidationRuleExpressionDetailsRightSideItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        left_side: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.left_side, Unset):
            left_side = []
            for left_side_item_data in self.left_side:
                left_side_item = left_side_item_data.to_dict()
                left_side.append(left_side_item)

        right_side: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.right_side, Unset):
            right_side = []
            for right_side_item_data in self.right_side:
                right_side_item = right_side_item_data.to_dict()
                right_side.append(right_side_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if left_side is not UNSET:
            field_dict["leftSide"] = left_side
        if right_side is not UNSET:
            field_dict["rightSide"] = right_side

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.validation_rule_expression_details_left_side_item import (
            ValidationRuleExpressionDetailsLeftSideItem,
        )
        from ..models.validation_rule_expression_details_right_side_item import (
            ValidationRuleExpressionDetailsRightSideItem,
        )

        d = src_dict.copy()
        left_side = []
        _left_side = d.pop("leftSide", UNSET)
        for left_side_item_data in _left_side or []:
            left_side_item = ValidationRuleExpressionDetailsLeftSideItem.from_dict(left_side_item_data)

            left_side.append(left_side_item)

        right_side = []
        _right_side = d.pop("rightSide", UNSET)
        for right_side_item_data in _right_side or []:
            right_side_item = ValidationRuleExpressionDetailsRightSideItem.from_dict(right_side_item_data)

            right_side.append(right_side_item)

        validation_rule_expression_details = cls(
            left_side=left_side,
            right_side=right_side,
        )

        validation_rule_expression_details.additional_properties = d
        return validation_rule_expression_details

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
