from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deprecated_tracker_tracked_entity_instance_feature_type import (
    DeprecatedTrackerTrackedEntityInstanceFeatureType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deprecated_tracker_attribute import DeprecatedTrackerAttribute
    from ..models.deprecated_tracker_enrollment import DeprecatedTrackerEnrollment
    from ..models.deprecated_tracker_program_owner import DeprecatedTrackerProgramOwner
    from ..models.deprecated_tracker_relationship import DeprecatedTrackerRelationship
    from ..models.deprecated_tracker_tracked_entity_instance_geometry import (
        DeprecatedTrackerTrackedEntityInstanceGeometry,
    )
    from ..models.user_info_snapshot import UserInfoSnapshot


T = TypeVar("T", bound="DeprecatedTrackerTrackedEntityInstance")


@_attrs_define
class DeprecatedTrackerTrackedEntityInstance:
    """
    Attributes:
        created (str):
        created_at_client (str):
        feature_type (DeprecatedTrackerTrackedEntityInstanceFeatureType):
        last_updated (str):
        last_updated_at_client (str):
        org_unit (str):
        tracked_entity_instance (str):
        tracked_entity_type (str):
        attributes (Union[Unset, list['DeprecatedTrackerAttribute']]):
        coordinates (Union[Unset, str]):
        created_by_user_info (Union[Unset, UserInfoSnapshot]):
        deleted (Union[Unset, bool]):
        enrollments (Union[Unset, list['DeprecatedTrackerEnrollment']]):
        geometry (Union[Unset, DeprecatedTrackerTrackedEntityInstanceGeometry]):
        inactive (Union[Unset, bool]):
        last_updated_by_user_info (Union[Unset, UserInfoSnapshot]):
        potential_duplicate (Union[Unset, bool]):
        program_owners (Union[Unset, list['DeprecatedTrackerProgramOwner']]):
        relationships (Union[Unset, list['DeprecatedTrackerRelationship']]):
        stored_by (Union[Unset, str]):
    """

    created: str
    created_at_client: str
    feature_type: DeprecatedTrackerTrackedEntityInstanceFeatureType
    last_updated: str
    last_updated_at_client: str
    org_unit: str
    tracked_entity_instance: str
    tracked_entity_type: str
    attributes: Union[Unset, list["DeprecatedTrackerAttribute"]] = UNSET
    coordinates: Union[Unset, str] = UNSET
    created_by_user_info: Union[Unset, "UserInfoSnapshot"] = UNSET
    deleted: Union[Unset, bool] = UNSET
    enrollments: Union[Unset, list["DeprecatedTrackerEnrollment"]] = UNSET
    geometry: Union[Unset, "DeprecatedTrackerTrackedEntityInstanceGeometry"] = UNSET
    inactive: Union[Unset, bool] = UNSET
    last_updated_by_user_info: Union[Unset, "UserInfoSnapshot"] = UNSET
    potential_duplicate: Union[Unset, bool] = UNSET
    program_owners: Union[Unset, list["DeprecatedTrackerProgramOwner"]] = UNSET
    relationships: Union[Unset, list["DeprecatedTrackerRelationship"]] = UNSET
    stored_by: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        created_at_client = self.created_at_client

        feature_type = self.feature_type.value

        last_updated = self.last_updated

        last_updated_at_client = self.last_updated_at_client

        org_unit = self.org_unit

        tracked_entity_instance = self.tracked_entity_instance

        tracked_entity_type = self.tracked_entity_type

        attributes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()
                attributes.append(attributes_item)

        coordinates = self.coordinates

        created_by_user_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by_user_info, Unset):
            created_by_user_info = self.created_by_user_info.to_dict()

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

        last_updated_by_user_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by_user_info, Unset):
            last_updated_by_user_info = self.last_updated_by_user_info.to_dict()

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "createdAtClient": created_at_client,
                "featureType": feature_type,
                "lastUpdated": last_updated,
                "lastUpdatedAtClient": last_updated_at_client,
                "orgUnit": org_unit,
                "trackedEntityInstance": tracked_entity_instance,
                "trackedEntityType": tracked_entity_type,
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if coordinates is not UNSET:
            field_dict["coordinates"] = coordinates
        if created_by_user_info is not UNSET:
            field_dict["createdByUserInfo"] = created_by_user_info
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if enrollments is not UNSET:
            field_dict["enrollments"] = enrollments
        if geometry is not UNSET:
            field_dict["geometry"] = geometry
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if last_updated_by_user_info is not UNSET:
            field_dict["lastUpdatedByUserInfo"] = last_updated_by_user_info
        if potential_duplicate is not UNSET:
            field_dict["potentialDuplicate"] = potential_duplicate
        if program_owners is not UNSET:
            field_dict["programOwners"] = program_owners
        if relationships is not UNSET:
            field_dict["relationships"] = relationships
        if stored_by is not UNSET:
            field_dict["storedBy"] = stored_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.deprecated_tracker_attribute import DeprecatedTrackerAttribute
        from ..models.deprecated_tracker_enrollment import DeprecatedTrackerEnrollment
        from ..models.deprecated_tracker_program_owner import DeprecatedTrackerProgramOwner
        from ..models.deprecated_tracker_relationship import DeprecatedTrackerRelationship
        from ..models.deprecated_tracker_tracked_entity_instance_geometry import (
            DeprecatedTrackerTrackedEntityInstanceGeometry,
        )
        from ..models.user_info_snapshot import UserInfoSnapshot

        d = src_dict.copy()
        created = d.pop("created")

        created_at_client = d.pop("createdAtClient")

        feature_type = DeprecatedTrackerTrackedEntityInstanceFeatureType(d.pop("featureType"))

        last_updated = d.pop("lastUpdated")

        last_updated_at_client = d.pop("lastUpdatedAtClient")

        org_unit = d.pop("orgUnit")

        tracked_entity_instance = d.pop("trackedEntityInstance")

        tracked_entity_type = d.pop("trackedEntityType")

        attributes = []
        _attributes = d.pop("attributes", UNSET)
        for attributes_item_data in _attributes or []:
            attributes_item = DeprecatedTrackerAttribute.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        coordinates = d.pop("coordinates", UNSET)

        _created_by_user_info = d.pop("createdByUserInfo", UNSET)
        created_by_user_info: Union[Unset, UserInfoSnapshot]
        if isinstance(_created_by_user_info, Unset):
            created_by_user_info = UNSET
        else:
            created_by_user_info = UserInfoSnapshot.from_dict(_created_by_user_info)

        deleted = d.pop("deleted", UNSET)

        enrollments = []
        _enrollments = d.pop("enrollments", UNSET)
        for enrollments_item_data in _enrollments or []:
            enrollments_item = DeprecatedTrackerEnrollment.from_dict(enrollments_item_data)

            enrollments.append(enrollments_item)

        _geometry = d.pop("geometry", UNSET)
        geometry: Union[Unset, DeprecatedTrackerTrackedEntityInstanceGeometry]
        if isinstance(_geometry, Unset):
            geometry = UNSET
        else:
            geometry = DeprecatedTrackerTrackedEntityInstanceGeometry.from_dict(_geometry)

        inactive = d.pop("inactive", UNSET)

        _last_updated_by_user_info = d.pop("lastUpdatedByUserInfo", UNSET)
        last_updated_by_user_info: Union[Unset, UserInfoSnapshot]
        if isinstance(_last_updated_by_user_info, Unset):
            last_updated_by_user_info = UNSET
        else:
            last_updated_by_user_info = UserInfoSnapshot.from_dict(_last_updated_by_user_info)

        potential_duplicate = d.pop("potentialDuplicate", UNSET)

        program_owners = []
        _program_owners = d.pop("programOwners", UNSET)
        for program_owners_item_data in _program_owners or []:
            program_owners_item = DeprecatedTrackerProgramOwner.from_dict(program_owners_item_data)

            program_owners.append(program_owners_item)

        relationships = []
        _relationships = d.pop("relationships", UNSET)
        for relationships_item_data in _relationships or []:
            relationships_item = DeprecatedTrackerRelationship.from_dict(relationships_item_data)

            relationships.append(relationships_item)

        stored_by = d.pop("storedBy", UNSET)

        deprecated_tracker_tracked_entity_instance = cls(
            created=created,
            created_at_client=created_at_client,
            feature_type=feature_type,
            last_updated=last_updated,
            last_updated_at_client=last_updated_at_client,
            org_unit=org_unit,
            tracked_entity_instance=tracked_entity_instance,
            tracked_entity_type=tracked_entity_type,
            attributes=attributes,
            coordinates=coordinates,
            created_by_user_info=created_by_user_info,
            deleted=deleted,
            enrollments=enrollments,
            geometry=geometry,
            inactive=inactive,
            last_updated_by_user_info=last_updated_by_user_info,
            potential_duplicate=potential_duplicate,
            program_owners=program_owners,
            relationships=relationships,
            stored_by=stored_by,
        )

        deprecated_tracker_tracked_entity_instance.additional_properties = d
        return deprecated_tracker_tracked_entity_instance

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
