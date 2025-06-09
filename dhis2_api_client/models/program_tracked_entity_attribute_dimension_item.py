import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.program_tracked_entity_attribute_dimension_item_attribute import (
        ProgramTrackedEntityAttributeDimensionItemAttribute,
    )
    from ..models.program_tracked_entity_attribute_dimension_item_created_by import (
        ProgramTrackedEntityAttributeDimensionItemCreatedBy,
    )
    from ..models.program_tracked_entity_attribute_dimension_item_last_updated_by import (
        ProgramTrackedEntityAttributeDimensionItemLastUpdatedBy,
    )
    from ..models.program_tracked_entity_attribute_dimension_item_legend_set import (
        ProgramTrackedEntityAttributeDimensionItemLegendSet,
    )
    from ..models.program_tracked_entity_attribute_dimension_item_program import (
        ProgramTrackedEntityAttributeDimensionItemProgram,
    )
    from ..models.program_tracked_entity_attribute_dimension_item_user import (
        ProgramTrackedEntityAttributeDimensionItemUser,
    )
    from ..models.query_modifiers import QueryModifiers
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="ProgramTrackedEntityAttributeDimensionItem")


@_attrs_define
class ProgramTrackedEntityAttributeDimensionItem:
    """
    Attributes:
        access (Union[Unset, Access]):
        attribute (Union[Unset, ProgramTrackedEntityAttributeDimensionItemAttribute]): A UID reference to a
            TrackedEntityAttribute
            (Java name `org.hisp.dhis.trackedentity.TrackedEntityAttribute`)
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, ProgramTrackedEntityAttributeDimensionItemCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        description (Union[Unset, str]):
        display_description (Union[Unset, str]):
        display_form_name (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        form_name (Union[Unset, str]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, ProgramTrackedEntityAttributeDimensionItemLastUpdatedBy]): A UID reference to a
            User
            (Java name `org.hisp.dhis.user.User`)
        legend_set (Union[Unset, ProgramTrackedEntityAttributeDimensionItemLegendSet]): A UID reference to a LegendSet
            (Java name `org.hisp.dhis.legend.LegendSet`)
        program (Union[Unset, ProgramTrackedEntityAttributeDimensionItemProgram]): A UID reference to a Program
            (Java name `org.hisp.dhis.program.Program`)
        query_mods (Union[Unset, QueryModifiers]):
        sharing (Union[Unset, Sharing]):
        short_name (Union[Unset, str]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, ProgramTrackedEntityAttributeDimensionItemUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    access: Union[Unset, "Access"] = UNSET
    attribute: Union[Unset, "ProgramTrackedEntityAttributeDimensionItemAttribute"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "ProgramTrackedEntityAttributeDimensionItemCreatedBy"] = UNSET
    description: Union[Unset, str] = UNSET
    display_description: Union[Unset, str] = UNSET
    display_form_name: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    form_name: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "ProgramTrackedEntityAttributeDimensionItemLastUpdatedBy"] = UNSET
    legend_set: Union[Unset, "ProgramTrackedEntityAttributeDimensionItemLegendSet"] = UNSET
    program: Union[Unset, "ProgramTrackedEntityAttributeDimensionItemProgram"] = UNSET
    query_mods: Union[Unset, "QueryModifiers"] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    short_name: Union[Unset, str] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "ProgramTrackedEntityAttributeDimensionItemUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attribute, Unset):
            attribute = self.attribute.to_dict()

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

        legend_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.legend_set, Unset):
            legend_set = self.legend_set.to_dict()

        program: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program, Unset):
            program = self.program.to_dict()

        query_mods: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.query_mods, Unset):
            query_mods = self.query_mods.to_dict()

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        short_name = self.short_name

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
        if attribute is not UNSET:
            field_dict["attribute"] = attribute
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
        if legend_set is not UNSET:
            field_dict["legendSet"] = legend_set
        if program is not UNSET:
            field_dict["program"] = program
        if query_mods is not UNSET:
            field_dict["queryMods"] = query_mods
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.program_tracked_entity_attribute_dimension_item_attribute import (
            ProgramTrackedEntityAttributeDimensionItemAttribute,
        )
        from ..models.program_tracked_entity_attribute_dimension_item_created_by import (
            ProgramTrackedEntityAttributeDimensionItemCreatedBy,
        )
        from ..models.program_tracked_entity_attribute_dimension_item_last_updated_by import (
            ProgramTrackedEntityAttributeDimensionItemLastUpdatedBy,
        )
        from ..models.program_tracked_entity_attribute_dimension_item_legend_set import (
            ProgramTrackedEntityAttributeDimensionItemLegendSet,
        )
        from ..models.program_tracked_entity_attribute_dimension_item_program import (
            ProgramTrackedEntityAttributeDimensionItemProgram,
        )
        from ..models.program_tracked_entity_attribute_dimension_item_user import (
            ProgramTrackedEntityAttributeDimensionItemUser,
        )
        from ..models.query_modifiers import QueryModifiers
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        _access = d.pop("access", UNSET)
        access: Union[Unset, Access]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

        _attribute = d.pop("attribute", UNSET)
        attribute: Union[Unset, ProgramTrackedEntityAttributeDimensionItemAttribute]
        if isinstance(_attribute, Unset):
            attribute = UNSET
        else:
            attribute = ProgramTrackedEntityAttributeDimensionItemAttribute.from_dict(_attribute)

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
        created_by: Union[Unset, ProgramTrackedEntityAttributeDimensionItemCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = ProgramTrackedEntityAttributeDimensionItemCreatedBy.from_dict(_created_by)

        description = d.pop("description", UNSET)

        display_description = d.pop("displayDescription", UNSET)

        display_form_name = d.pop("displayFormName", UNSET)

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
        last_updated_by: Union[Unset, ProgramTrackedEntityAttributeDimensionItemLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = ProgramTrackedEntityAttributeDimensionItemLastUpdatedBy.from_dict(_last_updated_by)

        _legend_set = d.pop("legendSet", UNSET)
        legend_set: Union[Unset, ProgramTrackedEntityAttributeDimensionItemLegendSet]
        if isinstance(_legend_set, Unset):
            legend_set = UNSET
        else:
            legend_set = ProgramTrackedEntityAttributeDimensionItemLegendSet.from_dict(_legend_set)

        _program = d.pop("program", UNSET)
        program: Union[Unset, ProgramTrackedEntityAttributeDimensionItemProgram]
        if isinstance(_program, Unset):
            program = UNSET
        else:
            program = ProgramTrackedEntityAttributeDimensionItemProgram.from_dict(_program)

        _query_mods = d.pop("queryMods", UNSET)
        query_mods: Union[Unset, QueryModifiers]
        if isinstance(_query_mods, Unset):
            query_mods = UNSET
        else:
            query_mods = QueryModifiers.from_dict(_query_mods)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        short_name = d.pop("shortName", UNSET)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, ProgramTrackedEntityAttributeDimensionItemUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ProgramTrackedEntityAttributeDimensionItemUser.from_dict(_user)

        program_tracked_entity_attribute_dimension_item = cls(
            access=access,
            attribute=attribute,
            attribute_values=attribute_values,
            code=code,
            created=created,
            created_by=created_by,
            description=description,
            display_description=display_description,
            display_form_name=display_form_name,
            favorite=favorite,
            favorites=favorites,
            form_name=form_name,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            legend_set=legend_set,
            program=program,
            query_mods=query_mods,
            sharing=sharing,
            short_name=short_name,
            translations=translations,
            user=user,
        )

        program_tracked_entity_attribute_dimension_item.additional_properties = d
        return program_tracked_entity_attribute_dimension_item

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
