from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tracker_enrollment import TrackerEnrollment
    from ..models.tracker_event import TrackerEvent
    from ..models.tracker_relationship import TrackerRelationship
    from ..models.tracker_tracked_entity import TrackerTrackedEntity


T = TypeVar("T", bound="Body")


@_attrs_define
class Body:
    """
    Attributes:
        enrollments (Union[Unset, list['TrackerEnrollment']]):
        events (Union[Unset, list['TrackerEvent']]):
        relationships (Union[Unset, list['TrackerRelationship']]):
        tracked_entities (Union[Unset, list['TrackerTrackedEntity']]):
    """

    enrollments: Union[Unset, list["TrackerEnrollment"]] = UNSET
    events: Union[Unset, list["TrackerEvent"]] = UNSET
    relationships: Union[Unset, list["TrackerRelationship"]] = UNSET
    tracked_entities: Union[Unset, list["TrackerTrackedEntity"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enrollments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.enrollments, Unset):
            enrollments = []
            for enrollments_item_data in self.enrollments:
                enrollments_item = enrollments_item_data.to_dict()
                enrollments.append(enrollments_item)

        events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        relationships: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = []
            for relationships_item_data in self.relationships:
                relationships_item = relationships_item_data.to_dict()
                relationships.append(relationships_item)

        tracked_entities: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tracked_entities, Unset):
            tracked_entities = []
            for tracked_entities_item_data in self.tracked_entities:
                tracked_entities_item = tracked_entities_item_data.to_dict()
                tracked_entities.append(tracked_entities_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enrollments is not UNSET:
            field_dict["enrollments"] = enrollments
        if events is not UNSET:
            field_dict["events"] = events
        if relationships is not UNSET:
            field_dict["relationships"] = relationships
        if tracked_entities is not UNSET:
            field_dict["trackedEntities"] = tracked_entities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tracker_enrollment import TrackerEnrollment
        from ..models.tracker_event import TrackerEvent
        from ..models.tracker_relationship import TrackerRelationship
        from ..models.tracker_tracked_entity import TrackerTrackedEntity

        d = src_dict.copy()
        enrollments = []
        _enrollments = d.pop("enrollments", UNSET)
        for enrollments_item_data in _enrollments or []:
            enrollments_item = TrackerEnrollment.from_dict(enrollments_item_data)

            enrollments.append(enrollments_item)

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = TrackerEvent.from_dict(events_item_data)

            events.append(events_item)

        relationships = []
        _relationships = d.pop("relationships", UNSET)
        for relationships_item_data in _relationships or []:
            relationships_item = TrackerRelationship.from_dict(relationships_item_data)

            relationships.append(relationships_item)

        tracked_entities = []
        _tracked_entities = d.pop("trackedEntities", UNSET)
        for tracked_entities_item_data in _tracked_entities or []:
            tracked_entities_item = TrackerTrackedEntity.from_dict(tracked_entities_item_data)

            tracked_entities.append(tracked_entities_item)

        body = cls(
            enrollments=enrollments,
            events=events,
            relationships=relationships,
            tracked_entities=tracked_entities,
        )

        body.additional_properties = d
        return body

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
