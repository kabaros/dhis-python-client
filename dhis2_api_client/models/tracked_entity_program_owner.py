from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tracked_entity_program_owner_organisation_unit import TrackedEntityProgramOwnerOrganisationUnit
    from ..models.tracked_entity_program_owner_program import TrackedEntityProgramOwnerProgram
    from ..models.tracked_entity_program_owner_tracked_entity_instance import (
        TrackedEntityProgramOwnerTrackedEntityInstance,
    )


T = TypeVar("T", bound="TrackedEntityProgramOwner")


@_attrs_define
class TrackedEntityProgramOwner:
    """
    Attributes:
        organisation_unit (Union[Unset, TrackedEntityProgramOwnerOrganisationUnit]): A UID reference to a
            OrganisationUnit
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`)
        program (Union[Unset, TrackedEntityProgramOwnerProgram]): A UID reference to a Program
            (Java name `org.hisp.dhis.program.Program`)
        tracked_entity_instance (Union[Unset, TrackedEntityProgramOwnerTrackedEntityInstance]): A UID reference to a
            TrackedEntity
            (Java name `org.hisp.dhis.trackedentity.TrackedEntity`)
    """

    organisation_unit: Union[Unset, "TrackedEntityProgramOwnerOrganisationUnit"] = UNSET
    program: Union[Unset, "TrackedEntityProgramOwnerProgram"] = UNSET
    tracked_entity_instance: Union[Unset, "TrackedEntityProgramOwnerTrackedEntityInstance"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organisation_unit: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organisation_unit, Unset):
            organisation_unit = self.organisation_unit.to_dict()

        program: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program, Unset):
            program = self.program.to_dict()

        tracked_entity_instance: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tracked_entity_instance, Unset):
            tracked_entity_instance = self.tracked_entity_instance.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organisation_unit is not UNSET:
            field_dict["organisationUnit"] = organisation_unit
        if program is not UNSET:
            field_dict["program"] = program
        if tracked_entity_instance is not UNSET:
            field_dict["trackedEntityInstance"] = tracked_entity_instance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tracked_entity_program_owner_organisation_unit import TrackedEntityProgramOwnerOrganisationUnit
        from ..models.tracked_entity_program_owner_program import TrackedEntityProgramOwnerProgram
        from ..models.tracked_entity_program_owner_tracked_entity_instance import (
            TrackedEntityProgramOwnerTrackedEntityInstance,
        )

        d = src_dict.copy()
        _organisation_unit = d.pop("organisationUnit", UNSET)
        organisation_unit: Union[Unset, TrackedEntityProgramOwnerOrganisationUnit]
        if isinstance(_organisation_unit, Unset):
            organisation_unit = UNSET
        else:
            organisation_unit = TrackedEntityProgramOwnerOrganisationUnit.from_dict(_organisation_unit)

        _program = d.pop("program", UNSET)
        program: Union[Unset, TrackedEntityProgramOwnerProgram]
        if isinstance(_program, Unset):
            program = UNSET
        else:
            program = TrackedEntityProgramOwnerProgram.from_dict(_program)

        _tracked_entity_instance = d.pop("trackedEntityInstance", UNSET)
        tracked_entity_instance: Union[Unset, TrackedEntityProgramOwnerTrackedEntityInstance]
        if isinstance(_tracked_entity_instance, Unset):
            tracked_entity_instance = UNSET
        else:
            tracked_entity_instance = TrackedEntityProgramOwnerTrackedEntityInstance.from_dict(_tracked_entity_instance)

        tracked_entity_program_owner = cls(
            organisation_unit=organisation_unit,
            program=program,
            tracked_entity_instance=tracked_entity_instance,
        )

        tracked_entity_program_owner.additional_properties = d
        return tracked_entity_program_owner

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
