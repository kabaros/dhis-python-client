import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.event_status import EventStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.event_assigned_user import EventAssignedUser
    from ..models.event_attribute_option_combo import EventAttributeOptionCombo
    from ..models.event_created_by import EventCreatedBy
    from ..models.event_data_value import EventDataValue
    from ..models.event_enrollment import EventEnrollment
    from ..models.event_geometry import EventGeometry
    from ..models.event_last_updated_by import EventLastUpdatedBy
    from ..models.event_message_conversations_item import EventMessageConversationsItem
    from ..models.event_notes_item import EventNotesItem
    from ..models.event_organisation_unit import EventOrganisationUnit
    from ..models.event_program_stage import EventProgramStage
    from ..models.event_user import EventUser
    from ..models.relationship_item import RelationshipItem
    from ..models.sharing import Sharing
    from ..models.translation import Translation
    from ..models.user_info_snapshot import UserInfoSnapshot


T = TypeVar("T", bound="Event")


@_attrs_define
class Event:
    """
    Attributes:
        status (EventStatus):
        access (Union[Unset, Access]):
        assigned_user (Union[Unset, EventAssignedUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        attribute_option_combo (Union[Unset, EventAttributeOptionCombo]): A UID reference to a CategoryOptionCombo
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`)
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        completed (Union[Unset, bool]):
        completed_by (Union[Unset, str]):
        completed_date (Union[Unset, datetime.datetime]):
        creatable_in_search_scope (Union[Unset, bool]):
        created (Union[Unset, datetime.datetime]):
        created_at_client (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, EventCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        created_by_user_info (Union[Unset, UserInfoSnapshot]):
        deleted (Union[Unset, bool]):
        display_name (Union[Unset, str]):
        enrollment (Union[Unset, EventEnrollment]): A UID reference to a Enrollment
            (Java name `org.hisp.dhis.program.Enrollment`)
        event_data_values (Union[Unset, list['EventDataValue']]):
        event_date (Union[Unset, datetime.datetime]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        geometry (Union[Unset, EventGeometry]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_at_client (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, EventLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        last_updated_by_user_info (Union[Unset, UserInfoSnapshot]):
        message_conversations (Union[Unset, list['EventMessageConversationsItem']]):
        name (Union[Unset, str]):
        notes (Union[Unset, list['EventNotesItem']]):
        organisation_unit (Union[Unset, EventOrganisationUnit]): A UID reference to a OrganisationUnit
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`)
        program_stage (Union[Unset, EventProgramStage]): A UID reference to a ProgramStage
            (Java name `org.hisp.dhis.program.ProgramStage`)
        relationship_items (Union[Unset, list['RelationshipItem']]):
        scheduled_date (Union[Unset, datetime.datetime]):
        sharing (Union[Unset, Sharing]):
        stored_by (Union[Unset, str]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, EventUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    status: EventStatus
    access: Union[Unset, "Access"] = UNSET
    assigned_user: Union[Unset, "EventAssignedUser"] = UNSET
    attribute_option_combo: Union[Unset, "EventAttributeOptionCombo"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    completed: Union[Unset, bool] = UNSET
    completed_by: Union[Unset, str] = UNSET
    completed_date: Union[Unset, datetime.datetime] = UNSET
    creatable_in_search_scope: Union[Unset, bool] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_at_client: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "EventCreatedBy"] = UNSET
    created_by_user_info: Union[Unset, "UserInfoSnapshot"] = UNSET
    deleted: Union[Unset, bool] = UNSET
    display_name: Union[Unset, str] = UNSET
    enrollment: Union[Unset, "EventEnrollment"] = UNSET
    event_data_values: Union[Unset, list["EventDataValue"]] = UNSET
    event_date: Union[Unset, datetime.datetime] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    geometry: Union[Unset, "EventGeometry"] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_at_client: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "EventLastUpdatedBy"] = UNSET
    last_updated_by_user_info: Union[Unset, "UserInfoSnapshot"] = UNSET
    message_conversations: Union[Unset, list["EventMessageConversationsItem"]] = UNSET
    name: Union[Unset, str] = UNSET
    notes: Union[Unset, list["EventNotesItem"]] = UNSET
    organisation_unit: Union[Unset, "EventOrganisationUnit"] = UNSET
    program_stage: Union[Unset, "EventProgramStage"] = UNSET
    relationship_items: Union[Unset, list["RelationshipItem"]] = UNSET
    scheduled_date: Union[Unset, datetime.datetime] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    stored_by: Union[Unset, str] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "EventUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        assigned_user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.assigned_user, Unset):
            assigned_user = self.assigned_user.to_dict()

        attribute_option_combo: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attribute_option_combo, Unset):
            attribute_option_combo = self.attribute_option_combo.to_dict()

        attribute_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_values, Unset):
            attribute_values = []
            for attribute_values_item_data in self.attribute_values:
                attribute_values_item = attribute_values_item_data.to_dict()
                attribute_values.append(attribute_values_item)

        code = self.code

        completed = self.completed

        completed_by = self.completed_by

        completed_date: Union[Unset, str] = UNSET
        if not isinstance(self.completed_date, Unset):
            completed_date = self.completed_date.isoformat()

        creatable_in_search_scope = self.creatable_in_search_scope

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

        enrollment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.enrollment, Unset):
            enrollment = self.enrollment.to_dict()

        event_data_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.event_data_values, Unset):
            event_data_values = []
            for event_data_values_item_data in self.event_data_values:
                event_data_values_item = event_data_values_item_data.to_dict()
                event_data_values.append(event_data_values_item)

        event_date: Union[Unset, str] = UNSET
        if not isinstance(self.event_date, Unset):
            event_date = self.event_date.isoformat()

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

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

        notes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.notes, Unset):
            notes = []
            for notes_item_data in self.notes:
                notes_item = notes_item_data.to_dict()
                notes.append(notes_item)

        organisation_unit: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organisation_unit, Unset):
            organisation_unit = self.organisation_unit.to_dict()

        program_stage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program_stage, Unset):
            program_stage = self.program_stage.to_dict()

        relationship_items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.relationship_items, Unset):
            relationship_items = []
            for relationship_items_item_data in self.relationship_items:
                relationship_items_item = relationship_items_item_data.to_dict()
                relationship_items.append(relationship_items_item)

        scheduled_date: Union[Unset, str] = UNSET
        if not isinstance(self.scheduled_date, Unset):
            scheduled_date = self.scheduled_date.isoformat()

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        stored_by = self.stored_by

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
        if assigned_user is not UNSET:
            field_dict["assignedUser"] = assigned_user
        if attribute_option_combo is not UNSET:
            field_dict["attributeOptionCombo"] = attribute_option_combo
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if code is not UNSET:
            field_dict["code"] = code
        if completed is not UNSET:
            field_dict["completed"] = completed
        if completed_by is not UNSET:
            field_dict["completedBy"] = completed_by
        if completed_date is not UNSET:
            field_dict["completedDate"] = completed_date
        if creatable_in_search_scope is not UNSET:
            field_dict["creatableInSearchScope"] = creatable_in_search_scope
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
        if enrollment is not UNSET:
            field_dict["enrollment"] = enrollment
        if event_data_values is not UNSET:
            field_dict["eventDataValues"] = event_data_values
        if event_date is not UNSET:
            field_dict["eventDate"] = event_date
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
        if notes is not UNSET:
            field_dict["notes"] = notes
        if organisation_unit is not UNSET:
            field_dict["organisationUnit"] = organisation_unit
        if program_stage is not UNSET:
            field_dict["programStage"] = program_stage
        if relationship_items is not UNSET:
            field_dict["relationshipItems"] = relationship_items
        if scheduled_date is not UNSET:
            field_dict["scheduledDate"] = scheduled_date
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if stored_by is not UNSET:
            field_dict["storedBy"] = stored_by
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.event_assigned_user import EventAssignedUser
        from ..models.event_attribute_option_combo import EventAttributeOptionCombo
        from ..models.event_created_by import EventCreatedBy
        from ..models.event_data_value import EventDataValue
        from ..models.event_enrollment import EventEnrollment
        from ..models.event_geometry import EventGeometry
        from ..models.event_last_updated_by import EventLastUpdatedBy
        from ..models.event_message_conversations_item import EventMessageConversationsItem
        from ..models.event_notes_item import EventNotesItem
        from ..models.event_organisation_unit import EventOrganisationUnit
        from ..models.event_program_stage import EventProgramStage
        from ..models.event_user import EventUser
        from ..models.relationship_item import RelationshipItem
        from ..models.sharing import Sharing
        from ..models.translation import Translation
        from ..models.user_info_snapshot import UserInfoSnapshot

        d = src_dict.copy()
        status = EventStatus(d.pop("status"))

        _access = d.pop("access", UNSET)
        access: Union[Unset, Access]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

        _assigned_user = d.pop("assignedUser", UNSET)
        assigned_user: Union[Unset, EventAssignedUser]
        if isinstance(_assigned_user, Unset):
            assigned_user = UNSET
        else:
            assigned_user = EventAssignedUser.from_dict(_assigned_user)

        _attribute_option_combo = d.pop("attributeOptionCombo", UNSET)
        attribute_option_combo: Union[Unset, EventAttributeOptionCombo]
        if isinstance(_attribute_option_combo, Unset):
            attribute_option_combo = UNSET
        else:
            attribute_option_combo = EventAttributeOptionCombo.from_dict(_attribute_option_combo)

        attribute_values = []
        _attribute_values = d.pop("attributeValues", UNSET)
        for attribute_values_item_data in _attribute_values or []:
            attribute_values_item = AttributeValue.from_dict(attribute_values_item_data)

            attribute_values.append(attribute_values_item)

        code = d.pop("code", UNSET)

        completed = d.pop("completed", UNSET)

        completed_by = d.pop("completedBy", UNSET)

        _completed_date = d.pop("completedDate", UNSET)
        completed_date: Union[Unset, datetime.datetime]
        if isinstance(_completed_date, Unset):
            completed_date = UNSET
        else:
            completed_date = isoparse(_completed_date)

        creatable_in_search_scope = d.pop("creatableInSearchScope", UNSET)

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
        created_by: Union[Unset, EventCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = EventCreatedBy.from_dict(_created_by)

        _created_by_user_info = d.pop("createdByUserInfo", UNSET)
        created_by_user_info: Union[Unset, UserInfoSnapshot]
        if isinstance(_created_by_user_info, Unset):
            created_by_user_info = UNSET
        else:
            created_by_user_info = UserInfoSnapshot.from_dict(_created_by_user_info)

        deleted = d.pop("deleted", UNSET)

        display_name = d.pop("displayName", UNSET)

        _enrollment = d.pop("enrollment", UNSET)
        enrollment: Union[Unset, EventEnrollment]
        if isinstance(_enrollment, Unset):
            enrollment = UNSET
        else:
            enrollment = EventEnrollment.from_dict(_enrollment)

        event_data_values = []
        _event_data_values = d.pop("eventDataValues", UNSET)
        for event_data_values_item_data in _event_data_values or []:
            event_data_values_item = EventDataValue.from_dict(event_data_values_item_data)

            event_data_values.append(event_data_values_item)

        _event_date = d.pop("eventDate", UNSET)
        event_date: Union[Unset, datetime.datetime]
        if isinstance(_event_date, Unset):
            event_date = UNSET
        else:
            event_date = isoparse(_event_date)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        _geometry = d.pop("geometry", UNSET)
        geometry: Union[Unset, EventGeometry]
        if isinstance(_geometry, Unset):
            geometry = UNSET
        else:
            geometry = EventGeometry.from_dict(_geometry)

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
        last_updated_by: Union[Unset, EventLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = EventLastUpdatedBy.from_dict(_last_updated_by)

        _last_updated_by_user_info = d.pop("lastUpdatedByUserInfo", UNSET)
        last_updated_by_user_info: Union[Unset, UserInfoSnapshot]
        if isinstance(_last_updated_by_user_info, Unset):
            last_updated_by_user_info = UNSET
        else:
            last_updated_by_user_info = UserInfoSnapshot.from_dict(_last_updated_by_user_info)

        message_conversations = []
        _message_conversations = d.pop("messageConversations", UNSET)
        for message_conversations_item_data in _message_conversations or []:
            message_conversations_item = EventMessageConversationsItem.from_dict(message_conversations_item_data)

            message_conversations.append(message_conversations_item)

        name = d.pop("name", UNSET)

        notes = []
        _notes = d.pop("notes", UNSET)
        for notes_item_data in _notes or []:
            notes_item = EventNotesItem.from_dict(notes_item_data)

            notes.append(notes_item)

        _organisation_unit = d.pop("organisationUnit", UNSET)
        organisation_unit: Union[Unset, EventOrganisationUnit]
        if isinstance(_organisation_unit, Unset):
            organisation_unit = UNSET
        else:
            organisation_unit = EventOrganisationUnit.from_dict(_organisation_unit)

        _program_stage = d.pop("programStage", UNSET)
        program_stage: Union[Unset, EventProgramStage]
        if isinstance(_program_stage, Unset):
            program_stage = UNSET
        else:
            program_stage = EventProgramStage.from_dict(_program_stage)

        relationship_items = []
        _relationship_items = d.pop("relationshipItems", UNSET)
        for relationship_items_item_data in _relationship_items or []:
            relationship_items_item = RelationshipItem.from_dict(relationship_items_item_data)

            relationship_items.append(relationship_items_item)

        _scheduled_date = d.pop("scheduledDate", UNSET)
        scheduled_date: Union[Unset, datetime.datetime]
        if isinstance(_scheduled_date, Unset):
            scheduled_date = UNSET
        else:
            scheduled_date = isoparse(_scheduled_date)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        stored_by = d.pop("storedBy", UNSET)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, EventUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = EventUser.from_dict(_user)

        event = cls(
            status=status,
            access=access,
            assigned_user=assigned_user,
            attribute_option_combo=attribute_option_combo,
            attribute_values=attribute_values,
            code=code,
            completed=completed,
            completed_by=completed_by,
            completed_date=completed_date,
            creatable_in_search_scope=creatable_in_search_scope,
            created=created,
            created_at_client=created_at_client,
            created_by=created_by,
            created_by_user_info=created_by_user_info,
            deleted=deleted,
            display_name=display_name,
            enrollment=enrollment,
            event_data_values=event_data_values,
            event_date=event_date,
            favorite=favorite,
            favorites=favorites,
            geometry=geometry,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_at_client=last_updated_at_client,
            last_updated_by=last_updated_by,
            last_updated_by_user_info=last_updated_by_user_info,
            message_conversations=message_conversations,
            name=name,
            notes=notes,
            organisation_unit=organisation_unit,
            program_stage=program_stage,
            relationship_items=relationship_items,
            scheduled_date=scheduled_date,
            sharing=sharing,
            stored_by=stored_by,
            translations=translations,
            user=user,
        )

        event.additional_properties = d
        return event

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
