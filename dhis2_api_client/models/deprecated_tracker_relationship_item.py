from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deprecated_tracker_enrollment import DeprecatedTrackerEnrollment
    from ..models.deprecated_tracker_event import DeprecatedTrackerEvent
    from ..models.deprecated_tracker_tracked_entity_instance import DeprecatedTrackerTrackedEntityInstance


T = TypeVar("T", bound="DeprecatedTrackerRelationshipItem")


@_attrs_define
class DeprecatedTrackerRelationshipItem:
    """
    Attributes:
        enrollment (Union[Unset, DeprecatedTrackerEnrollment]):
        event (Union[Unset, DeprecatedTrackerEvent]):
        tracked_entity_instance (Union[Unset, DeprecatedTrackerTrackedEntityInstance]):
    """

    enrollment: Union[Unset, "DeprecatedTrackerEnrollment"] = UNSET
    event: Union[Unset, "DeprecatedTrackerEvent"] = UNSET
    tracked_entity_instance: Union[Unset, "DeprecatedTrackerTrackedEntityInstance"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enrollment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.enrollment, Unset):
            enrollment = self.enrollment.to_dict()

        event: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.to_dict()

        tracked_entity_instance: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tracked_entity_instance, Unset):
            tracked_entity_instance = self.tracked_entity_instance.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enrollment is not UNSET:
            field_dict["enrollment"] = enrollment
        if event is not UNSET:
            field_dict["event"] = event
        if tracked_entity_instance is not UNSET:
            field_dict["trackedEntityInstance"] = tracked_entity_instance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.deprecated_tracker_enrollment import DeprecatedTrackerEnrollment
        from ..models.deprecated_tracker_event import DeprecatedTrackerEvent
        from ..models.deprecated_tracker_tracked_entity_instance import DeprecatedTrackerTrackedEntityInstance

        d = src_dict.copy()
        _enrollment = d.pop("enrollment", UNSET)
        enrollment: Union[Unset, DeprecatedTrackerEnrollment]
        if isinstance(_enrollment, Unset):
            enrollment = UNSET
        else:
            enrollment = DeprecatedTrackerEnrollment.from_dict(_enrollment)

        _event = d.pop("event", UNSET)
        event: Union[Unset, DeprecatedTrackerEvent]
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = DeprecatedTrackerEvent.from_dict(_event)

        _tracked_entity_instance = d.pop("trackedEntityInstance", UNSET)
        tracked_entity_instance: Union[Unset, DeprecatedTrackerTrackedEntityInstance]
        if isinstance(_tracked_entity_instance, Unset):
            tracked_entity_instance = UNSET
        else:
            tracked_entity_instance = DeprecatedTrackerTrackedEntityInstance.from_dict(_tracked_entity_instance)

        deprecated_tracker_relationship_item = cls(
            enrollment=enrollment,
            event=event,
            tracked_entity_instance=tracked_entity_instance,
        )

        deprecated_tracker_relationship_item.additional_properties = d
        return deprecated_tracker_relationship_item

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
