import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.object_style import ObjectStyle
    from ..models.program_section_created_by import ProgramSectionCreatedBy
    from ..models.program_section_last_updated_by import ProgramSectionLastUpdatedBy
    from ..models.program_section_program import ProgramSectionProgram
    from ..models.program_section_tracked_entity_attributes_item import ProgramSectionTrackedEntityAttributesItem
    from ..models.program_section_user import ProgramSectionUser
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="ProgramSection")


@_attrs_define
class ProgramSection:
    """
    Attributes:
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, ProgramSectionCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        description (Union[Unset, str]):
        display_description (Union[Unset, str]):
        display_form_name (Union[Unset, str]):
        display_name (Union[Unset, str]):
        display_short_name (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        form_name (Union[Unset, str]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, ProgramSectionLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        name (Union[Unset, str]):
        program (Union[Unset, ProgramSectionProgram]): A UID reference to a Program
            (Java name `org.hisp.dhis.program.Program`)
        render_type (Union[Unset, Any]): The exact type is unknown.
            (Java type was: `org.hisp.dhis.render.DeviceRenderTypeMap<org.hisp.dhis.render.type.SectionRenderingObject>`)
        sharing (Union[Unset, Sharing]):
        short_name (Union[Unset, str]):
        sort_order (Union[Unset, int]):
        style (Union[Unset, ObjectStyle]):
        tracked_entity_attributes (Union[Unset, list['ProgramSectionTrackedEntityAttributesItem']]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, ProgramSectionUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "ProgramSectionCreatedBy"] = UNSET
    description: Union[Unset, str] = UNSET
    display_description: Union[Unset, str] = UNSET
    display_form_name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    display_short_name: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    form_name: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "ProgramSectionLastUpdatedBy"] = UNSET
    name: Union[Unset, str] = UNSET
    program: Union[Unset, "ProgramSectionProgram"] = UNSET
    render_type: Union[Unset, Any] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    short_name: Union[Unset, str] = UNSET
    sort_order: Union[Unset, int] = UNSET
    style: Union[Unset, "ObjectStyle"] = UNSET
    tracked_entity_attributes: Union[Unset, list["ProgramSectionTrackedEntityAttributesItem"]] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "ProgramSectionUser"] = UNSET
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

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        description = self.description

        display_description = self.display_description

        display_form_name = self.display_form_name

        display_name = self.display_name

        display_short_name = self.display_short_name

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        form_name = self.form_name

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

        render_type = self.render_type

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        short_name = self.short_name

        sort_order = self.sort_order

        style: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.style, Unset):
            style = self.style.to_dict()

        tracked_entity_attributes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tracked_entity_attributes, Unset):
            tracked_entity_attributes = []
            for tracked_entity_attributes_item_data in self.tracked_entity_attributes:
                tracked_entity_attributes_item = tracked_entity_attributes_item_data.to_dict()
                tracked_entity_attributes.append(tracked_entity_attributes_item)

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
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if display_description is not UNSET:
            field_dict["displayDescription"] = display_description
        if display_form_name is not UNSET:
            field_dict["displayFormName"] = display_form_name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_short_name is not UNSET:
            field_dict["displayShortName"] = display_short_name
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if form_name is not UNSET:
            field_dict["formName"] = form_name
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
        if render_type is not UNSET:
            field_dict["renderType"] = render_type
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if style is not UNSET:
            field_dict["style"] = style
        if tracked_entity_attributes is not UNSET:
            field_dict["trackedEntityAttributes"] = tracked_entity_attributes
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.object_style import ObjectStyle
        from ..models.program_section_created_by import ProgramSectionCreatedBy
        from ..models.program_section_last_updated_by import ProgramSectionLastUpdatedBy
        from ..models.program_section_program import ProgramSectionProgram
        from ..models.program_section_tracked_entity_attributes_item import ProgramSectionTrackedEntityAttributesItem
        from ..models.program_section_user import ProgramSectionUser
        from ..models.sharing import Sharing
        from ..models.translation import Translation

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

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, ProgramSectionCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = ProgramSectionCreatedBy.from_dict(_created_by)

        description = d.pop("description", UNSET)

        display_description = d.pop("displayDescription", UNSET)

        display_form_name = d.pop("displayFormName", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_short_name = d.pop("displayShortName", UNSET)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        form_name = d.pop("formName", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, ProgramSectionLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = ProgramSectionLastUpdatedBy.from_dict(_last_updated_by)

        name = d.pop("name", UNSET)

        _program = d.pop("program", UNSET)
        program: Union[Unset, ProgramSectionProgram]
        if isinstance(_program, Unset):
            program = UNSET
        else:
            program = ProgramSectionProgram.from_dict(_program)

        render_type = d.pop("renderType", UNSET)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        short_name = d.pop("shortName", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        _style = d.pop("style", UNSET)
        style: Union[Unset, ObjectStyle]
        if isinstance(_style, Unset):
            style = UNSET
        else:
            style = ObjectStyle.from_dict(_style)

        tracked_entity_attributes = []
        _tracked_entity_attributes = d.pop("trackedEntityAttributes", UNSET)
        for tracked_entity_attributes_item_data in _tracked_entity_attributes or []:
            tracked_entity_attributes_item = ProgramSectionTrackedEntityAttributesItem.from_dict(
                tracked_entity_attributes_item_data
            )

            tracked_entity_attributes.append(tracked_entity_attributes_item)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, ProgramSectionUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ProgramSectionUser.from_dict(_user)

        program_section = cls(
            access=access,
            attribute_values=attribute_values,
            code=code,
            created=created,
            created_by=created_by,
            description=description,
            display_description=display_description,
            display_form_name=display_form_name,
            display_name=display_name,
            display_short_name=display_short_name,
            favorite=favorite,
            favorites=favorites,
            form_name=form_name,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            name=name,
            program=program,
            render_type=render_type,
            sharing=sharing,
            short_name=short_name,
            sort_order=sort_order,
            style=style,
            tracked_entity_attributes=tracked_entity_attributes,
            translations=translations,
            user=user,
        )

        program_section.additional_properties = d
        return program_section

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
