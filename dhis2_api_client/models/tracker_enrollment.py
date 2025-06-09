import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.tracker_enrollment_status import TrackerEnrollmentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tracker_attribute import TrackerAttribute
    from ..models.tracker_enrollment_geometry import TrackerEnrollmentGeometry
    from ..models.tracker_event import TrackerEvent
    from ..models.tracker_note import TrackerNote
    from ..models.tracker_relationship import TrackerRelationship
    from ..models.tracker_user import TrackerUser


T = TypeVar("T", bound="TrackerEnrollment")


@_attrs_define
class TrackerEnrollment:
    """
    Attributes:
        status (TrackerEnrollmentStatus):
        attributes (Union[Unset, list['TrackerAttribute']]):
        completed_at (Union[Unset, datetime.datetime, int]):
        completed_by (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime, int]):
        created_at_client (Union[Unset, datetime.datetime, int]):
        created_by (Union[Unset, TrackerUser]):
        deleted (Union[Unset, bool]):
        enrolled_at (Union[Unset, datetime.datetime, int]):
        enrollment (Union[Unset, str]): A UID for an TrackerEnrollment object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Enrollment`) Example: h9qA2Xb1CV0.
        events (Union[Unset, list['TrackerEvent']]):
        follow_up (Union[Unset, bool]):
        geometry (Union[Unset, TrackerEnrollmentGeometry]):
        notes (Union[Unset, list['TrackerNote']]):
        occurred_at (Union[Unset, datetime.datetime, int]):
        org_unit (Union[Unset, str]):
        program (Union[Unset, str]):
        relationships (Union[Unset, list['TrackerRelationship']]):
        stored_by (Union[Unset, str]):
        tracked_entity (Union[Unset, str]): A UID for an TrackerTrackedEntity object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.TrackedEntity`) Example: zg9rM85NF00.
        updated_at (Union[Unset, datetime.datetime, int]):
        updated_at_client (Union[Unset, datetime.datetime, int]):
        updated_by (Union[Unset, TrackerUser]):
    """

    status: TrackerEnrollmentStatus
    attributes: Union[Unset, list["TrackerAttribute"]] = UNSET
    completed_at: Union[Unset, datetime.datetime, int] = UNSET
    completed_by: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime, int] = UNSET
    created_at_client: Union[Unset, datetime.datetime, int] = UNSET
    created_by: Union[Unset, "TrackerUser"] = UNSET
    deleted: Union[Unset, bool] = UNSET
    enrolled_at: Union[Unset, datetime.datetime, int] = UNSET
    enrollment: Union[Unset, str] = UNSET
    events: Union[Unset, list["TrackerEvent"]] = UNSET
    follow_up: Union[Unset, bool] = UNSET
    geometry: Union[Unset, "TrackerEnrollmentGeometry"] = UNSET
    notes: Union[Unset, list["TrackerNote"]] = UNSET
    occurred_at: Union[Unset, datetime.datetime, int] = UNSET
    org_unit: Union[Unset, str] = UNSET
    program: Union[Unset, str] = UNSET
    relationships: Union[Unset, list["TrackerRelationship"]] = UNSET
    stored_by: Union[Unset, str] = UNSET
    tracked_entity: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime, int] = UNSET
    updated_at_client: Union[Unset, datetime.datetime, int] = UNSET
    updated_by: Union[Unset, "TrackerUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        attributes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()
                attributes.append(attributes_item)

        completed_at: Union[Unset, int, str]
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        completed_by = self.completed_by

        created_at: Union[Unset, int, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        created_at_client: Union[Unset, int, str]
        if isinstance(self.created_at_client, Unset):
            created_at_client = UNSET
        elif isinstance(self.created_at_client, datetime.datetime):
            created_at_client = self.created_at_client.isoformat()
        else:
            created_at_client = self.created_at_client

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        deleted = self.deleted

        enrolled_at: Union[Unset, int, str]
        if isinstance(self.enrolled_at, Unset):
            enrolled_at = UNSET
        elif isinstance(self.enrolled_at, datetime.datetime):
            enrolled_at = self.enrolled_at.isoformat()
        else:
            enrolled_at = self.enrolled_at

        enrollment = self.enrollment

        events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        follow_up = self.follow_up

        geometry: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.geometry, Unset):
            geometry = self.geometry.to_dict()

        notes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.notes, Unset):
            notes = []
            for notes_item_data in self.notes:
                notes_item = notes_item_data.to_dict()
                notes.append(notes_item)

        occurred_at: Union[Unset, int, str]
        if isinstance(self.occurred_at, Unset):
            occurred_at = UNSET
        elif isinstance(self.occurred_at, datetime.datetime):
            occurred_at = self.occurred_at.isoformat()
        else:
            occurred_at = self.occurred_at

        org_unit = self.org_unit

        program = self.program

        relationships: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = []
            for relationships_item_data in self.relationships:
                relationships_item = relationships_item_data.to_dict()
                relationships.append(relationships_item)

        stored_by = self.stored_by

        tracked_entity = self.tracked_entity

        updated_at: Union[Unset, int, str]
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        updated_at_client: Union[Unset, int, str]
        if isinstance(self.updated_at_client, Unset):
            updated_at_client = UNSET
        elif isinstance(self.updated_at_client, datetime.datetime):
            updated_at_client = self.updated_at_client.isoformat()
        else:
            updated_at_client = self.updated_at_client

        updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.updated_by, Unset):
            updated_by = self.updated_by.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if completed_by is not UNSET:
            field_dict["completedBy"] = completed_by
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_at_client is not UNSET:
            field_dict["createdAtClient"] = created_at_client
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if enrolled_at is not UNSET:
            field_dict["enrolledAt"] = enrolled_at
        if enrollment is not UNSET:
            field_dict["enrollment"] = enrollment
        if events is not UNSET:
            field_dict["events"] = events
        if follow_up is not UNSET:
            field_dict["followUp"] = follow_up
        if geometry is not UNSET:
            field_dict["geometry"] = geometry
        if notes is not UNSET:
            field_dict["notes"] = notes
        if occurred_at is not UNSET:
            field_dict["occurredAt"] = occurred_at
        if org_unit is not UNSET:
            field_dict["orgUnit"] = org_unit
        if program is not UNSET:
            field_dict["program"] = program
        if relationships is not UNSET:
            field_dict["relationships"] = relationships
        if stored_by is not UNSET:
            field_dict["storedBy"] = stored_by
        if tracked_entity is not UNSET:
            field_dict["trackedEntity"] = tracked_entity
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if updated_at_client is not UNSET:
            field_dict["updatedAtClient"] = updated_at_client
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tracker_attribute import TrackerAttribute
        from ..models.tracker_enrollment_geometry import TrackerEnrollmentGeometry
        from ..models.tracker_event import TrackerEvent
        from ..models.tracker_note import TrackerNote
        from ..models.tracker_relationship import TrackerRelationship
        from ..models.tracker_user import TrackerUser

        d = src_dict.copy()
        status = TrackerEnrollmentStatus(d.pop("status"))

        attributes = []
        _attributes = d.pop("attributes", UNSET)
        for attributes_item_data in _attributes or []:
            attributes_item = TrackerAttribute.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        def _parse_completed_at(data: object) -> Union[Unset, datetime.datetime, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = isoparse(data)

                return completed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Unset, datetime.datetime, int], data)

        completed_at = _parse_completed_at(d.pop("completedAt", UNSET))

        completed_by = d.pop("completedBy", UNSET)

        def _parse_created_at(data: object) -> Union[Unset, datetime.datetime, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)

                return created_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Unset, datetime.datetime, int], data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))

        def _parse_created_at_client(data: object) -> Union[Unset, datetime.datetime, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_client_type_0 = isoparse(data)

                return created_at_client_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Unset, datetime.datetime, int], data)

        created_at_client = _parse_created_at_client(d.pop("createdAtClient", UNSET))

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, TrackerUser]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = TrackerUser.from_dict(_created_by)

        deleted = d.pop("deleted", UNSET)

        def _parse_enrolled_at(data: object) -> Union[Unset, datetime.datetime, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                enrolled_at_type_0 = isoparse(data)

                return enrolled_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Unset, datetime.datetime, int], data)

        enrolled_at = _parse_enrolled_at(d.pop("enrolledAt", UNSET))

        enrollment = d.pop("enrollment", UNSET)

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = TrackerEvent.from_dict(events_item_data)

            events.append(events_item)

        follow_up = d.pop("followUp", UNSET)

        _geometry = d.pop("geometry", UNSET)
        geometry: Union[Unset, TrackerEnrollmentGeometry]
        if isinstance(_geometry, Unset):
            geometry = UNSET
        else:
            geometry = TrackerEnrollmentGeometry.from_dict(_geometry)

        notes = []
        _notes = d.pop("notes", UNSET)
        for notes_item_data in _notes or []:
            notes_item = TrackerNote.from_dict(notes_item_data)

            notes.append(notes_item)

        def _parse_occurred_at(data: object) -> Union[Unset, datetime.datetime, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                occurred_at_type_0 = isoparse(data)

                return occurred_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Unset, datetime.datetime, int], data)

        occurred_at = _parse_occurred_at(d.pop("occurredAt", UNSET))

        org_unit = d.pop("orgUnit", UNSET)

        program = d.pop("program", UNSET)

        relationships = []
        _relationships = d.pop("relationships", UNSET)
        for relationships_item_data in _relationships or []:
            relationships_item = TrackerRelationship.from_dict(relationships_item_data)

            relationships.append(relationships_item)

        stored_by = d.pop("storedBy", UNSET)

        tracked_entity = d.pop("trackedEntity", UNSET)

        def _parse_updated_at(data: object) -> Union[Unset, datetime.datetime, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Unset, datetime.datetime, int], data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))

        def _parse_updated_at_client(data: object) -> Union[Unset, datetime.datetime, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_client_type_0 = isoparse(data)

                return updated_at_client_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Unset, datetime.datetime, int], data)

        updated_at_client = _parse_updated_at_client(d.pop("updatedAtClient", UNSET))

        _updated_by = d.pop("updatedBy", UNSET)
        updated_by: Union[Unset, TrackerUser]
        if isinstance(_updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = TrackerUser.from_dict(_updated_by)

        tracker_enrollment = cls(
            status=status,
            attributes=attributes,
            completed_at=completed_at,
            completed_by=completed_by,
            created_at=created_at,
            created_at_client=created_at_client,
            created_by=created_by,
            deleted=deleted,
            enrolled_at=enrolled_at,
            enrollment=enrollment,
            events=events,
            follow_up=follow_up,
            geometry=geometry,
            notes=notes,
            occurred_at=occurred_at,
            org_unit=org_unit,
            program=program,
            relationships=relationships,
            stored_by=stored_by,
            tracked_entity=tracked_entity,
            updated_at=updated_at,
            updated_at_client=updated_at_client,
            updated_by=updated_by,
        )

        tracker_enrollment.additional_properties = d
        return tracker_enrollment

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
