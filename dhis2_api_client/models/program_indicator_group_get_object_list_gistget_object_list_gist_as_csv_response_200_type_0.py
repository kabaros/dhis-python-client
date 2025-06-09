from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gist_pager import GistPager
    from ..models.program_indicator_group_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_program_indicator_groups_item import (
        ProgramIndicatorGroupGetObjectListGistgetObjectListGistAsCsvResponse200Type0ProgramIndicatorGroupsItem,
    )


T = TypeVar("T", bound="ProgramIndicatorGroupGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class ProgramIndicatorGroupGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        program_indicator_groups (Union[Unset, list['ProgramIndicatorGroupGetObjectListGistgetObjectListGistAsCsvRespons
            e200Type0ProgramIndicatorGroupsItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    program_indicator_groups: Union[
        Unset,
        list["ProgramIndicatorGroupGetObjectListGistgetObjectListGistAsCsvResponse200Type0ProgramIndicatorGroupsItem"],
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        program_indicator_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.program_indicator_groups, Unset):
            program_indicator_groups = []
            for program_indicator_groups_item_data in self.program_indicator_groups:
                program_indicator_groups_item = program_indicator_groups_item_data.to_dict()
                program_indicator_groups.append(program_indicator_groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if program_indicator_groups is not UNSET:
            field_dict["programIndicatorGroups"] = program_indicator_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.gist_pager import GistPager
        from ..models.program_indicator_group_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_program_indicator_groups_item import (
            ProgramIndicatorGroupGetObjectListGistgetObjectListGistAsCsvResponse200Type0ProgramIndicatorGroupsItem,
        )

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        program_indicator_groups = []
        _program_indicator_groups = d.pop("programIndicatorGroups", UNSET)
        for program_indicator_groups_item_data in _program_indicator_groups or []:
            program_indicator_groups_item = ProgramIndicatorGroupGetObjectListGistgetObjectListGistAsCsvResponse200Type0ProgramIndicatorGroupsItem.from_dict(
                program_indicator_groups_item_data
            )

            program_indicator_groups.append(program_indicator_groups_item)

        program_indicator_group_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            program_indicator_groups=program_indicator_groups,
        )

        program_indicator_group_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return program_indicator_group_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
