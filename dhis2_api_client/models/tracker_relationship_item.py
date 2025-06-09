from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tracker_relationship_item_enrollment import TrackerRelationshipItemEnrollment
    from ..models.tracker_relationship_item_event import TrackerRelationshipItemEvent
    from ..models.tracker_relationship_item_tracked_entity import TrackerRelationshipItemTrackedEntity


T = TypeVar("T", bound="TrackerRelationshipItem")


@_attrs_define
class TrackerRelationshipItem:
    """
    Attributes:
        enrollment (Union[Unset, TrackerRelationshipItemEnrollment]):
        event (Union[Unset, TrackerRelationshipItemEvent]):
        tracked_entity (Union[Unset, TrackerRelationshipItemTrackedEntity]):
    """

    enrollment: Union[Unset, "TrackerRelationshipItemEnrollment"] = UNSET
    event: Union[Unset, "TrackerRelationshipItemEvent"] = UNSET
    tracked_entity: Union[Unset, "TrackerRelationshipItemTrackedEntity"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enrollment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.enrollment, Unset):
            enrollment = self.enrollment.to_dict()

        event: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.to_dict()

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
        if tracked_entity is not UNSET:
            field_dict["trackedEntity"] = tracked_entity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tracker_relationship_item_enrollment import TrackerRelationshipItemEnrollment
        from ..models.tracker_relationship_item_event import TrackerRelationshipItemEvent
        from ..models.tracker_relationship_item_tracked_entity import TrackerRelationshipItemTrackedEntity

        d = src_dict.copy()
        _enrollment = d.pop("enrollment", UNSET)
        enrollment: Union[Unset, TrackerRelationshipItemEnrollment]
        if isinstance(_enrollment, Unset):
            enrollment = UNSET
        else:
            enrollment = TrackerRelationshipItemEnrollment.from_dict(_enrollment)

        _event = d.pop("event", UNSET)
        event: Union[Unset, TrackerRelationshipItemEvent]
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = TrackerRelationshipItemEvent.from_dict(_event)

        _tracked_entity = d.pop("trackedEntity", UNSET)
        tracked_entity: Union[Unset, TrackerRelationshipItemTrackedEntity]
        if isinstance(_tracked_entity, Unset):
            tracked_entity = UNSET
        else:
            tracked_entity = TrackerRelationshipItemTrackedEntity.from_dict(_tracked_entity)

        tracker_relationship_item = cls(
            enrollment=enrollment,
            event=event,
            tracked_entity=tracked_entity,
        )

        tracker_relationship_item.additional_properties = d
        return tracker_relationship_item

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
