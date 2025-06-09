import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.tracker_relationship_item_enrollment_events_item_status import (
    TrackerRelationshipItemEnrollmentEventsItemStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tracker_data_value import TrackerDataValue
    from ..models.tracker_note import TrackerNote
    from ..models.tracker_relationship_item_enrollment_events_item_geometry import (
        TrackerRelationshipItemEnrollmentEventsItemGeometry,
    )
    from ..models.tracker_user import TrackerUser


T = TypeVar("T", bound="TrackerRelationshipItemEnrollmentEventsItem")


@_attrs_define
class TrackerRelationshipItemEnrollmentEventsItem:
    """
    Attributes:
        status (TrackerRelationshipItemEnrollmentEventsItemStatus):
        assigned_user (Union[Unset, TrackerUser]):
        attribute_category_options (Union[Unset, str]):
        attribute_option_combo (Union[Unset, str]):
        completed_at (Union[Unset, datetime.datetime, int]):
        completed_by (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime, int]):
        created_at_client (Union[Unset, datetime.datetime, int]):
        created_by (Union[Unset, TrackerUser]):
        data_values (Union[Unset, list['TrackerDataValue']]):
        deleted (Union[Unset, bool]):
        enrollment (Union[Unset, str]):
        event (Union[Unset, str]): A UID for an Event object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.RelationshipItem$Event`) Example: cc1uN0fb9Qi.
        follow_up (Union[Unset, bool]):
        followup (Union[Unset, bool]):
        geometry (Union[Unset, TrackerRelationshipItemEnrollmentEventsItemGeometry]):
        notes (Union[Unset, list['TrackerNote']]):
        occurred_at (Union[Unset, datetime.datetime, int]):
        org_unit (Union[Unset, str]):
        program (Union[Unset, str]):
        program_stage (Union[Unset, str]):
        scheduled_at (Union[Unset, datetime.datetime, int]):
        stored_by (Union[Unset, str]):
        updated_at (Union[Unset, datetime.datetime, int]):
        updated_at_client (Union[Unset, datetime.datetime, int]):
        updated_by (Union[Unset, TrackerUser]):
    """

    status: TrackerRelationshipItemEnrollmentEventsItemStatus
    assigned_user: Union[Unset, "TrackerUser"] = UNSET
    attribute_category_options: Union[Unset, str] = UNSET
    attribute_option_combo: Union[Unset, str] = UNSET
    completed_at: Union[Unset, datetime.datetime, int] = UNSET
    completed_by: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime, int] = UNSET
    created_at_client: Union[Unset, datetime.datetime, int] = UNSET
    created_by: Union[Unset, "TrackerUser"] = UNSET
    data_values: Union[Unset, list["TrackerDataValue"]] = UNSET
    deleted: Union[Unset, bool] = UNSET
    enrollment: Union[Unset, str] = UNSET
    event: Union[Unset, str] = UNSET
    follow_up: Union[Unset, bool] = UNSET
    followup: Union[Unset, bool] = UNSET
    geometry: Union[Unset, "TrackerRelationshipItemEnrollmentEventsItemGeometry"] = UNSET
    notes: Union[Unset, list["TrackerNote"]] = UNSET
    occurred_at: Union[Unset, datetime.datetime, int] = UNSET
    org_unit: Union[Unset, str] = UNSET
    program: Union[Unset, str] = UNSET
    program_stage: Union[Unset, str] = UNSET
    scheduled_at: Union[Unset, datetime.datetime, int] = UNSET
    stored_by: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime, int] = UNSET
    updated_at_client: Union[Unset, datetime.datetime, int] = UNSET
    updated_by: Union[Unset, "TrackerUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        assigned_user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.assigned_user, Unset):
            assigned_user = self.assigned_user.to_dict()

        attribute_category_options = self.attribute_category_options

        attribute_option_combo = self.attribute_option_combo

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

        data_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_values, Unset):
            data_values = []
            for data_values_item_data in self.data_values:
                data_values_item = data_values_item_data.to_dict()
                data_values.append(data_values_item)

        deleted = self.deleted

        enrollment = self.enrollment

        event = self.event

        follow_up = self.follow_up

        followup = self.followup

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

        program_stage = self.program_stage

        scheduled_at: Union[Unset, int, str]
        if isinstance(self.scheduled_at, Unset):
            scheduled_at = UNSET
        elif isinstance(self.scheduled_at, datetime.datetime):
            scheduled_at = self.scheduled_at.isoformat()
        else:
            scheduled_at = self.scheduled_at

        stored_by = self.stored_by

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
        if assigned_user is not UNSET:
            field_dict["assignedUser"] = assigned_user
        if attribute_category_options is not UNSET:
            field_dict["attributeCategoryOptions"] = attribute_category_options
        if attribute_option_combo is not UNSET:
            field_dict["attributeOptionCombo"] = attribute_option_combo
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
        if data_values is not UNSET:
            field_dict["dataValues"] = data_values
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if enrollment is not UNSET:
            field_dict["enrollment"] = enrollment
        if event is not UNSET:
            field_dict["event"] = event
        if follow_up is not UNSET:
            field_dict["followUp"] = follow_up
        if followup is not UNSET:
            field_dict["followup"] = followup
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
        if program_stage is not UNSET:
            field_dict["programStage"] = program_stage
        if scheduled_at is not UNSET:
            field_dict["scheduledAt"] = scheduled_at
        if stored_by is not UNSET:
            field_dict["storedBy"] = stored_by
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if updated_at_client is not UNSET:
            field_dict["updatedAtClient"] = updated_at_client
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tracker_data_value import TrackerDataValue
        from ..models.tracker_note import TrackerNote
        from ..models.tracker_relationship_item_enrollment_events_item_geometry import (
            TrackerRelationshipItemEnrollmentEventsItemGeometry,
        )
        from ..models.tracker_user import TrackerUser

        d = src_dict.copy()
        status = TrackerRelationshipItemEnrollmentEventsItemStatus(d.pop("status"))

        _assigned_user = d.pop("assignedUser", UNSET)
        assigned_user: Union[Unset, TrackerUser]
        if isinstance(_assigned_user, Unset):
            assigned_user = UNSET
        else:
            assigned_user = TrackerUser.from_dict(_assigned_user)

        attribute_category_options = d.pop("attributeCategoryOptions", UNSET)

        attribute_option_combo = d.pop("attributeOptionCombo", UNSET)

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

        data_values = []
        _data_values = d.pop("dataValues", UNSET)
        for data_values_item_data in _data_values or []:
            data_values_item = TrackerDataValue.from_dict(data_values_item_data)

            data_values.append(data_values_item)

        deleted = d.pop("deleted", UNSET)

        enrollment = d.pop("enrollment", UNSET)

        event = d.pop("event", UNSET)

        follow_up = d.pop("followUp", UNSET)

        followup = d.pop("followup", UNSET)

        _geometry = d.pop("geometry", UNSET)
        geometry: Union[Unset, TrackerRelationshipItemEnrollmentEventsItemGeometry]
        if isinstance(_geometry, Unset):
            geometry = UNSET
        else:
            geometry = TrackerRelationshipItemEnrollmentEventsItemGeometry.from_dict(_geometry)

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

        program_stage = d.pop("programStage", UNSET)

        def _parse_scheduled_at(data: object) -> Union[Unset, datetime.datetime, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_at_type_0 = isoparse(data)

                return scheduled_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Unset, datetime.datetime, int], data)

        scheduled_at = _parse_scheduled_at(d.pop("scheduledAt", UNSET))

        stored_by = d.pop("storedBy", UNSET)

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

        tracker_relationship_item_enrollment_events_item = cls(
            status=status,
            assigned_user=assigned_user,
            attribute_category_options=attribute_category_options,
            attribute_option_combo=attribute_option_combo,
            completed_at=completed_at,
            completed_by=completed_by,
            created_at=created_at,
            created_at_client=created_at_client,
            created_by=created_by,
            data_values=data_values,
            deleted=deleted,
            enrollment=enrollment,
            event=event,
            follow_up=follow_up,
            followup=followup,
            geometry=geometry,
            notes=notes,
            occurred_at=occurred_at,
            org_unit=org_unit,
            program=program,
            program_stage=program_stage,
            scheduled_at=scheduled_at,
            stored_by=stored_by,
            updated_at=updated_at,
            updated_at_client=updated_at_client,
            updated_by=updated_by,
        )

        tracker_relationship_item_enrollment_events_item.additional_properties = d
        return tracker_relationship_item_enrollment_events_item

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
