import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.relationship_item import RelationshipItem
    from ..models.sharing import Sharing
    from ..models.tracked_entity_attribute_value import TrackedEntityAttributeValue
    from ..models.tracked_entity_created_by import TrackedEntityCreatedBy
    from ..models.tracked_entity_enrollments_item import TrackedEntityEnrollmentsItem
    from ..models.tracked_entity_geometry import TrackedEntityGeometry
    from ..models.tracked_entity_last_updated_by import TrackedEntityLastUpdatedBy
    from ..models.tracked_entity_organisation_unit import TrackedEntityOrganisationUnit
    from ..models.tracked_entity_program_owner import TrackedEntityProgramOwner
    from ..models.tracked_entity_tracked_entity_type import TrackedEntityTrackedEntityType
    from ..models.tracked_entity_user import TrackedEntityUser
    from ..models.translation import Translation
    from ..models.user_info_snapshot import UserInfoSnapshot


T = TypeVar("T", bound="TrackedEntity")


@_attrs_define
class TrackedEntity:
    """
    Attributes:
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_at_client (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, TrackedEntityCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        created_by_user_info (Union[Unset, UserInfoSnapshot]):
        deleted (Union[Unset, bool]):
        display_name (Union[Unset, str]):
        enrollments (Union[Unset, list['TrackedEntityEnrollmentsItem']]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        geometry (Union[Unset, TrackedEntityGeometry]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        inactive (Union[Unset, bool]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_at_client (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, TrackedEntityLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        last_updated_by_user_info (Union[Unset, UserInfoSnapshot]):
        name (Union[Unset, str]):
        organisation_unit (Union[Unset, TrackedEntityOrganisationUnit]): A UID reference to a OrganisationUnit
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`)
        potential_duplicate (Union[Unset, bool]):
        program_owners (Union[Unset, list['TrackedEntityProgramOwner']]):
        relationship_items (Union[Unset, list['RelationshipItem']]):
        sharing (Union[Unset, Sharing]):
        stored_by (Union[Unset, str]):
        tracked_entity_attribute_values (Union[Unset, list['TrackedEntityAttributeValue']]):
        tracked_entity_type (Union[Unset, TrackedEntityTrackedEntityType]): A UID reference to a TrackedEntityType
            (Java name `org.hisp.dhis.trackedentity.TrackedEntityType`)
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, TrackedEntityUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_at_client: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "TrackedEntityCreatedBy"] = UNSET
    created_by_user_info: Union[Unset, "UserInfoSnapshot"] = UNSET
    deleted: Union[Unset, bool] = UNSET
    display_name: Union[Unset, str] = UNSET
    enrollments: Union[Unset, list["TrackedEntityEnrollmentsItem"]] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    geometry: Union[Unset, "TrackedEntityGeometry"] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    inactive: Union[Unset, bool] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_at_client: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "TrackedEntityLastUpdatedBy"] = UNSET
    last_updated_by_user_info: Union[Unset, "UserInfoSnapshot"] = UNSET
    name: Union[Unset, str] = UNSET
    organisation_unit: Union[Unset, "TrackedEntityOrganisationUnit"] = UNSET
    potential_duplicate: Union[Unset, bool] = UNSET
    program_owners: Union[Unset, list["TrackedEntityProgramOwner"]] = UNSET
    relationship_items: Union[Unset, list["RelationshipItem"]] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    stored_by: Union[Unset, str] = UNSET
    tracked_entity_attribute_values: Union[Unset, list["TrackedEntityAttributeValue"]] = UNSET
    tracked_entity_type: Union[Unset, "TrackedEntityTrackedEntityType"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "TrackedEntityUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        attribute_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_values, Unset):
            attribute_values = []
            for attribute_values_item_data in self.attribute_values:
                attribute_values_item = attribute_values_item_data.to_dict()
                attribute_values.append(attribute_values_item)

        code = self.code

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_at_client: Union[Unset, str] = UNSET
        if not isinstance(self.created_at_client, Unset):
            created_at_client = self.created_at_client.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        created_by_user_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by_user_info, Unset):
            created_by_user_info = self.created_by_user_info.to_dict()

        deleted = self.deleted

        display_name = self.display_name

        enrollments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.enrollments, Unset):
            enrollments = []
            for enrollments_item_data in self.enrollments:
                enrollments_item = enrollments_item_data.to_dict()
                enrollments.append(enrollments_item)

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        geometry: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.geometry, Unset):
            geometry = self.geometry.to_dict()

        href = self.href

        id = self.id

        inactive = self.inactive

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_at_client: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_at_client, Unset):
            last_updated_at_client = self.last_updated_at_client.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        last_updated_by_user_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by_user_info, Unset):
            last_updated_by_user_info = self.last_updated_by_user_info.to_dict()

        name = self.name

        organisation_unit: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organisation_unit, Unset):
            organisation_unit = self.organisation_unit.to_dict()

        potential_duplicate = self.potential_duplicate

        program_owners: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.program_owners, Unset):
            program_owners = []
            for program_owners_item_data in self.program_owners:
                program_owners_item = program_owners_item_data.to_dict()
                program_owners.append(program_owners_item)

        relationship_items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.relationship_items, Unset):
            relationship_items = []
            for relationship_items_item_data in self.relationship_items:
                relationship_items_item = relationship_items_item_data.to_dict()
                relationship_items.append(relationship_items_item)

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        stored_by = self.stored_by

        tracked_entity_attribute_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tracked_entity_attribute_values, Unset):
            tracked_entity_attribute_values = []
            for tracked_entity_attribute_values_item_data in self.tracked_entity_attribute_values:
                tracked_entity_attribute_values_item = tracked_entity_attribute_values_item_data.to_dict()
                tracked_entity_attribute_values.append(tracked_entity_attribute_values_item)

        tracked_entity_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tracked_entity_type, Unset):
            tracked_entity_type = self.tracked_entity_type.to_dict()

        translations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access is not UNSET:
            field_dict["access"] = access
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if code is not UNSET:
            field_dict["code"] = code
        if created is not UNSET:
            field_dict["created"] = created
        if created_at_client is not UNSET:
            field_dict["createdAtClient"] = created_at_client
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_by_user_info is not UNSET:
            field_dict["createdByUserInfo"] = created_by_user_info
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if enrollments is not UNSET:
            field_dict["enrollments"] = enrollments
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if geometry is not UNSET:
            field_dict["geometry"] = geometry
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_at_client is not UNSET:
            field_dict["lastUpdatedAtClient"] = last_updated_at_client
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if last_updated_by_user_info is not UNSET:
            field_dict["lastUpdatedByUserInfo"] = last_updated_by_user_info
        if name is not UNSET:
            field_dict["name"] = name
        if organisation_unit is not UNSET:
            field_dict["organisationUnit"] = organisation_unit
        if potential_duplicate is not UNSET:
            field_dict["potentialDuplicate"] = potential_duplicate
        if program_owners is not UNSET:
            field_dict["programOwners"] = program_owners
        if relationship_items is not UNSET:
            field_dict["relationshipItems"] = relationship_items
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if stored_by is not UNSET:
            field_dict["storedBy"] = stored_by
        if tracked_entity_attribute_values is not UNSET:
            field_dict["trackedEntityAttributeValues"] = tracked_entity_attribute_values
        if tracked_entity_type is not UNSET:
            field_dict["trackedEntityType"] = tracked_entity_type
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.relationship_item import RelationshipItem
        from ..models.sharing import Sharing
        from ..models.tracked_entity_attribute_value import TrackedEntityAttributeValue
        from ..models.tracked_entity_created_by import TrackedEntityCreatedBy
        from ..models.tracked_entity_enrollments_item import TrackedEntityEnrollmentsItem
        from ..models.tracked_entity_geometry import TrackedEntityGeometry
        from ..models.tracked_entity_last_updated_by import TrackedEntityLastUpdatedBy
        from ..models.tracked_entity_organisation_unit import TrackedEntityOrganisationUnit
        from ..models.tracked_entity_program_owner import TrackedEntityProgramOwner
        from ..models.tracked_entity_tracked_entity_type import TrackedEntityTrackedEntityType
        from ..models.tracked_entity_user import TrackedEntityUser
        from ..models.translation import Translation
        from ..models.user_info_snapshot import UserInfoSnapshot

        d = src_dict.copy()
        _access = d.pop("access", UNSET)
        access: Union[Unset, Access]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

        attribute_values = []
        _attribute_values = d.pop("attributeValues", UNSET)
        for attribute_values_item_data in _attribute_values or []:
            attribute_values_item = AttributeValue.from_dict(attribute_values_item_data)

            attribute_values.append(attribute_values_item)

        code = d.pop("code", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_at_client = d.pop("createdAtClient", UNSET)
        created_at_client: Union[Unset, datetime.datetime]
        if isinstance(_created_at_client, Unset):
            created_at_client = UNSET
        else:
            created_at_client = isoparse(_created_at_client)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, TrackedEntityCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = TrackedEntityCreatedBy.from_dict(_created_by)

        _created_by_user_info = d.pop("createdByUserInfo", UNSET)
        created_by_user_info: Union[Unset, UserInfoSnapshot]
        if isinstance(_created_by_user_info, Unset):
            created_by_user_info = UNSET
        else:
            created_by_user_info = UserInfoSnapshot.from_dict(_created_by_user_info)

        deleted = d.pop("deleted", UNSET)

        display_name = d.pop("displayName", UNSET)

        enrollments = []
        _enrollments = d.pop("enrollments", UNSET)
        for enrollments_item_data in _enrollments or []:
            enrollments_item = TrackedEntityEnrollmentsItem.from_dict(enrollments_item_data)

            enrollments.append(enrollments_item)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        _geometry = d.pop("geometry", UNSET)
        geometry: Union[Unset, TrackedEntityGeometry]
        if isinstance(_geometry, Unset):
            geometry = UNSET
        else:
            geometry = TrackedEntityGeometry.from_dict(_geometry)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        inactive = d.pop("inactive", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_at_client = d.pop("lastUpdatedAtClient", UNSET)
        last_updated_at_client: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_at_client, Unset):
            last_updated_at_client = UNSET
        else:
            last_updated_at_client = isoparse(_last_updated_at_client)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, TrackedEntityLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = TrackedEntityLastUpdatedBy.from_dict(_last_updated_by)

        _last_updated_by_user_info = d.pop("lastUpdatedByUserInfo", UNSET)
        last_updated_by_user_info: Union[Unset, UserInfoSnapshot]
        if isinstance(_last_updated_by_user_info, Unset):
            last_updated_by_user_info = UNSET
        else:
            last_updated_by_user_info = UserInfoSnapshot.from_dict(_last_updated_by_user_info)

        name = d.pop("name", UNSET)

        _organisation_unit = d.pop("organisationUnit", UNSET)
        organisation_unit: Union[Unset, TrackedEntityOrganisationUnit]
        if isinstance(_organisation_unit, Unset):
            organisation_unit = UNSET
        else:
            organisation_unit = TrackedEntityOrganisationUnit.from_dict(_organisation_unit)

        potential_duplicate = d.pop("potentialDuplicate", UNSET)

        program_owners = []
        _program_owners = d.pop("programOwners", UNSET)
        for program_owners_item_data in _program_owners or []:
            program_owners_item = TrackedEntityProgramOwner.from_dict(program_owners_item_data)

            program_owners.append(program_owners_item)

        relationship_items = []
        _relationship_items = d.pop("relationshipItems", UNSET)
        for relationship_items_item_data in _relationship_items or []:
            relationship_items_item = RelationshipItem.from_dict(relationship_items_item_data)

            relationship_items.append(relationship_items_item)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        stored_by = d.pop("storedBy", UNSET)

        tracked_entity_attribute_values = []
        _tracked_entity_attribute_values = d.pop("trackedEntityAttributeValues", UNSET)
        for tracked_entity_attribute_values_item_data in _tracked_entity_attribute_values or []:
            tracked_entity_attribute_values_item = TrackedEntityAttributeValue.from_dict(
                tracked_entity_attribute_values_item_data
            )

            tracked_entity_attribute_values.append(tracked_entity_attribute_values_item)

        _tracked_entity_type = d.pop("trackedEntityType", UNSET)
        tracked_entity_type: Union[Unset, TrackedEntityTrackedEntityType]
        if isinstance(_tracked_entity_type, Unset):
            tracked_entity_type = UNSET
        else:
            tracked_entity_type = TrackedEntityTrackedEntityType.from_dict(_tracked_entity_type)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, TrackedEntityUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = TrackedEntityUser.from_dict(_user)

        tracked_entity = cls(
            access=access,
            attribute_values=attribute_values,
            code=code,
            created=created,
            created_at_client=created_at_client,
            created_by=created_by,
            created_by_user_info=created_by_user_info,
            deleted=deleted,
            display_name=display_name,
            enrollments=enrollments,
            favorite=favorite,
            favorites=favorites,
            geometry=geometry,
            href=href,
            id=id,
            inactive=inactive,
            last_updated=last_updated,
            last_updated_at_client=last_updated_at_client,
            last_updated_by=last_updated_by,
            last_updated_by_user_info=last_updated_by_user_info,
            name=name,
            organisation_unit=organisation_unit,
            potential_duplicate=potential_duplicate,
            program_owners=program_owners,
            relationship_items=relationship_items,
            sharing=sharing,
            stored_by=stored_by,
            tracked_entity_attribute_values=tracked_entity_attribute_values,
            tracked_entity_type=tracked_entity_type,
            translations=translations,
            user=user,
        )

        tracked_entity.additional_properties = d
        return tracked_entity

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
