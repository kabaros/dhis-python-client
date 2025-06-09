import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.tracked_entity_filter_enrollment_status import TrackedEntityFilterEnrollmentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.entity_query_criteria import EntityQueryCriteria
    from ..models.event_filter_info import EventFilterInfo
    from ..models.filter_period import FilterPeriod
    from ..models.object_style import ObjectStyle
    from ..models.sharing import Sharing
    from ..models.tracked_entity_filter_created_by import TrackedEntityFilterCreatedBy
    from ..models.tracked_entity_filter_last_updated_by import TrackedEntityFilterLastUpdatedBy
    from ..models.tracked_entity_filter_program import TrackedEntityFilterProgram
    from ..models.tracked_entity_filter_user import TrackedEntityFilterUser
    from ..models.translation import Translation


T = TypeVar("T", bound="TrackedEntityFilter")


@_attrs_define
class TrackedEntityFilter:
    """
    Attributes:
        enrollment_status (TrackedEntityFilterEnrollmentStatus):
        sort_order (int):
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, TrackedEntityFilterCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        description (Union[Unset, str]):
        display_description (Union[Unset, str]):
        display_name (Union[Unset, str]):
        enrollment_created_period (Union[Unset, FilterPeriod]):
        entity_query_criteria (Union[Unset, EntityQueryCriteria]):
        event_filters (Union[Unset, list['EventFilterInfo']]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        followup (Union[Unset, bool]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, TrackedEntityFilterLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        name (Union[Unset, str]):
        program (Union[Unset, TrackedEntityFilterProgram]): A UID reference to a Program
            (Java name `org.hisp.dhis.program.Program`)
        sharing (Union[Unset, Sharing]):
        style (Union[Unset, ObjectStyle]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, TrackedEntityFilterUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    enrollment_status: TrackedEntityFilterEnrollmentStatus
    sort_order: int
    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "TrackedEntityFilterCreatedBy"] = UNSET
    description: Union[Unset, str] = UNSET
    display_description: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    enrollment_created_period: Union[Unset, "FilterPeriod"] = UNSET
    entity_query_criteria: Union[Unset, "EntityQueryCriteria"] = UNSET
    event_filters: Union[Unset, list["EventFilterInfo"]] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    followup: Union[Unset, bool] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "TrackedEntityFilterLastUpdatedBy"] = UNSET
    name: Union[Unset, str] = UNSET
    program: Union[Unset, "TrackedEntityFilterProgram"] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    style: Union[Unset, "ObjectStyle"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "TrackedEntityFilterUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enrollment_status = self.enrollment_status.value

        sort_order = self.sort_order

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

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        description = self.description

        display_description = self.display_description

        display_name = self.display_name

        enrollment_created_period: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.enrollment_created_period, Unset):
            enrollment_created_period = self.enrollment_created_period.to_dict()

        entity_query_criteria: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entity_query_criteria, Unset):
            entity_query_criteria = self.entity_query_criteria.to_dict()

        event_filters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.event_filters, Unset):
            event_filters = []
            for event_filters_item_data in self.event_filters:
                event_filters_item = event_filters_item_data.to_dict()
                event_filters.append(event_filters_item)

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        followup = self.followup

        href = self.href

        id = self.id

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        name = self.name

        program: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program, Unset):
            program = self.program.to_dict()

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        style: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.style, Unset):
            style = self.style.to_dict()

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
                "enrollmentStatus": enrollment_status,
                "sortOrder": sort_order,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if code is not UNSET:
            field_dict["code"] = code
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if display_description is not UNSET:
            field_dict["displayDescription"] = display_description
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if enrollment_created_period is not UNSET:
            field_dict["enrollmentCreatedPeriod"] = enrollment_created_period
        if entity_query_criteria is not UNSET:
            field_dict["entityQueryCriteria"] = entity_query_criteria
        if event_filters is not UNSET:
            field_dict["eventFilters"] = event_filters
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if followup is not UNSET:
            field_dict["followup"] = followup
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if name is not UNSET:
            field_dict["name"] = name
        if program is not UNSET:
            field_dict["program"] = program
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if style is not UNSET:
            field_dict["style"] = style
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.entity_query_criteria import EntityQueryCriteria
        from ..models.event_filter_info import EventFilterInfo
        from ..models.filter_period import FilterPeriod
        from ..models.object_style import ObjectStyle
        from ..models.sharing import Sharing
        from ..models.tracked_entity_filter_created_by import TrackedEntityFilterCreatedBy
        from ..models.tracked_entity_filter_last_updated_by import TrackedEntityFilterLastUpdatedBy
        from ..models.tracked_entity_filter_program import TrackedEntityFilterProgram
        from ..models.tracked_entity_filter_user import TrackedEntityFilterUser
        from ..models.translation import Translation

        d = src_dict.copy()
        enrollment_status = TrackedEntityFilterEnrollmentStatus(d.pop("enrollmentStatus"))

        sort_order = d.pop("sortOrder")

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

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, TrackedEntityFilterCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = TrackedEntityFilterCreatedBy.from_dict(_created_by)

        description = d.pop("description", UNSET)

        display_description = d.pop("displayDescription", UNSET)

        display_name = d.pop("displayName", UNSET)

        _enrollment_created_period = d.pop("enrollmentCreatedPeriod", UNSET)
        enrollment_created_period: Union[Unset, FilterPeriod]
        if isinstance(_enrollment_created_period, Unset):
            enrollment_created_period = UNSET
        else:
            enrollment_created_period = FilterPeriod.from_dict(_enrollment_created_period)

        _entity_query_criteria = d.pop("entityQueryCriteria", UNSET)
        entity_query_criteria: Union[Unset, EntityQueryCriteria]
        if isinstance(_entity_query_criteria, Unset):
            entity_query_criteria = UNSET
        else:
            entity_query_criteria = EntityQueryCriteria.from_dict(_entity_query_criteria)

        event_filters = []
        _event_filters = d.pop("eventFilters", UNSET)
        for event_filters_item_data in _event_filters or []:
            event_filters_item = EventFilterInfo.from_dict(event_filters_item_data)

            event_filters.append(event_filters_item)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        followup = d.pop("followup", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, TrackedEntityFilterLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = TrackedEntityFilterLastUpdatedBy.from_dict(_last_updated_by)

        name = d.pop("name", UNSET)

        _program = d.pop("program", UNSET)
        program: Union[Unset, TrackedEntityFilterProgram]
        if isinstance(_program, Unset):
            program = UNSET
        else:
            program = TrackedEntityFilterProgram.from_dict(_program)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        _style = d.pop("style", UNSET)
        style: Union[Unset, ObjectStyle]
        if isinstance(_style, Unset):
            style = UNSET
        else:
            style = ObjectStyle.from_dict(_style)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, TrackedEntityFilterUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = TrackedEntityFilterUser.from_dict(_user)

        tracked_entity_filter = cls(
            enrollment_status=enrollment_status,
            sort_order=sort_order,
            access=access,
            attribute_values=attribute_values,
            code=code,
            created=created,
            created_by=created_by,
            description=description,
            display_description=display_description,
            display_name=display_name,
            enrollment_created_period=enrollment_created_period,
            entity_query_criteria=entity_query_criteria,
            event_filters=event_filters,
            favorite=favorite,
            favorites=favorites,
            followup=followup,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            name=name,
            program=program,
            sharing=sharing,
            style=style,
            translations=translations,
            user=user,
        )

        tracked_entity_filter.additional_properties = d
        return tracked_entity_filter

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
