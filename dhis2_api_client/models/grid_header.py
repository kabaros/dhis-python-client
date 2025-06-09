from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.grid_header_value_type import GridHeaderValueType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GridHeader")


@_attrs_define
class GridHeader:
    """
    Attributes:
        value_type (GridHeaderValueType):
        column (Union[Unset, str]):
        hidden (Union[Unset, bool]):
        legend_set (Union[Unset, str]):
        meta (Union[Unset, bool]):
        name (Union[Unset, str]):
        option_set (Union[Unset, str]):
        program_stage (Union[Unset, str]):
        repeatable_stage_params (Union[Unset, str]):
        stage_offset (Union[Unset, int]):
        type_ (Union[Unset, str]):
    """

    value_type: GridHeaderValueType
    column: Union[Unset, str] = UNSET
    hidden: Union[Unset, bool] = UNSET
    legend_set: Union[Unset, str] = UNSET
    meta: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    option_set: Union[Unset, str] = UNSET
    program_stage: Union[Unset, str] = UNSET
    repeatable_stage_params: Union[Unset, str] = UNSET
    stage_offset: Union[Unset, int] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value_type = self.value_type.value

        column = self.column

        hidden = self.hidden

        legend_set = self.legend_set

        meta = self.meta

        name = self.name

        option_set = self.option_set

        program_stage = self.program_stage

        repeatable_stage_params = self.repeatable_stage_params

        stage_offset = self.stage_offset

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "valueType": value_type,
            }
        )
        if column is not UNSET:
            field_dict["column"] = column
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if legend_set is not UNSET:
            field_dict["legendSet"] = legend_set
        if meta is not UNSET:
            field_dict["meta"] = meta
        if name is not UNSET:
            field_dict["name"] = name
        if option_set is not UNSET:
            field_dict["optionSet"] = option_set
        if program_stage is not UNSET:
            field_dict["programStage"] = program_stage
        if repeatable_stage_params is not UNSET:
            field_dict["repeatableStageParams"] = repeatable_stage_params
        if stage_offset is not UNSET:
            field_dict["stageOffset"] = stage_offset
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        value_type = GridHeaderValueType(d.pop("valueType"))

        column = d.pop("column", UNSET)

        hidden = d.pop("hidden", UNSET)

        legend_set = d.pop("legendSet", UNSET)

        meta = d.pop("meta", UNSET)

        name = d.pop("name", UNSET)

        option_set = d.pop("optionSet", UNSET)

        program_stage = d.pop("programStage", UNSET)

        repeatable_stage_params = d.pop("repeatableStageParams", UNSET)

        stage_offset = d.pop("stageOffset", UNSET)

        type_ = d.pop("type", UNSET)

        grid_header = cls(
            value_type=value_type,
            column=column,
            hidden=hidden,
            legend_set=legend_set,
            meta=meta,
            name=name,
            option_set=option_set,
            program_stage=program_stage,
            repeatable_stage_params=repeatable_stage_params,
            stage_offset=stage_offset,
            type_=type_,
        )

        grid_header.additional_properties = d
        return grid_header

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
