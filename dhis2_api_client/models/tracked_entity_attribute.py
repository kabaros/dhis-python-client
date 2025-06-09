import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.tracked_entity_attribute_aggregation_type import TrackedEntityAttributeAggregationType
from ..models.tracked_entity_attribute_value_type import TrackedEntityAttributeValueType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.object_style import ObjectStyle
    from ..models.query_modifiers import QueryModifiers
    from ..models.sharing import Sharing
    from ..models.tracked_entity_attribute_created_by import TrackedEntityAttributeCreatedBy
    from ..models.tracked_entity_attribute_last_updated_by import TrackedEntityAttributeLastUpdatedBy
    from ..models.tracked_entity_attribute_legend_set import TrackedEntityAttributeLegendSet
    from ..models.tracked_entity_attribute_legend_sets_item import TrackedEntityAttributeLegendSetsItem
    from ..models.tracked_entity_attribute_option_set import TrackedEntityAttributeOptionSet
    from ..models.tracked_entity_attribute_user import TrackedEntityAttributeUser
    from ..models.translation import Translation


T = TypeVar("T", bound="TrackedEntityAttribute")


@_attrs_define
class TrackedEntityAttribute:
    """
    Attributes:
        aggregation_type (TrackedEntityAttributeAggregationType):
        value_type (TrackedEntityAttributeValueType):
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        confidential (Union[Unset, bool]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, TrackedEntityAttributeCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        description (Union[Unset, str]):
        dimension_item (Union[Unset, str]):
        display_description (Union[Unset, str]):
        display_form_name (Union[Unset, str]):
        display_in_list_no_program (Union[Unset, bool]):
        display_name (Union[Unset, str]):
        display_on_visit_schedule (Union[Unset, bool]):
        display_short_name (Union[Unset, str]):
        expression (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        field_mask (Union[Unset, str]):
        form_name (Union[Unset, str]):
        generated (Union[Unset, bool]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        inherit (Union[Unset, bool]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, TrackedEntityAttributeLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        legend_set (Union[Unset, TrackedEntityAttributeLegendSet]): A UID reference to a LegendSet
            (Java name `org.hisp.dhis.legend.LegendSet`)
        legend_sets (Union[Unset, list['TrackedEntityAttributeLegendSetsItem']]):
        name (Union[Unset, str]):
        option_set (Union[Unset, TrackedEntityAttributeOptionSet]): A UID reference to a OptionSet
            (Java name `org.hisp.dhis.option.OptionSet`)
        option_set_value (Union[Unset, bool]):
        orgunit_scope (Union[Unset, bool]):
        pattern (Union[Unset, str]):
        query_mods (Union[Unset, QueryModifiers]):
        sharing (Union[Unset, Sharing]):
        short_name (Union[Unset, str]):
        skip_synchronization (Union[Unset, bool]):
        sort_order_in_list_no_program (Union[Unset, int]):
        sort_order_in_visit_schedule (Union[Unset, int]):
        style (Union[Unset, ObjectStyle]):
        translations (Union[Unset, list['Translation']]):
        unique (Union[Unset, bool]):
        user (Union[Unset, TrackedEntityAttributeUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    aggregation_type: TrackedEntityAttributeAggregationType
    value_type: TrackedEntityAttributeValueType
    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    confidential: Union[Unset, bool] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "TrackedEntityAttributeCreatedBy"] = UNSET
    description: Union[Unset, str] = UNSET
    dimension_item: Union[Unset, str] = UNSET
    display_description: Union[Unset, str] = UNSET
    display_form_name: Union[Unset, str] = UNSET
    display_in_list_no_program: Union[Unset, bool] = UNSET
    display_name: Union[Unset, str] = UNSET
    display_on_visit_schedule: Union[Unset, bool] = UNSET
    display_short_name: Union[Unset, str] = UNSET
    expression: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    field_mask: Union[Unset, str] = UNSET
    form_name: Union[Unset, str] = UNSET
    generated: Union[Unset, bool] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    inherit: Union[Unset, bool] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "TrackedEntityAttributeLastUpdatedBy"] = UNSET
    legend_set: Union[Unset, "TrackedEntityAttributeLegendSet"] = UNSET
    legend_sets: Union[Unset, list["TrackedEntityAttributeLegendSetsItem"]] = UNSET
    name: Union[Unset, str] = UNSET
    option_set: Union[Unset, "TrackedEntityAttributeOptionSet"] = UNSET
    option_set_value: Union[Unset, bool] = UNSET
    orgunit_scope: Union[Unset, bool] = UNSET
    pattern: Union[Unset, str] = UNSET
    query_mods: Union[Unset, "QueryModifiers"] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    short_name: Union[Unset, str] = UNSET
    skip_synchronization: Union[Unset, bool] = UNSET
    sort_order_in_list_no_program: Union[Unset, int] = UNSET
    sort_order_in_visit_schedule: Union[Unset, int] = UNSET
    style: Union[Unset, "ObjectStyle"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    unique: Union[Unset, bool] = UNSET
    user: Union[Unset, "TrackedEntityAttributeUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregation_type = self.aggregation_type.value

        value_type = self.value_type.value

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

        confidential = self.confidential

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        description = self.description

        dimension_item = self.dimension_item

        display_description = self.display_description

        display_form_name = self.display_form_name

        display_in_list_no_program = self.display_in_list_no_program

        display_name = self.display_name

        display_on_visit_schedule = self.display_on_visit_schedule

        display_short_name = self.display_short_name

        expression = self.expression

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        field_mask = self.field_mask

        form_name = self.form_name

        generated = self.generated

        href = self.href

        id = self.id

        inherit = self.inherit

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        legend_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.legend_set, Unset):
            legend_set = self.legend_set.to_dict()

        legend_sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.legend_sets, Unset):
            legend_sets = []
            for legend_sets_item_data in self.legend_sets:
                legend_sets_item = legend_sets_item_data.to_dict()
                legend_sets.append(legend_sets_item)

        name = self.name

        option_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.option_set, Unset):
            option_set = self.option_set.to_dict()

        option_set_value = self.option_set_value

        orgunit_scope = self.orgunit_scope

        pattern = self.pattern

        query_mods: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.query_mods, Unset):
            query_mods = self.query_mods.to_dict()

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        short_name = self.short_name

        skip_synchronization = self.skip_synchronization

        sort_order_in_list_no_program = self.sort_order_in_list_no_program

        sort_order_in_visit_schedule = self.sort_order_in_visit_schedule

        style: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.style, Unset):
            style = self.style.to_dict()

        translations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        unique = self.unique

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aggregationType": aggregation_type,
                "valueType": value_type,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if code is not UNSET:
            field_dict["code"] = code
        if confidential is not UNSET:
            field_dict["confidential"] = confidential
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if dimension_item is not UNSET:
            field_dict["dimensionItem"] = dimension_item
        if display_description is not UNSET:
            field_dict["displayDescription"] = display_description
        if display_form_name is not UNSET:
            field_dict["displayFormName"] = display_form_name
        if display_in_list_no_program is not UNSET:
            field_dict["displayInListNoProgram"] = display_in_list_no_program
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_on_visit_schedule is not UNSET:
            field_dict["displayOnVisitSchedule"] = display_on_visit_schedule
        if display_short_name is not UNSET:
            field_dict["displayShortName"] = display_short_name
        if expression is not UNSET:
            field_dict["expression"] = expression
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if field_mask is not UNSET:
            field_dict["fieldMask"] = field_mask
        if form_name is not UNSET:
            field_dict["formName"] = form_name
        if generated is not UNSET:
            field_dict["generated"] = generated
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if inherit is not UNSET:
            field_dict["inherit"] = inherit
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if legend_set is not UNSET:
            field_dict["legendSet"] = legend_set
        if legend_sets is not UNSET:
            field_dict["legendSets"] = legend_sets
        if name is not UNSET:
            field_dict["name"] = name
        if option_set is not UNSET:
            field_dict["optionSet"] = option_set
        if option_set_value is not UNSET:
            field_dict["optionSetValue"] = option_set_value
        if orgunit_scope is not UNSET:
            field_dict["orgunitScope"] = orgunit_scope
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if query_mods is not UNSET:
            field_dict["queryMods"] = query_mods
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if skip_synchronization is not UNSET:
            field_dict["skipSynchronization"] = skip_synchronization
        if sort_order_in_list_no_program is not UNSET:
            field_dict["sortOrderInListNoProgram"] = sort_order_in_list_no_program
        if sort_order_in_visit_schedule is not UNSET:
            field_dict["sortOrderInVisitSchedule"] = sort_order_in_visit_schedule
        if style is not UNSET:
            field_dict["style"] = style
        if translations is not UNSET:
            field_dict["translations"] = translations
        if unique is not UNSET:
            field_dict["unique"] = unique
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.object_style import ObjectStyle
        from ..models.query_modifiers import QueryModifiers
        from ..models.sharing import Sharing
        from ..models.tracked_entity_attribute_created_by import TrackedEntityAttributeCreatedBy
        from ..models.tracked_entity_attribute_last_updated_by import TrackedEntityAttributeLastUpdatedBy
        from ..models.tracked_entity_attribute_legend_set import TrackedEntityAttributeLegendSet
        from ..models.tracked_entity_attribute_legend_sets_item import TrackedEntityAttributeLegendSetsItem
        from ..models.tracked_entity_attribute_option_set import TrackedEntityAttributeOptionSet
        from ..models.tracked_entity_attribute_user import TrackedEntityAttributeUser
        from ..models.translation import Translation

        d = src_dict.copy()
        aggregation_type = TrackedEntityAttributeAggregationType(d.pop("aggregationType"))

        value_type = TrackedEntityAttributeValueType(d.pop("valueType"))

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

        confidential = d.pop("confidential", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, TrackedEntityAttributeCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = TrackedEntityAttributeCreatedBy.from_dict(_created_by)

        description = d.pop("description", UNSET)

        dimension_item = d.pop("dimensionItem", UNSET)

        display_description = d.pop("displayDescription", UNSET)

        display_form_name = d.pop("displayFormName", UNSET)

        display_in_list_no_program = d.pop("displayInListNoProgram", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_on_visit_schedule = d.pop("displayOnVisitSchedule", UNSET)

        display_short_name = d.pop("displayShortName", UNSET)

        expression = d.pop("expression", UNSET)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        field_mask = d.pop("fieldMask", UNSET)

        form_name = d.pop("formName", UNSET)

        generated = d.pop("generated", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        inherit = d.pop("inherit", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, TrackedEntityAttributeLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = TrackedEntityAttributeLastUpdatedBy.from_dict(_last_updated_by)

        _legend_set = d.pop("legendSet", UNSET)
        legend_set: Union[Unset, TrackedEntityAttributeLegendSet]
        if isinstance(_legend_set, Unset):
            legend_set = UNSET
        else:
            legend_set = TrackedEntityAttributeLegendSet.from_dict(_legend_set)

        legend_sets = []
        _legend_sets = d.pop("legendSets", UNSET)
        for legend_sets_item_data in _legend_sets or []:
            legend_sets_item = TrackedEntityAttributeLegendSetsItem.from_dict(legend_sets_item_data)

            legend_sets.append(legend_sets_item)

        name = d.pop("name", UNSET)

        _option_set = d.pop("optionSet", UNSET)
        option_set: Union[Unset, TrackedEntityAttributeOptionSet]
        if isinstance(_option_set, Unset):
            option_set = UNSET
        else:
            option_set = TrackedEntityAttributeOptionSet.from_dict(_option_set)

        option_set_value = d.pop("optionSetValue", UNSET)

        orgunit_scope = d.pop("orgunitScope", UNSET)

        pattern = d.pop("pattern", UNSET)

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

        skip_synchronization = d.pop("skipSynchronization", UNSET)

        sort_order_in_list_no_program = d.pop("sortOrderInListNoProgram", UNSET)

        sort_order_in_visit_schedule = d.pop("sortOrderInVisitSchedule", UNSET)

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

        unique = d.pop("unique", UNSET)

        _user = d.pop("user", UNSET)
        user: Union[Unset, TrackedEntityAttributeUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = TrackedEntityAttributeUser.from_dict(_user)

        tracked_entity_attribute = cls(
            aggregation_type=aggregation_type,
            value_type=value_type,
            access=access,
            attribute_values=attribute_values,
            code=code,
            confidential=confidential,
            created=created,
            created_by=created_by,
            description=description,
            dimension_item=dimension_item,
            display_description=display_description,
            display_form_name=display_form_name,
            display_in_list_no_program=display_in_list_no_program,
            display_name=display_name,
            display_on_visit_schedule=display_on_visit_schedule,
            display_short_name=display_short_name,
            expression=expression,
            favorite=favorite,
            favorites=favorites,
            field_mask=field_mask,
            form_name=form_name,
            generated=generated,
            href=href,
            id=id,
            inherit=inherit,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            legend_set=legend_set,
            legend_sets=legend_sets,
            name=name,
            option_set=option_set,
            option_set_value=option_set_value,
            orgunit_scope=orgunit_scope,
            pattern=pattern,
            query_mods=query_mods,
            sharing=sharing,
            short_name=short_name,
            skip_synchronization=skip_synchronization,
            sort_order_in_list_no_program=sort_order_in_list_no_program,
            sort_order_in_visit_schedule=sort_order_in_visit_schedule,
            style=style,
            translations=translations,
            unique=unique,
            user=user,
        )

        tracked_entity_attribute.additional_properties = d
        return tracked_entity_attribute

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
