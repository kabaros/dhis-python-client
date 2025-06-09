import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.category_option_aggregation_type import CategoryOptionAggregationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.category_option_categories_item import CategoryOptionCategoriesItem
    from ..models.category_option_category_option_combos_item import CategoryOptionCategoryOptionCombosItem
    from ..models.category_option_category_option_groups_item import CategoryOptionCategoryOptionGroupsItem
    from ..models.category_option_created_by import CategoryOptionCreatedBy
    from ..models.category_option_last_updated_by import CategoryOptionLastUpdatedBy
    from ..models.category_option_legend_set import CategoryOptionLegendSet
    from ..models.category_option_legend_sets_item import CategoryOptionLegendSetsItem
    from ..models.category_option_organisation_units_item import CategoryOptionOrganisationUnitsItem
    from ..models.category_option_user import CategoryOptionUser
    from ..models.object_style import ObjectStyle
    from ..models.query_modifiers import QueryModifiers
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="CategoryOption")


@_attrs_define
class CategoryOption:
    """
    Attributes:
        aggregation_type (CategoryOptionAggregationType):
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        categories (Union[Unset, list['CategoryOptionCategoriesItem']]):
        category_option_combos (Union[Unset, list['CategoryOptionCategoryOptionCombosItem']]):
        category_option_groups (Union[Unset, list['CategoryOptionCategoryOptionGroupsItem']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, CategoryOptionCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        description (Union[Unset, str]):
        dimension_item (Union[Unset, str]):
        display_description (Union[Unset, str]):
        display_form_name (Union[Unset, str]):
        display_name (Union[Unset, str]):
        display_short_name (Union[Unset, str]):
        end_date (Union[Unset, datetime.datetime]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        form_name (Union[Unset, str]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        is_default (Union[Unset, bool]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, CategoryOptionLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        legend_set (Union[Unset, CategoryOptionLegendSet]): A UID reference to a LegendSet
            (Java name `org.hisp.dhis.legend.LegendSet`)
        legend_sets (Union[Unset, list['CategoryOptionLegendSetsItem']]):
        name (Union[Unset, str]):
        organisation_units (Union[Unset, list['CategoryOptionOrganisationUnitsItem']]):
        query_mods (Union[Unset, QueryModifiers]):
        sharing (Union[Unset, Sharing]):
        short_name (Union[Unset, str]):
        start_date (Union[Unset, datetime.datetime]):
        style (Union[Unset, ObjectStyle]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, CategoryOptionUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    aggregation_type: CategoryOptionAggregationType
    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    categories: Union[Unset, list["CategoryOptionCategoriesItem"]] = UNSET
    category_option_combos: Union[Unset, list["CategoryOptionCategoryOptionCombosItem"]] = UNSET
    category_option_groups: Union[Unset, list["CategoryOptionCategoryOptionGroupsItem"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "CategoryOptionCreatedBy"] = UNSET
    description: Union[Unset, str] = UNSET
    dimension_item: Union[Unset, str] = UNSET
    display_description: Union[Unset, str] = UNSET
    display_form_name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    display_short_name: Union[Unset, str] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    form_name: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    is_default: Union[Unset, bool] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "CategoryOptionLastUpdatedBy"] = UNSET
    legend_set: Union[Unset, "CategoryOptionLegendSet"] = UNSET
    legend_sets: Union[Unset, list["CategoryOptionLegendSetsItem"]] = UNSET
    name: Union[Unset, str] = UNSET
    organisation_units: Union[Unset, list["CategoryOptionOrganisationUnitsItem"]] = UNSET
    query_mods: Union[Unset, "QueryModifiers"] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    short_name: Union[Unset, str] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    style: Union[Unset, "ObjectStyle"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "CategoryOptionUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregation_type = self.aggregation_type.value

        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        attribute_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_values, Unset):
            attribute_values = []
            for attribute_values_item_data in self.attribute_values:
                attribute_values_item = attribute_values_item_data.to_dict()
                attribute_values.append(attribute_values_item)

        categories: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)

        category_option_combos: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.category_option_combos, Unset):
            category_option_combos = []
            for category_option_combos_item_data in self.category_option_combos:
                category_option_combos_item = category_option_combos_item_data.to_dict()
                category_option_combos.append(category_option_combos_item)

        category_option_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.category_option_groups, Unset):
            category_option_groups = []
            for category_option_groups_item_data in self.category_option_groups:
                category_option_groups_item = category_option_groups_item_data.to_dict()
                category_option_groups.append(category_option_groups_item)

        code = self.code

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

        display_name = self.display_name

        display_short_name = self.display_short_name

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        form_name = self.form_name

        href = self.href

        id = self.id

        is_default = self.is_default

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

        organisation_units: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.organisation_units, Unset):
            organisation_units = []
            for organisation_units_item_data in self.organisation_units:
                organisation_units_item = organisation_units_item_data.to_dict()
                organisation_units.append(organisation_units_item)

        query_mods: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.query_mods, Unset):
            query_mods = self.query_mods.to_dict()

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        short_name = self.short_name

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

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
                "aggregationType": aggregation_type,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if categories is not UNSET:
            field_dict["categories"] = categories
        if category_option_combos is not UNSET:
            field_dict["categoryOptionCombos"] = category_option_combos
        if category_option_groups is not UNSET:
            field_dict["categoryOptionGroups"] = category_option_groups
        if code is not UNSET:
            field_dict["code"] = code
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
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_short_name is not UNSET:
            field_dict["displayShortName"] = display_short_name
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
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
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
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
        if organisation_units is not UNSET:
            field_dict["organisationUnits"] = organisation_units
        if query_mods is not UNSET:
            field_dict["queryMods"] = query_mods
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
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
        from ..models.category_option_categories_item import CategoryOptionCategoriesItem
        from ..models.category_option_category_option_combos_item import CategoryOptionCategoryOptionCombosItem
        from ..models.category_option_category_option_groups_item import CategoryOptionCategoryOptionGroupsItem
        from ..models.category_option_created_by import CategoryOptionCreatedBy
        from ..models.category_option_last_updated_by import CategoryOptionLastUpdatedBy
        from ..models.category_option_legend_set import CategoryOptionLegendSet
        from ..models.category_option_legend_sets_item import CategoryOptionLegendSetsItem
        from ..models.category_option_organisation_units_item import CategoryOptionOrganisationUnitsItem
        from ..models.category_option_user import CategoryOptionUser
        from ..models.object_style import ObjectStyle
        from ..models.query_modifiers import QueryModifiers
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        aggregation_type = CategoryOptionAggregationType(d.pop("aggregationType"))

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

        categories = []
        _categories = d.pop("categories", UNSET)
        for categories_item_data in _categories or []:
            categories_item = CategoryOptionCategoriesItem.from_dict(categories_item_data)

            categories.append(categories_item)

        category_option_combos = []
        _category_option_combos = d.pop("categoryOptionCombos", UNSET)
        for category_option_combos_item_data in _category_option_combos or []:
            category_option_combos_item = CategoryOptionCategoryOptionCombosItem.from_dict(
                category_option_combos_item_data
            )

            category_option_combos.append(category_option_combos_item)

        category_option_groups = []
        _category_option_groups = d.pop("categoryOptionGroups", UNSET)
        for category_option_groups_item_data in _category_option_groups or []:
            category_option_groups_item = CategoryOptionCategoryOptionGroupsItem.from_dict(
                category_option_groups_item_data
            )

            category_option_groups.append(category_option_groups_item)

        code = d.pop("code", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, CategoryOptionCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = CategoryOptionCreatedBy.from_dict(_created_by)

        description = d.pop("description", UNSET)

        dimension_item = d.pop("dimensionItem", UNSET)

        display_description = d.pop("displayDescription", UNSET)

        display_form_name = d.pop("displayFormName", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_short_name = d.pop("displayShortName", UNSET)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        form_name = d.pop("formName", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        is_default = d.pop("isDefault", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, CategoryOptionLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = CategoryOptionLastUpdatedBy.from_dict(_last_updated_by)

        _legend_set = d.pop("legendSet", UNSET)
        legend_set: Union[Unset, CategoryOptionLegendSet]
        if isinstance(_legend_set, Unset):
            legend_set = UNSET
        else:
            legend_set = CategoryOptionLegendSet.from_dict(_legend_set)

        legend_sets = []
        _legend_sets = d.pop("legendSets", UNSET)
        for legend_sets_item_data in _legend_sets or []:
            legend_sets_item = CategoryOptionLegendSetsItem.from_dict(legend_sets_item_data)

            legend_sets.append(legend_sets_item)

        name = d.pop("name", UNSET)

        organisation_units = []
        _organisation_units = d.pop("organisationUnits", UNSET)
        for organisation_units_item_data in _organisation_units or []:
            organisation_units_item = CategoryOptionOrganisationUnitsItem.from_dict(organisation_units_item_data)

            organisation_units.append(organisation_units_item)

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

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

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
        user: Union[Unset, CategoryOptionUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = CategoryOptionUser.from_dict(_user)

        category_option = cls(
            aggregation_type=aggregation_type,
            access=access,
            attribute_values=attribute_values,
            categories=categories,
            category_option_combos=category_option_combos,
            category_option_groups=category_option_groups,
            code=code,
            created=created,
            created_by=created_by,
            description=description,
            dimension_item=dimension_item,
            display_description=display_description,
            display_form_name=display_form_name,
            display_name=display_name,
            display_short_name=display_short_name,
            end_date=end_date,
            favorite=favorite,
            favorites=favorites,
            form_name=form_name,
            href=href,
            id=id,
            is_default=is_default,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            legend_set=legend_set,
            legend_sets=legend_sets,
            name=name,
            organisation_units=organisation_units,
            query_mods=query_mods,
            sharing=sharing,
            short_name=short_name,
            start_date=start_date,
            style=style,
            translations=translations,
            user=user,
        )

        category_option.additional_properties = d
        return category_option

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
