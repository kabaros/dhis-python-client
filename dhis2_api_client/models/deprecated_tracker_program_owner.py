from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeprecatedTrackerProgramOwner")


@_attrs_define
class DeprecatedTrackerProgramOwner:
    """
    Attributes:
        owner_org_unit (Union[Unset, str]):
        program (Union[Unset, str]):
        tracked_entity_instance (Union[Unset, str]):
    """

    owner_org_unit: Union[Unset, str] = UNSET
    program: Union[Unset, str] = UNSET
    tracked_entity_instance: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        owner_org_unit = self.owner_org_unit

        program = self.program

        tracked_entity_instance = self.tracked_entity_instance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if owner_org_unit is not UNSET:
            field_dict["ownerOrgUnit"] = owner_org_unit
        if program is not UNSET:
            field_dict["program"] = program
        if tracked_entity_instance is not UNSET:
            field_dict["trackedEntityInstance"] = tracked_entity_instance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        owner_org_unit = d.pop("ownerOrgUnit", UNSET)

        program = d.pop("program", UNSET)

        tracked_entity_instance = d.pop("trackedEntityInstance", UNSET)

        deprecated_tracker_program_owner = cls(
            owner_org_unit=owner_org_unit,
            program=program,
            tracked_entity_instance=tracked_entity_instance,
        )

        deprecated_tracker_program_owner.additional_properties = d
        return deprecated_tracker_program_owner

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
