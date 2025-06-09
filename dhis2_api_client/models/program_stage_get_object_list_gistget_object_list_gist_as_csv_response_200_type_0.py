from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gist_pager import GistPager
    from ..models.program_stage_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_program_stages_item import (
        ProgramStageGetObjectListGistgetObjectListGistAsCsvResponse200Type0ProgramStagesItem,
    )


T = TypeVar("T", bound="ProgramStageGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class ProgramStageGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        program_stages (Union[Unset,
            list['ProgramStageGetObjectListGistgetObjectListGistAsCsvResponse200Type0ProgramStagesItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    program_stages: Union[
        Unset, list["ProgramStageGetObjectListGistgetObjectListGistAsCsvResponse200Type0ProgramStagesItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        program_stages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.program_stages, Unset):
            program_stages = []
            for program_stages_item_data in self.program_stages:
                program_stages_item = program_stages_item_data.to_dict()
                program_stages.append(program_stages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if program_stages is not UNSET:
            field_dict["programStages"] = program_stages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.gist_pager import GistPager
        from ..models.program_stage_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_program_stages_item import (
            ProgramStageGetObjectListGistgetObjectListGistAsCsvResponse200Type0ProgramStagesItem,
        )

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        program_stages = []
        _program_stages = d.pop("programStages", UNSET)
        for program_stages_item_data in _program_stages or []:
            program_stages_item = (
                ProgramStageGetObjectListGistgetObjectListGistAsCsvResponse200Type0ProgramStagesItem.from_dict(
                    program_stages_item_data
                )
            )

            program_stages.append(program_stages_item)

        program_stage_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            program_stages=program_stages,
        )

        program_stage_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return program_stage_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
