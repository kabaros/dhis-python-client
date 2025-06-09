from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_repetition_parent import EventRepetitionParent
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventRepetition")


@_attrs_define
class EventRepetition:
    """
    Attributes:
        parent (EventRepetitionParent):
        dimension (Union[Unset, str]):
        indexes (Union[Unset, list[int]]):
        program (Union[Unset, str]):
        program_stage (Union[Unset, str]):
    """

    parent: EventRepetitionParent
    dimension: Union[Unset, str] = UNSET
    indexes: Union[Unset, list[int]] = UNSET
    program: Union[Unset, str] = UNSET
    program_stage: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent = self.parent.value

        dimension = self.dimension

        indexes: Union[Unset, list[int]] = UNSET
        if not isinstance(self.indexes, Unset):
            indexes = self.indexes

        program = self.program

        program_stage = self.program_stage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent": parent,
            }
        )
        if dimension is not UNSET:
            field_dict["dimension"] = dimension
        if indexes is not UNSET:
            field_dict["indexes"] = indexes
        if program is not UNSET:
            field_dict["program"] = program
        if program_stage is not UNSET:
            field_dict["programStage"] = program_stage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        parent = EventRepetitionParent(d.pop("parent"))

        dimension = d.pop("dimension", UNSET)

        indexes = cast(list[int], d.pop("indexes", UNSET))

        program = d.pop("program", UNSET)

        program_stage = d.pop("programStage", UNSET)

        event_repetition = cls(
            parent=parent,
            dimension=dimension,
            indexes=indexes,
            program=program,
            program_stage=program_stage,
        )

        event_repetition.additional_properties = d
        return event_repetition

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
