import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.enrollment_status import EnrollmentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.enrollment_created_by import EnrollmentCreatedBy
    from ..models.enrollment_events_item import EnrollmentEventsItem
    from ..models.enrollment_geometry import EnrollmentGeometry
    from ..models.enrollment_last_updated_by import EnrollmentLastUpdatedBy
    from ..models.enrollment_message_conversations_item import EnrollmentMessageConversationsItem
    from ..models.enrollment_organisation_unit import EnrollmentOrganisationUnit
    from ..models.enrollment_program import EnrollmentProgram
    from ..models.enrollment_tracked_entity_comments_item import EnrollmentTrackedEntityCommentsItem
    from ..models.enrollment_tracked_entity_instance import EnrollmentTrackedEntityInstance
    from ..models.enrollment_user import EnrollmentUser
    from ..models.relationship_item import RelationshipItem
    from ..models.sharing import Sharing
    from ..models.translation import Translation
    from ..models.user_info_snapshot import UserInfoSnapshot


T = TypeVar("T", bound="Enrollment")


@_attrs_define
class Enrollment:
    """
    Attributes:
        status (EnrollmentStatus):
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        completed_by (Union[Unset, str]):
        completed_date (Union[Unset, datetime.datetime]):
        created (Union[Unset, datetime.datetime]):
        created_at_client (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, EnrollmentCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        created_by_user_info (Union[Unset, UserInfoSnapshot]):
        deleted (Union[Unset, bool]):
        display_name (Union[Unset, str]):
        enrollment_date (Union[Unset, datetime.datetime]):
        events (Union[Unset, list['EnrollmentEventsItem']]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        followup (Union[Unset, bool]):
        geometry (Union[Unset, EnrollmentGeometry]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_at_client (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, EnrollmentLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        last_updated_by_user_info (Union[Unset, UserInfoSnapshot]):
        message_conversations (Union[Unset, list['EnrollmentMessageConversationsItem']]):
        name (Union[Unset, str]):
        occurred_date (Union[Unset, datetime.datetime]):
        organisation_unit (Union[Unset, EnrollmentOrganisationUnit]): A UID reference to a OrganisationUnit
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`)
        program (Union[Unset, EnrollmentProgram]): A UID reference to a Program
            (Java name `org.hisp.dhis.program.Program`)
        relationship_items (Union[Unset, list['RelationshipItem']]):
        sharing (Union[Unset, Sharing]):
        stored_by (Union[Unset, str]):
        tracked_entity_comments (Union[Unset, list['EnrollmentTrackedEntityCommentsItem']]):
        tracked_entity_instance (Union[Unset, EnrollmentTrackedEntityInstance]): A UID reference to a TrackedEntity
            (Java name `org.hisp.dhis.trackedentity.TrackedEntity`)
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, EnrollmentUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    status: EnrollmentStatus
    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    completed_by: Union[Unset, str] = UNSET
    completed_date: Union[Unset, datetime.datetime] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_at_client: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "EnrollmentCreatedBy"] = UNSET
    created_by_user_info: Union[Unset, "UserInfoSnapshot"] = UNSET
    deleted: Union[Unset, bool] = UNSET
    display_name: Union[Unset, str] = UNSET
    enrollment_date: Union[Unset, datetime.datetime] = UNSET
    events: Union[Unset, list["EnrollmentEventsItem"]] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    followup: Union[Unset, bool] = UNSET
    geometry: Union[Unset, "EnrollmentGeometry"] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_at_client: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "EnrollmentLastUpdatedBy"] = UNSET
    last_updated_by_user_info: Union[Unset, "UserInfoSnapshot"] = UNSET
    message_conversations: Union[Unset, list["EnrollmentMessageConversationsItem"]] = UNSET
    name: Union[Unset, str] = UNSET
    occurred_date: Union[Unset, datetime.datetime] = UNSET
    organisation_unit: Union[Unset, "EnrollmentOrganisationUnit"] = UNSET
    program: Union[Unset, "EnrollmentProgram"] = UNSET
    relationship_items: Union[Unset, list["RelationshipItem"]] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    stored_by: Union[Unset, str] = UNSET
    tracked_entity_comments: Union[Unset, list["EnrollmentTrackedEntityCommentsItem"]] = UNSET
    tracked_entity_instance: Union[Unset, "EnrollmentTrackedEntityInstance"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "EnrollmentUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

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

        completed_by = self.completed_by

        completed_date: Union[Unset, str] = UNSET
        if not isinstance(self.completed_date, Unset):
            completed_date = self.completed_date.isoformat()

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

        enrollment_date: Union[Unset, str] = UNSET
        if not isinstance(self.enrollment_date, Unset):
            enrollment_date = self.enrollment_date.isoformat()

        events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        followup = self.followup

        geometry: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.geometry, Unset):
            geometry = self.geometry.to_dict()

        href = self.href

        id = self.id

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

        message_conversations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.message_conversations, Unset):
            message_conversations = []
            for message_conversations_item_data in self.message_conversations:
                message_conversations_item = message_conversations_item_data.to_dict()
                message_conversations.append(message_conversations_item)

        name = self.name

        occurred_date: Union[Unset, str] = UNSET
        if not isinstance(self.occurred_date, Unset):
            occurred_date = self.occurred_date.isoformat()

        organisation_unit: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organisation_unit, Unset):
            organisation_unit = self.organisation_unit.to_dict()

        program: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program, Unset):
            program = self.program.to_dict()

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

        tracked_entity_comments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tracked_entity_comments, Unset):
            tracked_entity_comments = []
            for tracked_entity_comments_item_data in self.tracked_entity_comments:
                tracked_entity_comments_item = tracked_entity_comments_item_data.to_dict()
                tracked_entity_comments.append(tracked_entity_comments_item)

        tracked_entity_instance: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tracked_entity_instance, Unset):
            tracked_entity_instance = self.tracked_entity_instance.to_dict()

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
        field_dict.update(
            {
                "status": status,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if code is not UNSET:
            field_dict["code"] = code
        if completed_by is not UNSET:
            field_dict["completedBy"] = completed_by
        if completed_date is not UNSET:
            field_dict["completedDate"] = completed_date
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
        if enrollment_date is not UNSET:
            field_dict["enrollmentDate"] = enrollment_date
        if events is not UNSET:
            field_dict["events"] = events
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if followup is not UNSET:
            field_dict["followup"] = followup
        if geometry is not UNSET:
            field_dict["geometry"] = geometry
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_at_client is not UNSET:
            field_dict["lastUpdatedAtClient"] = last_updated_at_client
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if last_updated_by_user_info is not UNSET:
            field_dict["lastUpdatedByUserInfo"] = last_updated_by_user_info
        if message_conversations is not UNSET:
            field_dict["messageConversations"] = message_conversations
        if name is not UNSET:
            field_dict["name"] = name
        if occurred_date is not UNSET:
            field_dict["occurredDate"] = occurred_date
        if organisation_unit is not UNSET:
            field_dict["organisationUnit"] = organisation_unit
        if program is not UNSET:
            field_dict["program"] = program
        if relationship_items is not UNSET:
            field_dict["relationshipItems"] = relationship_items
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if stored_by is not UNSET:
            field_dict["storedBy"] = stored_by
        if tracked_entity_comments is not UNSET:
            field_dict["trackedEntityComments"] = tracked_entity_comments
        if tracked_entity_instance is not UNSET:
            field_dict["trackedEntityInstance"] = tracked_entity_instance
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.enrollment_created_by import EnrollmentCreatedBy
        from ..models.enrollment_events_item import EnrollmentEventsItem
        from ..models.enrollment_geometry import EnrollmentGeometry
        from ..models.enrollment_last_updated_by import EnrollmentLastUpdatedBy
        from ..models.enrollment_message_conversations_item import EnrollmentMessageConversationsItem
        from ..models.enrollment_organisation_unit import EnrollmentOrganisationUnit
        from ..models.enrollment_program import EnrollmentProgram
        from ..models.enrollment_tracked_entity_comments_item import EnrollmentTrackedEntityCommentsItem
        from ..models.enrollment_tracked_entity_instance import EnrollmentTrackedEntityInstance
        from ..models.enrollment_user import EnrollmentUser
        from ..models.relationship_item import RelationshipItem
        from ..models.sharing import Sharing
        from ..models.translation import Translation
        from ..models.user_info_snapshot import UserInfoSnapshot

        d = src_dict.copy()
        status = EnrollmentStatus(d.pop("status"))

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

        completed_by = d.pop("completedBy", UNSET)

        _completed_date = d.pop("completedDate", UNSET)
        completed_date: Union[Unset, datetime.datetime]
        if isinstance(_completed_date, Unset):
            completed_date = UNSET
        else:
            completed_date = isoparse(_completed_date)

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
        created_by: Union[Unset, EnrollmentCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = EnrollmentCreatedBy.from_dict(_created_by)

        _created_by_user_info = d.pop("createdByUserInfo", UNSET)
        created_by_user_info: Union[Unset, UserInfoSnapshot]
        if isinstance(_created_by_user_info, Unset):
            created_by_user_info = UNSET
        else:
            created_by_user_info = UserInfoSnapshot.from_dict(_created_by_user_info)

        deleted = d.pop("deleted", UNSET)

        display_name = d.pop("displayName", UNSET)

        _enrollment_date = d.pop("enrollmentDate", UNSET)
        enrollment_date: Union[Unset, datetime.datetime]
        if isinstance(_enrollment_date, Unset):
            enrollment_date = UNSET
        else:
            enrollment_date = isoparse(_enrollment_date)

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = EnrollmentEventsItem.from_dict(events_item_data)

            events.append(events_item)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        followup = d.pop("followup", UNSET)

        _geometry = d.pop("geometry", UNSET)
        geometry: Union[Unset, EnrollmentGeometry]
        if isinstance(_geometry, Unset):
            geometry = UNSET
        else:
            geometry = EnrollmentGeometry.from_dict(_geometry)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

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
        last_updated_by: Union[Unset, EnrollmentLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = EnrollmentLastUpdatedBy.from_dict(_last_updated_by)

        _last_updated_by_user_info = d.pop("lastUpdatedByUserInfo", UNSET)
        last_updated_by_user_info: Union[Unset, UserInfoSnapshot]
        if isinstance(_last_updated_by_user_info, Unset):
            last_updated_by_user_info = UNSET
        else:
            last_updated_by_user_info = UserInfoSnapshot.from_dict(_last_updated_by_user_info)

        message_conversations = []
        _message_conversations = d.pop("messageConversations", UNSET)
        for message_conversations_item_data in _message_conversations or []:
            message_conversations_item = EnrollmentMessageConversationsItem.from_dict(message_conversations_item_data)

            message_conversations.append(message_conversations_item)

        name = d.pop("name", UNSET)

        _occurred_date = d.pop("occurredDate", UNSET)
        occurred_date: Union[Unset, datetime.datetime]
        if isinstance(_occurred_date, Unset):
            occurred_date = UNSET
        else:
            occurred_date = isoparse(_occurred_date)

        _organisation_unit = d.pop("organisationUnit", UNSET)
        organisation_unit: Union[Unset, EnrollmentOrganisationUnit]
        if isinstance(_organisation_unit, Unset):
            organisation_unit = UNSET
        else:
            organisation_unit = EnrollmentOrganisationUnit.from_dict(_organisation_unit)

        _program = d.pop("program", UNSET)
        program: Union[Unset, EnrollmentProgram]
        if isinstance(_program, Unset):
            program = UNSET
        else:
            program = EnrollmentProgram.from_dict(_program)

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

        tracked_entity_comments = []
        _tracked_entity_comments = d.pop("trackedEntityComments", UNSET)
        for tracked_entity_comments_item_data in _tracked_entity_comments or []:
            tracked_entity_comments_item = EnrollmentTrackedEntityCommentsItem.from_dict(
                tracked_entity_comments_item_data
            )

            tracked_entity_comments.append(tracked_entity_comments_item)

        _tracked_entity_instance = d.pop("trackedEntityInstance", UNSET)
        tracked_entity_instance: Union[Unset, EnrollmentTrackedEntityInstance]
        if isinstance(_tracked_entity_instance, Unset):
            tracked_entity_instance = UNSET
        else:
            tracked_entity_instance = EnrollmentTrackedEntityInstance.from_dict(_tracked_entity_instance)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, EnrollmentUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = EnrollmentUser.from_dict(_user)

        enrollment = cls(
            status=status,
            access=access,
            attribute_values=attribute_values,
            code=code,
            completed_by=completed_by,
            completed_date=completed_date,
            created=created,
            created_at_client=created_at_client,
            created_by=created_by,
            created_by_user_info=created_by_user_info,
            deleted=deleted,
            display_name=display_name,
            enrollment_date=enrollment_date,
            events=events,
            favorite=favorite,
            favorites=favorites,
            followup=followup,
            geometry=geometry,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_at_client=last_updated_at_client,
            last_updated_by=last_updated_by,
            last_updated_by_user_info=last_updated_by_user_info,
            message_conversations=message_conversations,
            name=name,
            occurred_date=occurred_date,
            organisation_unit=organisation_unit,
            program=program,
            relationship_items=relationship_items,
            sharing=sharing,
            stored_by=stored_by,
            tracked_entity_comments=tracked_entity_comments,
            tracked_entity_instance=tracked_entity_instance,
            translations=translations,
            user=user,
        )

        enrollment.additional_properties = d
        return enrollment

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
