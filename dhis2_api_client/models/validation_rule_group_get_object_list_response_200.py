from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pager import Pager
    from ..models.validation_rule_group import ValidationRuleGroup


T = TypeVar("T", bound="ValidationRuleGroupGetObjectListResponse200")


@_attrs_define
class ValidationRuleGroupGetObjectListResponse200:
    """
    Attributes:
        pager (Union[Unset, Pager]):
        validation_rule_groups (Union[Unset, list['ValidationRuleGroup']]):
    """

    pager: Union[Unset, "Pager"] = UNSET
    validation_rule_groups: Union[Unset, list["ValidationRuleGroup"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        validation_rule_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.validation_rule_groups, Unset):
            validation_rule_groups = []
            for validation_rule_groups_item_data in self.validation_rule_groups:
                validation_rule_groups_item = validation_rule_groups_item_data.to_dict()
                validation_rule_groups.append(validation_rule_groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if validation_rule_groups is not UNSET:
            field_dict["validationRuleGroups"] = validation_rule_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.pager import Pager
        from ..models.validation_rule_group import ValidationRuleGroup

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, Pager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = Pager.from_dict(_pager)

        validation_rule_groups = []
        _validation_rule_groups = d.pop("validationRuleGroups", UNSET)
        for validation_rule_groups_item_data in _validation_rule_groups or []:
            validation_rule_groups_item = ValidationRuleGroup.from_dict(validation_rule_groups_item_data)

            validation_rule_groups.append(validation_rule_groups_item)

        validation_rule_group_get_object_list_response_200 = cls(
            pager=pager,
            validation_rule_groups=validation_rule_groups,
        )

        validation_rule_group_get_object_list_response_200.additional_properties = d
        return validation_rule_group_get_object_list_response_200

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
