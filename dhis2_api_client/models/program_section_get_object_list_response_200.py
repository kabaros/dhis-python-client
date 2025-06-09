from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pager import Pager
    from ..models.program_section import ProgramSection


T = TypeVar("T", bound="ProgramSectionGetObjectListResponse200")


@_attrs_define
class ProgramSectionGetObjectListResponse200:
    """
    Attributes:
        pager (Union[Unset, Pager]):
        program_sections (Union[Unset, list['ProgramSection']]):
    """

    pager: Union[Unset, "Pager"] = UNSET
    program_sections: Union[Unset, list["ProgramSection"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        program_sections: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.program_sections, Unset):
            program_sections = []
            for program_sections_item_data in self.program_sections:
                program_sections_item = program_sections_item_data.to_dict()
                program_sections.append(program_sections_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if program_sections is not UNSET:
            field_dict["programSections"] = program_sections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.pager import Pager
        from ..models.program_section import ProgramSection

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, Pager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = Pager.from_dict(_pager)

        program_sections = []
        _program_sections = d.pop("programSections", UNSET)
        for program_sections_item_data in _program_sections or []:
            program_sections_item = ProgramSection.from_dict(program_sections_item_data)

            program_sections.append(program_sections_item)

        program_section_get_object_list_response_200 = cls(
            pager=pager,
            program_sections=program_sections,
        )

        program_section_get_object_list_response_200.additional_properties = d
        return program_section_get_object_list_response_200

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
