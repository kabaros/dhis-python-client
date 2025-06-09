import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.deprecated_tracker_enrollment_status import DeprecatedTrackerEnrollmentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deprecated_tracker_attribute import DeprecatedTrackerAttribute
    from ..models.deprecated_tracker_enrollment_geometry import DeprecatedTrackerEnrollmentGeometry
    from ..models.deprecated_tracker_event import DeprecatedTrackerEvent
    from ..models.deprecated_tracker_note import DeprecatedTrackerNote
    from ..models.deprecated_tracker_relationship import DeprecatedTrackerRelationship
    from ..models.user_info_snapshot import UserInfoSnapshot


T = TypeVar("T", bound="DeprecatedTrackerEnrollment")


@_attrs_define
class DeprecatedTrackerEnrollment:
    """
    Attributes:
        created (str):
        created_at_client (str):
        enrollment (str):
        enrollment_date (datetime.datetime):
        incident_date (datetime.datetime):
        last_updated (str):
        last_updated_at_client (str):
        program (str):
        status (DeprecatedTrackerEnrollmentStatus):
        tracked_entity_instance (str):
        tracked_entity_type (str):
        attributes (Union[Unset, list['DeprecatedTrackerAttribute']]):
        completed_by (Union[Unset, str]):
        completed_date (Union[Unset, datetime.datetime]):
        created_by_user_info (Union[Unset, UserInfoSnapshot]):
        deleted (Union[Unset, bool]):
        events (Union[Unset, list['DeprecatedTrackerEvent']]):
        followup (Union[Unset, bool]):
        geometry (Union[Unset, DeprecatedTrackerEnrollmentGeometry]):
        last_updated_by_user_info (Union[Unset, UserInfoSnapshot]):
        notes (Union[Unset, list['DeprecatedTrackerNote']]):
        org_unit (Union[Unset, str]):
        org_unit_name (Union[Unset, str]):
        relationships (Union[Unset, list['DeprecatedTrackerRelationship']]):
        stored_by (Union[Unset, str]):
    """

    created: str
    created_at_client: str
    enrollment: str
    enrollment_date: datetime.datetime
    incident_date: datetime.datetime
    last_updated: str
    last_updated_at_client: str
    program: str
    status: DeprecatedTrackerEnrollmentStatus
    tracked_entity_instance: str
    tracked_entity_type: str
    attributes: Union[Unset, list["DeprecatedTrackerAttribute"]] = UNSET
    completed_by: Union[Unset, str] = UNSET
    completed_date: Union[Unset, datetime.datetime] = UNSET
    created_by_user_info: Union[Unset, "UserInfoSnapshot"] = UNSET
    deleted: Union[Unset, bool] = UNSET
    events: Union[Unset, list["DeprecatedTrackerEvent"]] = UNSET
    followup: Union[Unset, bool] = UNSET
    geometry: Union[Unset, "DeprecatedTrackerEnrollmentGeometry"] = UNSET
    last_updated_by_user_info: Union[Unset, "UserInfoSnapshot"] = UNSET
    notes: Union[Unset, list["DeprecatedTrackerNote"]] = UNSET
    org_unit: Union[Unset, str] = UNSET
    org_unit_name: Union[Unset, str] = UNSET
    relationships: Union[Unset, list["DeprecatedTrackerRelationship"]] = UNSET
    stored_by: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        created_at_client = self.created_at_client

        enrollment = self.enrollment

        enrollment_date = self.enrollment_date.isoformat()

        incident_date = self.incident_date.isoformat()

        last_updated = self.last_updated

        last_updated_at_client = self.last_updated_at_client

        program = self.program

        status = self.status.value

        tracked_entity_instance = self.tracked_entity_instance

        tracked_entity_type = self.tracked_entity_type

        attributes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()
                attributes.append(attributes_item)

        completed_by = self.completed_by

        completed_date: Union[Unset, str] = UNSET
        if not isinstance(self.completed_date, Unset):
            completed_date = self.completed_date.isoformat()

        created_by_user_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by_user_info, Unset):
            created_by_user_info = self.created_by_user_info.to_dict()

        deleted = self.deleted

        events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        followup = self.followup

        geometry: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.geometry, Unset):
            geometry = self.geometry.to_dict()

        last_updated_by_user_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by_user_info, Unset):
            last_updated_by_user_info = self.last_updated_by_user_info.to_dict()

        notes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.notes, Unset):
            notes = []
            for notes_item_data in self.notes:
                notes_item = notes_item_data.to_dict()
                notes.append(notes_item)

        org_unit = self.org_unit

        org_unit_name = self.org_unit_name

        relationships: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = []
            for relationships_item_data in self.relationships:
                relationships_item = relationships_item_data.to_dict()
                relationships.append(relationships_item)

        stored_by = self.stored_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "createdAtClient": created_at_client,
                "enrollment": enrollment,
                "enrollmentDate": enrollment_date,
                "incidentDate": incident_date,
                "lastUpdated": last_updated,
                "lastUpdatedAtClient": last_updated_at_client,
                "program": program,
                "status": status,
                "trackedEntityInstance": tracked_entity_instance,
                "trackedEntityType": tracked_entity_type,
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if completed_by is not UNSET:
            field_dict["completedBy"] = completed_by
        if completed_date is not UNSET:
            field_dict["completedDate"] = completed_date
        if created_by_user_info is not UNSET:
            field_dict["createdByUserInfo"] = created_by_user_info
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if events is not UNSET:
            field_dict["events"] = events
        if followup is not UNSET:
            field_dict["followup"] = followup
        if geometry is not UNSET:
            field_dict["geometry"] = geometry
        if last_updated_by_user_info is not UNSET:
            field_dict["lastUpdatedByUserInfo"] = last_updated_by_user_info
        if notes is not UNSET:
            field_dict["notes"] = notes
        if org_unit is not UNSET:
            field_dict["orgUnit"] = org_unit
        if org_unit_name is not UNSET:
            field_dict["orgUnitName"] = org_unit_name
        if relationships is not UNSET:
            field_dict["relationships"] = relationships
        if stored_by is not UNSET:
            field_dict["storedBy"] = stored_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.deprecated_tracker_attribute import DeprecatedTrackerAttribute
        from ..models.deprecated_tracker_enrollment_geometry import DeprecatedTrackerEnrollmentGeometry
        from ..models.deprecated_tracker_event import DeprecatedTrackerEvent
        from ..models.deprecated_tracker_note import DeprecatedTrackerNote
        from ..models.deprecated_tracker_relationship import DeprecatedTrackerRelationship
        from ..models.user_info_snapshot import UserInfoSnapshot

        d = src_dict.copy()
        created = d.pop("created")

        created_at_client = d.pop("createdAtClient")

        enrollment = d.pop("enrollment")

        enrollment_date = isoparse(d.pop("enrollmentDate"))

        incident_date = isoparse(d.pop("incidentDate"))

        last_updated = d.pop("lastUpdated")

        last_updated_at_client = d.pop("lastUpdatedAtClient")

        program = d.pop("program")

        status = DeprecatedTrackerEnrollmentStatus(d.pop("status"))

        tracked_entity_instance = d.pop("trackedEntityInstance")

        tracked_entity_type = d.pop("trackedEntityType")

        attributes = []
        _attributes = d.pop("attributes", UNSET)
        for attributes_item_data in _attributes or []:
            attributes_item = DeprecatedTrackerAttribute.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        completed_by = d.pop("completedBy", UNSET)

        _completed_date = d.pop("completedDate", UNSET)
        completed_date: Union[Unset, datetime.datetime]
        if isinstance(_completed_date, Unset):
            completed_date = UNSET
        else:
            completed_date = isoparse(_completed_date)

        _created_by_user_info = d.pop("createdByUserInfo", UNSET)
        created_by_user_info: Union[Unset, UserInfoSnapshot]
        if isinstance(_created_by_user_info, Unset):
            created_by_user_info = UNSET
        else:
            created_by_user_info = UserInfoSnapshot.from_dict(_created_by_user_info)

        deleted = d.pop("deleted", UNSET)

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = DeprecatedTrackerEvent.from_dict(events_item_data)

            events.append(events_item)

        followup = d.pop("followup", UNSET)

        _geometry = d.pop("geometry", UNSET)
        geometry: Union[Unset, DeprecatedTrackerEnrollmentGeometry]
        if isinstance(_geometry, Unset):
            geometry = UNSET
        else:
            geometry = DeprecatedTrackerEnrollmentGeometry.from_dict(_geometry)

        _last_updated_by_user_info = d.pop("lastUpdatedByUserInfo", UNSET)
        last_updated_by_user_info: Union[Unset, UserInfoSnapshot]
        if isinstance(_last_updated_by_user_info, Unset):
            last_updated_by_user_info = UNSET
        else:
            last_updated_by_user_info = UserInfoSnapshot.from_dict(_last_updated_by_user_info)

        notes = []
        _notes = d.pop("notes", UNSET)
        for notes_item_data in _notes or []:
            notes_item = DeprecatedTrackerNote.from_dict(notes_item_data)

            notes.append(notes_item)

        org_unit = d.pop("orgUnit", UNSET)

        org_unit_name = d.pop("orgUnitName", UNSET)

        relationships = []
        _relationships = d.pop("relationships", UNSET)
        for relationships_item_data in _relationships or []:
            relationships_item = DeprecatedTrackerRelationship.from_dict(relationships_item_data)

            relationships.append(relationships_item)

        stored_by = d.pop("storedBy", UNSET)

        deprecated_tracker_enrollment = cls(
            created=created,
            created_at_client=created_at_client,
            enrollment=enrollment,
            enrollment_date=enrollment_date,
            incident_date=incident_date,
            last_updated=last_updated,
            last_updated_at_client=last_updated_at_client,
            program=program,
            status=status,
            tracked_entity_instance=tracked_entity_instance,
            tracked_entity_type=tracked_entity_type,
            attributes=attributes,
            completed_by=completed_by,
            completed_date=completed_date,
            created_by_user_info=created_by_user_info,
            deleted=deleted,
            events=events,
            followup=followup,
            geometry=geometry,
            last_updated_by_user_info=last_updated_by_user_info,
            notes=notes,
            org_unit=org_unit,
            org_unit_name=org_unit_name,
            relationships=relationships,
            stored_by=stored_by,
        )

        deprecated_tracker_enrollment.additional_properties = d
        return deprecated_tracker_enrollment

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
