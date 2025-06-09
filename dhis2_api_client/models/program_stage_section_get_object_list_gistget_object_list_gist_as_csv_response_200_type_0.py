from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gist_pager import GistPager
    from ..models.program_stage_section_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_program_stage_sections_item import (
        ProgramStageSectionGetObjectListGistgetObjectListGistAsCsvResponse200Type0ProgramStageSectionsItem,
    )


T = TypeVar("T", bound="ProgramStageSectionGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class ProgramStageSectionGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        program_stage_sections (Union[Unset,
            list['ProgramStageSectionGetObjectListGistgetObjectListGistAsCsvResponse200Type0ProgramStageSectionsItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    program_stage_sections: Union[
        Unset,
        list["ProgramStageSectionGetObjectListGistgetObjectListGistAsCsvResponse200Type0ProgramStageSectionsItem"],
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        program_stage_sections: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.program_stage_sections, Unset):
            program_stage_sections = []
            for program_stage_sections_item_data in self.program_stage_sections:
                program_stage_sections_item = program_stage_sections_item_data.to_dict()
                program_stage_sections.append(program_stage_sections_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if program_stage_sections is not UNSET:
            field_dict["programStageSections"] = program_stage_sections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.gist_pager import GistPager
        from ..models.program_stage_section_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_program_stage_sections_item import (
            ProgramStageSectionGetObjectListGistgetObjectListGistAsCsvResponse200Type0ProgramStageSectionsItem,
        )

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        program_stage_sections = []
        _program_stage_sections = d.pop("programStageSections", UNSET)
        for program_stage_sections_item_data in _program_stage_sections or []:
            program_stage_sections_item = ProgramStageSectionGetObjectListGistgetObjectListGistAsCsvResponse200Type0ProgramStageSectionsItem.from_dict(
                program_stage_sections_item_data
            )

            program_stage_sections.append(program_stage_sections_item)

        program_stage_section_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            program_stage_sections=program_stage_sections,
        )

        program_stage_section_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return program_stage_section_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
