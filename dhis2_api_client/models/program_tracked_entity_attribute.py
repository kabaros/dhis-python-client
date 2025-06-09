import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.program_tracked_entity_attribute_value_type import ProgramTrackedEntityAttributeValueType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.program_tracked_entity_attribute_created_by import ProgramTrackedEntityAttributeCreatedBy
    from ..models.program_tracked_entity_attribute_last_updated_by import ProgramTrackedEntityAttributeLastUpdatedBy
    from ..models.program_tracked_entity_attribute_program import ProgramTrackedEntityAttributeProgram
    from ..models.program_tracked_entity_attribute_tracked_entity_attribute import (
        ProgramTrackedEntityAttributeTrackedEntityAttribute,
    )
    from ..models.program_tracked_entity_attribute_user import ProgramTrackedEntityAttributeUser
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="ProgramTrackedEntityAttribute")


@_attrs_define
class ProgramTrackedEntityAttribute:
    """
    Attributes:
        value_type (ProgramTrackedEntityAttributeValueType):
        access (Union[Unset, Access]):
        allow_future_date (Union[Unset, bool]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, ProgramTrackedEntityAttributeCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        display_in_list (Union[Unset, bool]):
        display_name (Union[Unset, str]):
        display_short_name (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, ProgramTrackedEntityAttributeLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        mandatory (Union[Unset, bool]):
        program (Union[Unset, ProgramTrackedEntityAttributeProgram]): A UID reference to a Program
            (Java name `org.hisp.dhis.program.Program`)
        render_options_as_radio (Union[Unset, bool]):
        render_type (Union[Unset, Any]): The exact type is unknown.
            (Java type was: `org.hisp.dhis.render.DeviceRenderTypeMap<org.hisp.dhis.render.type.ValueTypeRenderingObject>`)
        searchable (Union[Unset, bool]):
        sharing (Union[Unset, Sharing]):
        sort_order (Union[Unset, int]):
        tracked_entity_attribute (Union[Unset, ProgramTrackedEntityAttributeTrackedEntityAttribute]): A UID reference to
            a TrackedEntityAttribute
            (Java name `org.hisp.dhis.trackedentity.TrackedEntityAttribute`)
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, ProgramTrackedEntityAttributeUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    value_type: ProgramTrackedEntityAttributeValueType
    access: Union[Unset, "Access"] = UNSET
    allow_future_date: Union[Unset, bool] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "ProgramTrackedEntityAttributeCreatedBy"] = UNSET
    display_in_list: Union[Unset, bool] = UNSET
    display_name: Union[Unset, str] = UNSET
    display_short_name: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "ProgramTrackedEntityAttributeLastUpdatedBy"] = UNSET
    mandatory: Union[Unset, bool] = UNSET
    program: Union[Unset, "ProgramTrackedEntityAttributeProgram"] = UNSET
    render_options_as_radio: Union[Unset, bool] = UNSET
    render_type: Union[Unset, Any] = UNSET
    searchable: Union[Unset, bool] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    sort_order: Union[Unset, int] = UNSET
    tracked_entity_attribute: Union[Unset, "ProgramTrackedEntityAttributeTrackedEntityAttribute"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "ProgramTrackedEntityAttributeUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value_type = self.value_type.value

        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        allow_future_date = self.allow_future_date

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

        display_in_list = self.display_in_list

        display_name = self.display_name

        display_short_name = self.display_short_name

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        href = self.href

        id = self.id

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        mandatory = self.mandatory

        program: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program, Unset):
            program = self.program.to_dict()

        render_options_as_radio = self.render_options_as_radio

        render_type = self.render_type

        searchable = self.searchable

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        sort_order = self.sort_order

        tracked_entity_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tracked_entity_attribute, Unset):
            tracked_entity_attribute = self.tracked_entity_attribute.to_dict()

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
                "valueType": value_type,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if allow_future_date is not UNSET:
            field_dict["allowFutureDate"] = allow_future_date
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if code is not UNSET:
            field_dict["code"] = code
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if display_in_list is not UNSET:
            field_dict["displayInList"] = display_in_list
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_short_name is not UNSET:
            field_dict["displayShortName"] = display_short_name
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if mandatory is not UNSET:
            field_dict["mandatory"] = mandatory
        if program is not UNSET:
            field_dict["program"] = program
        if render_options_as_radio is not UNSET:
            field_dict["renderOptionsAsRadio"] = render_options_as_radio
        if render_type is not UNSET:
            field_dict["renderType"] = render_type
        if searchable is not UNSET:
            field_dict["searchable"] = searchable
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if tracked_entity_attribute is not UNSET:
            field_dict["trackedEntityAttribute"] = tracked_entity_attribute
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.program_tracked_entity_attribute_created_by import ProgramTrackedEntityAttributeCreatedBy
        from ..models.program_tracked_entity_attribute_last_updated_by import ProgramTrackedEntityAttributeLastUpdatedBy
        from ..models.program_tracked_entity_attribute_program import ProgramTrackedEntityAttributeProgram
        from ..models.program_tracked_entity_attribute_tracked_entity_attribute import (
            ProgramTrackedEntityAttributeTrackedEntityAttribute,
        )
        from ..models.program_tracked_entity_attribute_user import ProgramTrackedEntityAttributeUser
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        value_type = ProgramTrackedEntityAttributeValueType(d.pop("valueType"))

        _access = d.pop("access", UNSET)
        access: Union[Unset, Access]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

        allow_future_date = d.pop("allowFutureDate", UNSET)

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
        created_by: Union[Unset, ProgramTrackedEntityAttributeCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = ProgramTrackedEntityAttributeCreatedBy.from_dict(_created_by)

        display_in_list = d.pop("displayInList", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_short_name = d.pop("displayShortName", UNSET)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, ProgramTrackedEntityAttributeLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = ProgramTrackedEntityAttributeLastUpdatedBy.from_dict(_last_updated_by)

        mandatory = d.pop("mandatory", UNSET)

        _program = d.pop("program", UNSET)
        program: Union[Unset, ProgramTrackedEntityAttributeProgram]
        if isinstance(_program, Unset):
            program = UNSET
        else:
            program = ProgramTrackedEntityAttributeProgram.from_dict(_program)

        render_options_as_radio = d.pop("renderOptionsAsRadio", UNSET)

        render_type = d.pop("renderType", UNSET)

        searchable = d.pop("searchable", UNSET)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        sort_order = d.pop("sortOrder", UNSET)

        _tracked_entity_attribute = d.pop("trackedEntityAttribute", UNSET)
        tracked_entity_attribute: Union[Unset, ProgramTrackedEntityAttributeTrackedEntityAttribute]
        if isinstance(_tracked_entity_attribute, Unset):
            tracked_entity_attribute = UNSET
        else:
            tracked_entity_attribute = ProgramTrackedEntityAttributeTrackedEntityAttribute.from_dict(
                _tracked_entity_attribute
            )

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, ProgramTrackedEntityAttributeUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ProgramTrackedEntityAttributeUser.from_dict(_user)

        program_tracked_entity_attribute = cls(
            value_type=value_type,
            access=access,
            allow_future_date=allow_future_date,
            attribute_values=attribute_values,
            code=code,
            created=created,
            created_by=created_by,
            display_in_list=display_in_list,
            display_name=display_name,
            display_short_name=display_short_name,
            favorite=favorite,
            favorites=favorites,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            mandatory=mandatory,
            program=program,
            render_options_as_radio=render_options_as_radio,
            render_type=render_type,
            searchable=searchable,
            sharing=sharing,
            sort_order=sort_order,
            tracked_entity_attribute=tracked_entity_attribute,
            translations=translations,
            user=user,
        )

        program_tracked_entity_attribute.additional_properties = d
        return program_tracked_entity_attribute

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
