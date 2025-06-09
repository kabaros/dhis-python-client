import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tracker_attribute import TrackerAttribute
    from ..models.tracker_enrollment import TrackerEnrollment
    from ..models.tracker_program_owner import TrackerProgramOwner
    from ..models.tracker_relationship import TrackerRelationship
    from ..models.tracker_tracked_entity_geometry import TrackerTrackedEntityGeometry
    from ..models.tracker_user import TrackerUser


T = TypeVar("T", bound="TrackerTrackedEntity")


@_attrs_define
class TrackerTrackedEntity:
    """
    Attributes:
        attributes (Union[Unset, list['TrackerAttribute']]):
        created_at (Union[Unset, datetime.datetime, int]):
        created_at_client (Union[Unset, datetime.datetime, int]):
        created_by (Union[Unset, TrackerUser]):
        deleted (Union[Unset, bool]):
        enrollments (Union[Unset, list['TrackerEnrollment']]):
        geometry (Union[Unset, TrackerTrackedEntityGeometry]):
        inactive (Union[Unset, bool]):
        org_unit (Union[Unset, str]):
        potential_duplicate (Union[Unset, bool]):
        program_owners (Union[Unset, list['TrackerProgramOwner']]):
        relationships (Union[Unset, list['TrackerRelationship']]):
        stored_by (Union[Unset, str]):
        tracked_entity (Union[Unset, str]): A UID for an TrackerTrackedEntity object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.TrackedEntity`) Example: zg9rM85NF00.
        tracked_entity_type (Union[Unset, str]):
        updated_at (Union[Unset, datetime.datetime, int]):
        updated_at_client (Union[Unset, datetime.datetime, int]):
        updated_by (Union[Unset, TrackerUser]):
    """

    attributes: Union[Unset, list["TrackerAttribute"]] = UNSET
    created_at: Union[Unset, datetime.datetime, int] = UNSET
    created_at_client: Union[Unset, datetime.datetime, int] = UNSET
    created_by: Union[Unset, "TrackerUser"] = UNSET
    deleted: Union[Unset, bool] = UNSET
    enrollments: Union[Unset, list["TrackerEnrollment"]] = UNSET
    geometry: Union[Unset, "TrackerTrackedEntityGeometry"] = UNSET
    inactive: Union[Unset, bool] = UNSET
    org_unit: Union[Unset, str] = UNSET
    potential_duplicate: Union[Unset, bool] = UNSET
    program_owners: Union[Unset, list["TrackerProgramOwner"]] = UNSET
    relationships: Union[Unset, list["TrackerRelationship"]] = UNSET
    stored_by: Union[Unset, str] = UNSET
    tracked_entity: Union[Unset, str] = UNSET
    tracked_entity_type: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime, int] = UNSET
    updated_at_client: Union[Unset, datetime.datetime, int] = UNSET
    updated_by: Union[Unset, "TrackerUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()
                attributes.append(attributes_item)

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

        enrollments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.enrollments, Unset):
            enrollments = []
            for enrollments_item_data in self.enrollments:
                enrollments_item = enrollments_item_data.to_dict()
                enrollments.append(enrollments_item)

        geometry: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.geometry, Unset):
            geometry = self.geometry.to_dict()

        inactive = self.inactive

        org_unit = self.org_unit

        potential_duplicate = self.potential_duplicate

        program_owners: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.program_owners, Unset):
            program_owners = []
            for program_owners_item_data in self.program_owners:
                program_owners_item = program_owners_item_data.to_dict()
                program_owners.append(program_owners_item)

        relationships: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = []
            for relationships_item_data in self.relationships:
                relationships_item = relationships_item_data.to_dict()
                relationships.append(relationships_item)

        stored_by = self.stored_by

        tracked_entity = self.tracked_entity

        tracked_entity_type = self.tracked_entity_type

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
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_at_client is not UNSET:
            field_dict["createdAtClient"] = created_at_client
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if enrollments is not UNSET:
            field_dict["enrollments"] = enrollments
        if geometry is not UNSET:
            field_dict["geometry"] = geometry
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if org_unit is not UNSET:
            field_dict["orgUnit"] = org_unit
        if potential_duplicate is not UNSET:
            field_dict["potentialDuplicate"] = potential_duplicate
        if program_owners is not UNSET:
            field_dict["programOwners"] = program_owners
        if relationships is not UNSET:
            field_dict["relationships"] = relationships
        if stored_by is not UNSET:
            field_dict["storedBy"] = stored_by
        if tracked_entity is not UNSET:
            field_dict["trackedEntity"] = tracked_entity
        if tracked_entity_type is not UNSET:
            field_dict["trackedEntityType"] = tracked_entity_type
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
        from ..models.tracker_enrollment import TrackerEnrollment
        from ..models.tracker_program_owner import TrackerProgramOwner
        from ..models.tracker_relationship import TrackerRelationship
        from ..models.tracker_tracked_entity_geometry import TrackerTrackedEntityGeometry
        from ..models.tracker_user import TrackerUser

        d = src_dict.copy()
        attributes = []
        _attributes = d.pop("attributes", UNSET)
        for attributes_item_data in _attributes or []:
            attributes_item = TrackerAttribute.from_dict(attributes_item_data)

            attributes.append(attributes_item)

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

        enrollments = []
        _enrollments = d.pop("enrollments", UNSET)
        for enrollments_item_data in _enrollments or []:
            enrollments_item = TrackerEnrollment.from_dict(enrollments_item_data)

            enrollments.append(enrollments_item)

        _geometry = d.pop("geometry", UNSET)
        geometry: Union[Unset, TrackerTrackedEntityGeometry]
        if isinstance(_geometry, Unset):
            geometry = UNSET
        else:
            geometry = TrackerTrackedEntityGeometry.from_dict(_geometry)

        inactive = d.pop("inactive", UNSET)

        org_unit = d.pop("orgUnit", UNSET)

        potential_duplicate = d.pop("potentialDuplicate", UNSET)

        program_owners = []
        _program_owners = d.pop("programOwners", UNSET)
        for program_owners_item_data in _program_owners or []:
            program_owners_item = TrackerProgramOwner.from_dict(program_owners_item_data)

            program_owners.append(program_owners_item)

        relationships = []
        _relationships = d.pop("relationships", UNSET)
        for relationships_item_data in _relationships or []:
            relationships_item = TrackerRelationship.from_dict(relationships_item_data)

            relationships.append(relationships_item)

        stored_by = d.pop("storedBy", UNSET)

        tracked_entity = d.pop("trackedEntity", UNSET)

        tracked_entity_type = d.pop("trackedEntityType", UNSET)

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

        tracker_tracked_entity = cls(
            attributes=attributes,
            created_at=created_at,
            created_at_client=created_at_client,
            created_by=created_by,
            deleted=deleted,
            enrollments=enrollments,
            geometry=geometry,
            inactive=inactive,
            org_unit=org_unit,
            potential_duplicate=potential_duplicate,
            program_owners=program_owners,
            relationships=relationships,
            stored_by=stored_by,
            tracked_entity=tracked_entity,
            tracked_entity_type=tracked_entity_type,
            updated_at=updated_at,
            updated_at_client=updated_at_client,
            updated_by=updated_by,
        )

        tracker_tracked_entity.additional_properties = d
        return tracker_tracked_entity

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
