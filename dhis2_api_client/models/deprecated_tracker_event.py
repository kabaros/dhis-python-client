from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deprecated_tracker_event_enrollment_status import DeprecatedTrackerEventEnrollmentStatus
from ..models.deprecated_tracker_event_program_type import DeprecatedTrackerEventProgramType
from ..models.deprecated_tracker_event_status import DeprecatedTrackerEventStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deprecated_tracker_data_value import DeprecatedTrackerDataValue
    from ..models.deprecated_tracker_event_geometry import DeprecatedTrackerEventGeometry
    from ..models.deprecated_tracker_note import DeprecatedTrackerNote
    from ..models.deprecated_tracker_relationship import DeprecatedTrackerRelationship
    from ..models.user_info_snapshot import UserInfoSnapshot


T = TypeVar("T", bound="DeprecatedTrackerEvent")


@_attrs_define
class DeprecatedTrackerEvent:
    """
    Attributes:
        created_at_client (str):
        enrollment (str):
        enrollment_status (DeprecatedTrackerEventEnrollmentStatus):
        event (str):
        event_date (str):
        last_updated_at_client (str):
        program (str):
        program_stage (str):
        program_type (DeprecatedTrackerEventProgramType):
        status (DeprecatedTrackerEventStatus):
        assigned_user (Union[Unset, str]):
        assigned_user_display_name (Union[Unset, str]):
        assigned_user_first_name (Union[Unset, str]):
        assigned_user_surname (Union[Unset, str]):
        assigned_user_username (Union[Unset, str]):
        attribute_category_options (Union[Unset, str]):
        attribute_option_combo (Union[Unset, str]):
        completed_by (Union[Unset, str]):
        completed_date (Union[Unset, str]):
        created (Union[Unset, str]):
        created_by_user_info (Union[Unset, UserInfoSnapshot]):
        data_values (Union[Unset, list['DeprecatedTrackerDataValue']]):
        deleted (Union[Unset, bool]):
        due_date (Union[Unset, str]):
        followup (Union[Unset, bool]):
        geometry (Union[Unset, DeprecatedTrackerEventGeometry]):
        href (Union[Unset, str]):
        last_updated (Union[Unset, str]):
        last_updated_by_user_info (Union[Unset, UserInfoSnapshot]):
        notes (Union[Unset, list['DeprecatedTrackerNote']]):
        org_unit (Union[Unset, str]):
        org_unit_name (Union[Unset, str]):
        relationships (Union[Unset, list['DeprecatedTrackerRelationship']]):
        stored_by (Union[Unset, str]):
        tracked_entity_instance (Union[Unset, str]):
    """

    created_at_client: str
    enrollment: str
    enrollment_status: DeprecatedTrackerEventEnrollmentStatus
    event: str
    event_date: str
    last_updated_at_client: str
    program: str
    program_stage: str
    program_type: DeprecatedTrackerEventProgramType
    status: DeprecatedTrackerEventStatus
    assigned_user: Union[Unset, str] = UNSET
    assigned_user_display_name: Union[Unset, str] = UNSET
    assigned_user_first_name: Union[Unset, str] = UNSET
    assigned_user_surname: Union[Unset, str] = UNSET
    assigned_user_username: Union[Unset, str] = UNSET
    attribute_category_options: Union[Unset, str] = UNSET
    attribute_option_combo: Union[Unset, str] = UNSET
    completed_by: Union[Unset, str] = UNSET
    completed_date: Union[Unset, str] = UNSET
    created: Union[Unset, str] = UNSET
    created_by_user_info: Union[Unset, "UserInfoSnapshot"] = UNSET
    data_values: Union[Unset, list["DeprecatedTrackerDataValue"]] = UNSET
    deleted: Union[Unset, bool] = UNSET
    due_date: Union[Unset, str] = UNSET
    followup: Union[Unset, bool] = UNSET
    geometry: Union[Unset, "DeprecatedTrackerEventGeometry"] = UNSET
    href: Union[Unset, str] = UNSET
    last_updated: Union[Unset, str] = UNSET
    last_updated_by_user_info: Union[Unset, "UserInfoSnapshot"] = UNSET
    notes: Union[Unset, list["DeprecatedTrackerNote"]] = UNSET
    org_unit: Union[Unset, str] = UNSET
    org_unit_name: Union[Unset, str] = UNSET
    relationships: Union[Unset, list["DeprecatedTrackerRelationship"]] = UNSET
    stored_by: Union[Unset, str] = UNSET
    tracked_entity_instance: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at_client = self.created_at_client

        enrollment = self.enrollment

        enrollment_status = self.enrollment_status.value

        event = self.event

        event_date = self.event_date

        last_updated_at_client = self.last_updated_at_client

        program = self.program

        program_stage = self.program_stage

        program_type = self.program_type.value

        status = self.status.value

        assigned_user = self.assigned_user

        assigned_user_display_name = self.assigned_user_display_name

        assigned_user_first_name = self.assigned_user_first_name

        assigned_user_surname = self.assigned_user_surname

        assigned_user_username = self.assigned_user_username

        attribute_category_options = self.attribute_category_options

        attribute_option_combo = self.attribute_option_combo

        completed_by = self.completed_by

        completed_date = self.completed_date

        created = self.created

        created_by_user_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by_user_info, Unset):
            created_by_user_info = self.created_by_user_info.to_dict()

        data_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_values, Unset):
            data_values = []
            for data_values_item_data in self.data_values:
                data_values_item = data_values_item_data.to_dict()
                data_values.append(data_values_item)

        deleted = self.deleted

        due_date = self.due_date

        followup = self.followup

        geometry: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.geometry, Unset):
            geometry = self.geometry.to_dict()

        href = self.href

        last_updated = self.last_updated

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

        tracked_entity_instance = self.tracked_entity_instance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAtClient": created_at_client,
                "enrollment": enrollment,
                "enrollmentStatus": enrollment_status,
                "event": event,
                "eventDate": event_date,
                "lastUpdatedAtClient": last_updated_at_client,
                "program": program,
                "programStage": program_stage,
                "programType": program_type,
                "status": status,
            }
        )
        if assigned_user is not UNSET:
            field_dict["assignedUser"] = assigned_user
        if assigned_user_display_name is not UNSET:
            field_dict["assignedUserDisplayName"] = assigned_user_display_name
        if assigned_user_first_name is not UNSET:
            field_dict["assignedUserFirstName"] = assigned_user_first_name
        if assigned_user_surname is not UNSET:
            field_dict["assignedUserSurname"] = assigned_user_surname
        if assigned_user_username is not UNSET:
            field_dict["assignedUserUsername"] = assigned_user_username
        if attribute_category_options is not UNSET:
            field_dict["attributeCategoryOptions"] = attribute_category_options
        if attribute_option_combo is not UNSET:
            field_dict["attributeOptionCombo"] = attribute_option_combo
        if completed_by is not UNSET:
            field_dict["completedBy"] = completed_by
        if completed_date is not UNSET:
            field_dict["completedDate"] = completed_date
        if created is not UNSET:
            field_dict["created"] = created
        if created_by_user_info is not UNSET:
            field_dict["createdByUserInfo"] = created_by_user_info
        if data_values is not UNSET:
            field_dict["dataValues"] = data_values
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if followup is not UNSET:
            field_dict["followup"] = followup
        if geometry is not UNSET:
            field_dict["geometry"] = geometry
        if href is not UNSET:
            field_dict["href"] = href
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
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
        if tracked_entity_instance is not UNSET:
            field_dict["trackedEntityInstance"] = tracked_entity_instance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.deprecated_tracker_data_value import DeprecatedTrackerDataValue
        from ..models.deprecated_tracker_event_geometry import DeprecatedTrackerEventGeometry
        from ..models.deprecated_tracker_note import DeprecatedTrackerNote
        from ..models.deprecated_tracker_relationship import DeprecatedTrackerRelationship
        from ..models.user_info_snapshot import UserInfoSnapshot

        d = src_dict.copy()
        created_at_client = d.pop("createdAtClient")

        enrollment = d.pop("enrollment")

        enrollment_status = DeprecatedTrackerEventEnrollmentStatus(d.pop("enrollmentStatus"))

        event = d.pop("event")

        event_date = d.pop("eventDate")

        last_updated_at_client = d.pop("lastUpdatedAtClient")

        program = d.pop("program")

        program_stage = d.pop("programStage")

        program_type = DeprecatedTrackerEventProgramType(d.pop("programType"))

        status = DeprecatedTrackerEventStatus(d.pop("status"))

        assigned_user = d.pop("assignedUser", UNSET)

        assigned_user_display_name = d.pop("assignedUserDisplayName", UNSET)

        assigned_user_first_name = d.pop("assignedUserFirstName", UNSET)

        assigned_user_surname = d.pop("assignedUserSurname", UNSET)

        assigned_user_username = d.pop("assignedUserUsername", UNSET)

        attribute_category_options = d.pop("attributeCategoryOptions", UNSET)

        attribute_option_combo = d.pop("attributeOptionCombo", UNSET)

        completed_by = d.pop("completedBy", UNSET)

        completed_date = d.pop("completedDate", UNSET)

        created = d.pop("created", UNSET)

        _created_by_user_info = d.pop("createdByUserInfo", UNSET)
        created_by_user_info: Union[Unset, UserInfoSnapshot]
        if isinstance(_created_by_user_info, Unset):
            created_by_user_info = UNSET
        else:
            created_by_user_info = UserInfoSnapshot.from_dict(_created_by_user_info)

        data_values = []
        _data_values = d.pop("dataValues", UNSET)
        for data_values_item_data in _data_values or []:
            data_values_item = DeprecatedTrackerDataValue.from_dict(data_values_item_data)

            data_values.append(data_values_item)

        deleted = d.pop("deleted", UNSET)

        due_date = d.pop("dueDate", UNSET)

        followup = d.pop("followup", UNSET)

        _geometry = d.pop("geometry", UNSET)
        geometry: Union[Unset, DeprecatedTrackerEventGeometry]
        if isinstance(_geometry, Unset):
            geometry = UNSET
        else:
            geometry = DeprecatedTrackerEventGeometry.from_dict(_geometry)

        href = d.pop("href", UNSET)

        last_updated = d.pop("lastUpdated", UNSET)

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

        tracked_entity_instance = d.pop("trackedEntityInstance", UNSET)

        deprecated_tracker_event = cls(
            created_at_client=created_at_client,
            enrollment=enrollment,
            enrollment_status=enrollment_status,
            event=event,
            event_date=event_date,
            last_updated_at_client=last_updated_at_client,
            program=program,
            program_stage=program_stage,
            program_type=program_type,
            status=status,
            assigned_user=assigned_user,
            assigned_user_display_name=assigned_user_display_name,
            assigned_user_first_name=assigned_user_first_name,
            assigned_user_surname=assigned_user_surname,
            assigned_user_username=assigned_user_username,
            attribute_category_options=attribute_category_options,
            attribute_option_combo=attribute_option_combo,
            completed_by=completed_by,
            completed_date=completed_date,
            created=created,
            created_by_user_info=created_by_user_info,
            data_values=data_values,
            deleted=deleted,
            due_date=due_date,
            followup=followup,
            geometry=geometry,
            href=href,
            last_updated=last_updated,
            last_updated_by_user_info=last_updated_by_user_info,
            notes=notes,
            org_unit=org_unit,
            org_unit_name=org_unit_name,
            relationships=relationships,
            stored_by=stored_by,
            tracked_entity_instance=tracked_entity_instance,
        )

        deprecated_tracker_event.additional_properties = d
        return deprecated_tracker_event

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
