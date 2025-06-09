from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.simple_dimension_parent import SimpleDimensionParent
from ..types import UNSET, Unset

T = TypeVar("T", bound="SimpleDimension")


@_attrs_define
class SimpleDimension:
    """
    Attributes:
        parent (SimpleDimensionParent):
        dimension (Union[Unset, str]):
        program (Union[Unset, str]):
        program_stage (Union[Unset, str]):
        values (Union[Unset, list[str]]):
    """

    parent: SimpleDimensionParent
    dimension: Union[Unset, str] = UNSET
    program: Union[Unset, str] = UNSET
    program_stage: Union[Unset, str] = UNSET
    values: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent = self.parent.value

        dimension = self.dimension

        program = self.program

        program_stage = self.program_stage

        values: Union[Unset, list[str]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent": parent,
            }
        )
        if dimension is not UNSET:
            field_dict["dimension"] = dimension
        if program is not UNSET:
            field_dict["program"] = program
        if program_stage is not UNSET:
            field_dict["programStage"] = program_stage
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        parent = SimpleDimensionParent(d.pop("parent"))

        dimension = d.pop("dimension", UNSET)

        program = d.pop("program", UNSET)

        program_stage = d.pop("programStage", UNSET)

        values = cast(list[str], d.pop("values", UNSET))

        simple_dimension = cls(
            parent=parent,
            dimension=dimension,
            program=program,
            program_stage=program_stage,
            values=values,
        )

        simple_dimension.additional_properties = d
        return simple_dimension

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
