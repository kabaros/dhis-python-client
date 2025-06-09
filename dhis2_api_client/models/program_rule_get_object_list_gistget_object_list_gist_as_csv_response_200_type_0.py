from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gist_pager import GistPager
    from ..models.program_rule_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_program_rules_item import (
        ProgramRuleGetObjectListGistgetObjectListGistAsCsvResponse200Type0ProgramRulesItem,
    )


T = TypeVar("T", bound="ProgramRuleGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class ProgramRuleGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        program_rules (Union[Unset,
            list['ProgramRuleGetObjectListGistgetObjectListGistAsCsvResponse200Type0ProgramRulesItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    program_rules: Union[
        Unset, list["ProgramRuleGetObjectListGistgetObjectListGistAsCsvResponse200Type0ProgramRulesItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        program_rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.program_rules, Unset):
            program_rules = []
            for program_rules_item_data in self.program_rules:
                program_rules_item = program_rules_item_data.to_dict()
                program_rules.append(program_rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if program_rules is not UNSET:
            field_dict["programRules"] = program_rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.gist_pager import GistPager
        from ..models.program_rule_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_program_rules_item import (
            ProgramRuleGetObjectListGistgetObjectListGistAsCsvResponse200Type0ProgramRulesItem,
        )

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        program_rules = []
        _program_rules = d.pop("programRules", UNSET)
        for program_rules_item_data in _program_rules or []:
            program_rules_item = (
                ProgramRuleGetObjectListGistgetObjectListGistAsCsvResponse200Type0ProgramRulesItem.from_dict(
                    program_rules_item_data
                )
            )

            program_rules.append(program_rules_item)

        program_rule_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            program_rules=program_rules,
        )

        program_rule_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return program_rule_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
