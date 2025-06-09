from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.relationship_item_enrollment import RelationshipItemEnrollment
    from ..models.relationship_item_event import RelationshipItemEvent
    from ..models.relationship_item_relationship import RelationshipItemRelationship
    from ..models.relationship_item_tracked_entity import RelationshipItemTrackedEntity


T = TypeVar("T", bound="RelationshipItem")


@_attrs_define
class RelationshipItem:
    """
    Attributes:
        enrollment (Union[Unset, RelationshipItemEnrollment]): A UID reference to a Enrollment
            (Java name `org.hisp.dhis.program.Enrollment`)
        event (Union[Unset, RelationshipItemEvent]): A UID reference to a Event
            (Java name `org.hisp.dhis.program.Event`)
        relationship (Union[Unset, RelationshipItemRelationship]): A UID reference to a Relationship
            (Java name `org.hisp.dhis.relationship.Relationship`)
        tracked_entity (Union[Unset, RelationshipItemTrackedEntity]): A UID reference to a TrackedEntity
            (Java name `org.hisp.dhis.trackedentity.TrackedEntity`)
    """

    enrollment: Union[Unset, "RelationshipItemEnrollment"] = UNSET
    event: Union[Unset, "RelationshipItemEvent"] = UNSET
    relationship: Union[Unset, "RelationshipItemRelationship"] = UNSET
    tracked_entity: Union[Unset, "RelationshipItemTrackedEntity"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enrollment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.enrollment, Unset):
            enrollment = self.enrollment.to_dict()

        event: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.to_dict()

        relationship: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.relationship, Unset):
            relationship = self.relationship.to_dict()

        tracked_entity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tracked_entity, Unset):
            tracked_entity = self.tracked_entity.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enrollment is not UNSET:
            field_dict["enrollment"] = enrollment
        if event is not UNSET:
            field_dict["event"] = event
        if relationship is not UNSET:
            field_dict["relationship"] = relationship
        if tracked_entity is not UNSET:
            field_dict["trackedEntity"] = tracked_entity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.relationship_item_enrollment import RelationshipItemEnrollment
        from ..models.relationship_item_event import RelationshipItemEvent
        from ..models.relationship_item_relationship import RelationshipItemRelationship
        from ..models.relationship_item_tracked_entity import RelationshipItemTrackedEntity

        d = src_dict.copy()
        _enrollment = d.pop("enrollment", UNSET)
        enrollment: Union[Unset, RelationshipItemEnrollment]
        if isinstance(_enrollment, Unset):
            enrollment = UNSET
        else:
            enrollment = RelationshipItemEnrollment.from_dict(_enrollment)

        _event = d.pop("event", UNSET)
        event: Union[Unset, RelationshipItemEvent]
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = RelationshipItemEvent.from_dict(_event)

        _relationship = d.pop("relationship", UNSET)
        relationship: Union[Unset, RelationshipItemRelationship]
        if isinstance(_relationship, Unset):
            relationship = UNSET
        else:
            relationship = RelationshipItemRelationship.from_dict(_relationship)

        _tracked_entity = d.pop("trackedEntity", UNSET)
        tracked_entity: Union[Unset, RelationshipItemTrackedEntity]
        if isinstance(_tracked_entity, Unset):
            tracked_entity = UNSET
        else:
            tracked_entity = RelationshipItemTrackedEntity.from_dict(_tracked_entity)

        relationship_item = cls(
            enrollment=enrollment,
            event=event,
            relationship=relationship,
            tracked_entity=tracked_entity,
        )

        relationship_item.additional_properties = d
        return relationship_item

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
