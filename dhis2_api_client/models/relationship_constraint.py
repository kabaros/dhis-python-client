from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.relationship_constraint_relationship_entity import RelationshipConstraintRelationshipEntity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.relationship_constraint_program import RelationshipConstraintProgram
    from ..models.relationship_constraint_program_stage import RelationshipConstraintProgramStage
    from ..models.relationship_constraint_tracked_entity_type import RelationshipConstraintTrackedEntityType
    from ..models.tracker_data_view import TrackerDataView


T = TypeVar("T", bound="RelationshipConstraint")


@_attrs_define
class RelationshipConstraint:
    """
    Attributes:
        relationship_entity (RelationshipConstraintRelationshipEntity):
        program (Union[Unset, RelationshipConstraintProgram]): A UID reference to a Program
            (Java name `org.hisp.dhis.program.Program`)
        program_stage (Union[Unset, RelationshipConstraintProgramStage]): A UID reference to a ProgramStage
            (Java name `org.hisp.dhis.program.ProgramStage`)
        tracked_entity_type (Union[Unset, RelationshipConstraintTrackedEntityType]): A UID reference to a
            TrackedEntityType
            (Java name `org.hisp.dhis.trackedentity.TrackedEntityType`)
        tracker_data_view (Union[Unset, TrackerDataView]):
    """

    relationship_entity: RelationshipConstraintRelationshipEntity
    program: Union[Unset, "RelationshipConstraintProgram"] = UNSET
    program_stage: Union[Unset, "RelationshipConstraintProgramStage"] = UNSET
    tracked_entity_type: Union[Unset, "RelationshipConstraintTrackedEntityType"] = UNSET
    tracker_data_view: Union[Unset, "TrackerDataView"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        relationship_entity = self.relationship_entity.value

        program: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program, Unset):
            program = self.program.to_dict()

        program_stage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program_stage, Unset):
            program_stage = self.program_stage.to_dict()

        tracked_entity_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tracked_entity_type, Unset):
            tracked_entity_type = self.tracked_entity_type.to_dict()

        tracker_data_view: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tracker_data_view, Unset):
            tracker_data_view = self.tracker_data_view.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "relationshipEntity": relationship_entity,
            }
        )
        if program is not UNSET:
            field_dict["program"] = program
        if program_stage is not UNSET:
            field_dict["programStage"] = program_stage
        if tracked_entity_type is not UNSET:
            field_dict["trackedEntityType"] = tracked_entity_type
        if tracker_data_view is not UNSET:
            field_dict["trackerDataView"] = tracker_data_view

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.relationship_constraint_program import RelationshipConstraintProgram
        from ..models.relationship_constraint_program_stage import RelationshipConstraintProgramStage
        from ..models.relationship_constraint_tracked_entity_type import RelationshipConstraintTrackedEntityType
        from ..models.tracker_data_view import TrackerDataView

        d = src_dict.copy()
        relationship_entity = RelationshipConstraintRelationshipEntity(d.pop("relationshipEntity"))

        _program = d.pop("program", UNSET)
        program: Union[Unset, RelationshipConstraintProgram]
        if isinstance(_program, Unset):
            program = UNSET
        else:
            program = RelationshipConstraintProgram.from_dict(_program)

        _program_stage = d.pop("programStage", UNSET)
        program_stage: Union[Unset, RelationshipConstraintProgramStage]
        if isinstance(_program_stage, Unset):
            program_stage = UNSET
        else:
            program_stage = RelationshipConstraintProgramStage.from_dict(_program_stage)

        _tracked_entity_type = d.pop("trackedEntityType", UNSET)
        tracked_entity_type: Union[Unset, RelationshipConstraintTrackedEntityType]
        if isinstance(_tracked_entity_type, Unset):
            tracked_entity_type = UNSET
        else:
            tracked_entity_type = RelationshipConstraintTrackedEntityType.from_dict(_tracked_entity_type)

        _tracker_data_view = d.pop("trackerDataView", UNSET)
        tracker_data_view: Union[Unset, TrackerDataView]
        if isinstance(_tracker_data_view, Unset):
            tracker_data_view = UNSET
        else:
            tracker_data_view = TrackerDataView.from_dict(_tracker_data_view)

        relationship_constraint = cls(
            relationship_entity=relationship_entity,
            program=program,
            program_stage=program_stage,
            tracked_entity_type=tracked_entity_type,
            tracker_data_view=tracker_data_view,
        )

        relationship_constraint.additional_properties = d
        return relationship_constraint

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
