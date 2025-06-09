from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrackerProgramOwner")


@_attrs_define
class TrackerProgramOwner:
    """
    Attributes:
        org_unit (Union[Unset, str]):
        program (Union[Unset, str]):
        tracked_entity (Union[Unset, str]): A UID for an TrackerTrackedEntity object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.TrackedEntity`) Example: zg9rM85NF00.
    """

    org_unit: Union[Unset, str] = UNSET
    program: Union[Unset, str] = UNSET
    tracked_entity: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_unit = self.org_unit

        program = self.program

        tracked_entity = self.tracked_entity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if org_unit is not UNSET:
            field_dict["orgUnit"] = org_unit
        if program is not UNSET:
            field_dict["program"] = program
        if tracked_entity is not UNSET:
            field_dict["trackedEntity"] = tracked_entity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        org_unit = d.pop("orgUnit", UNSET)

        program = d.pop("program", UNSET)

        tracked_entity = d.pop("trackedEntity", UNSET)

        tracker_program_owner = cls(
            org_unit=org_unit,
            program=program,
            tracked_entity=tracked_entity,
        )

        tracker_program_owner.additional_properties = d
        return tracker_program_owner

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
