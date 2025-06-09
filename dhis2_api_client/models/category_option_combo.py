import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.category_option_combo_aggregation_type import CategoryOptionComboAggregationType
from ..models.category_option_combo_dimension_item_type import CategoryOptionComboDimensionItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.category_option_combo_category_combo import CategoryOptionComboCategoryCombo
    from ..models.category_option_combo_category_options_item import CategoryOptionComboCategoryOptionsItem
    from ..models.category_option_combo_created_by import CategoryOptionComboCreatedBy
    from ..models.category_option_combo_last_updated_by import CategoryOptionComboLastUpdatedBy
    from ..models.category_option_combo_legend_set import CategoryOptionComboLegendSet
    from ..models.category_option_combo_legend_sets_item import CategoryOptionComboLegendSetsItem
    from ..models.category_option_combo_user import CategoryOptionComboUser
    from ..models.query_modifiers import QueryModifiers
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="CategoryOptionCombo")


@_attrs_define
class CategoryOptionCombo:
    """
    Attributes:
        aggregation_type (CategoryOptionComboAggregationType):
        dimension_item_type (CategoryOptionComboDimensionItemType):
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        category_combo (Union[Unset, CategoryOptionComboCategoryCombo]): A UID reference to a CategoryCombo
            (Java name `org.hisp.dhis.category.CategoryCombo`)
        category_options (Union[Unset, list['CategoryOptionComboCategoryOptionsItem']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, CategoryOptionComboCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        description (Union[Unset, str]):
        dimension_item (Union[Unset, str]):
        display_description (Union[Unset, str]):
        display_form_name (Union[Unset, str]):
        display_name (Union[Unset, str]):
        display_short_name (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        form_name (Union[Unset, str]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        ignore_approval (Union[Unset, bool]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, CategoryOptionComboLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        legend_set (Union[Unset, CategoryOptionComboLegendSet]): A UID reference to a LegendSet
            (Java name `org.hisp.dhis.legend.LegendSet`)
        legend_sets (Union[Unset, list['CategoryOptionComboLegendSetsItem']]):
        query_mods (Union[Unset, QueryModifiers]):
        sharing (Union[Unset, Sharing]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, CategoryOptionComboUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    aggregation_type: CategoryOptionComboAggregationType
    dimension_item_type: CategoryOptionComboDimensionItemType
    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    category_combo: Union[Unset, "CategoryOptionComboCategoryCombo"] = UNSET
    category_options: Union[Unset, list["CategoryOptionComboCategoryOptionsItem"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "CategoryOptionComboCreatedBy"] = UNSET
    description: Union[Unset, str] = UNSET
    dimension_item: Union[Unset, str] = UNSET
    display_description: Union[Unset, str] = UNSET
    display_form_name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    display_short_name: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    form_name: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    ignore_approval: Union[Unset, bool] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "CategoryOptionComboLastUpdatedBy"] = UNSET
    legend_set: Union[Unset, "CategoryOptionComboLegendSet"] = UNSET
    legend_sets: Union[Unset, list["CategoryOptionComboLegendSetsItem"]] = UNSET
    query_mods: Union[Unset, "QueryModifiers"] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "CategoryOptionComboUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregation_type = self.aggregation_type.value

        dimension_item_type = self.dimension_item_type.value

        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        attribute_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_values, Unset):
            attribute_values = []
            for attribute_values_item_data in self.attribute_values:
                attribute_values_item = attribute_values_item_data.to_dict()
                attribute_values.append(attribute_values_item)

        category_combo: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.category_combo, Unset):
            category_combo = self.category_combo.to_dict()

        category_options: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.category_options, Unset):
            category_options = []
            for category_options_item_data in self.category_options:
                category_options_item = category_options_item_data.to_dict()
                category_options.append(category_options_item)

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

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        form_name = self.form_name

        href = self.href

        id = self.id

        ignore_approval = self.ignore_approval

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

        query_mods: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.query_mods, Unset):
            query_mods = self.query_mods.to_dict()

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

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
                "dimensionItemType": dimension_item_type,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if category_combo is not UNSET:
            field_dict["categoryCombo"] = category_combo
        if category_options is not UNSET:
            field_dict["categoryOptions"] = category_options
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
        if ignore_approval is not UNSET:
            field_dict["ignoreApproval"] = ignore_approval
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if legend_set is not UNSET:
            field_dict["legendSet"] = legend_set
        if legend_sets is not UNSET:
            field_dict["legendSets"] = legend_sets
        if query_mods is not UNSET:
            field_dict["queryMods"] = query_mods
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.category_option_combo_category_combo import CategoryOptionComboCategoryCombo
        from ..models.category_option_combo_category_options_item import CategoryOptionComboCategoryOptionsItem
        from ..models.category_option_combo_created_by import CategoryOptionComboCreatedBy
        from ..models.category_option_combo_last_updated_by import CategoryOptionComboLastUpdatedBy
        from ..models.category_option_combo_legend_set import CategoryOptionComboLegendSet
        from ..models.category_option_combo_legend_sets_item import CategoryOptionComboLegendSetsItem
        from ..models.category_option_combo_user import CategoryOptionComboUser
        from ..models.query_modifiers import QueryModifiers
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        aggregation_type = CategoryOptionComboAggregationType(d.pop("aggregationType"))

        dimension_item_type = CategoryOptionComboDimensionItemType(d.pop("dimensionItemType"))

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

        _category_combo = d.pop("categoryCombo", UNSET)
        category_combo: Union[Unset, CategoryOptionComboCategoryCombo]
        if isinstance(_category_combo, Unset):
            category_combo = UNSET
        else:
            category_combo = CategoryOptionComboCategoryCombo.from_dict(_category_combo)

        category_options = []
        _category_options = d.pop("categoryOptions", UNSET)
        for category_options_item_data in _category_options or []:
            category_options_item = CategoryOptionComboCategoryOptionsItem.from_dict(category_options_item_data)

            category_options.append(category_options_item)

        code = d.pop("code", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, CategoryOptionComboCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = CategoryOptionComboCreatedBy.from_dict(_created_by)

        description = d.pop("description", UNSET)

        dimension_item = d.pop("dimensionItem", UNSET)

        display_description = d.pop("displayDescription", UNSET)

        display_form_name = d.pop("displayFormName", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_short_name = d.pop("displayShortName", UNSET)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        form_name = d.pop("formName", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        ignore_approval = d.pop("ignoreApproval", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, CategoryOptionComboLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = CategoryOptionComboLastUpdatedBy.from_dict(_last_updated_by)

        _legend_set = d.pop("legendSet", UNSET)
        legend_set: Union[Unset, CategoryOptionComboLegendSet]
        if isinstance(_legend_set, Unset):
            legend_set = UNSET
        else:
            legend_set = CategoryOptionComboLegendSet.from_dict(_legend_set)

        legend_sets = []
        _legend_sets = d.pop("legendSets", UNSET)
        for legend_sets_item_data in _legend_sets or []:
            legend_sets_item = CategoryOptionComboLegendSetsItem.from_dict(legend_sets_item_data)

            legend_sets.append(legend_sets_item)

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

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, CategoryOptionComboUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = CategoryOptionComboUser.from_dict(_user)

        category_option_combo = cls(
            aggregation_type=aggregation_type,
            dimension_item_type=dimension_item_type,
            access=access,
            attribute_values=attribute_values,
            category_combo=category_combo,
            category_options=category_options,
            code=code,
            created=created,
            created_by=created_by,
            description=description,
            dimension_item=dimension_item,
            display_description=display_description,
            display_form_name=display_form_name,
            display_name=display_name,
            display_short_name=display_short_name,
            favorite=favorite,
            favorites=favorites,
            form_name=form_name,
            href=href,
            id=id,
            ignore_approval=ignore_approval,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            legend_set=legend_set,
            legend_sets=legend_sets,
            query_mods=query_mods,
            sharing=sharing,
            translations=translations,
            user=user,
        )

        category_option_combo.additional_properties = d
        return category_option_combo

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
