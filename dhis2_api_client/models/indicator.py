import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.indicator_aggregation_type import IndicatorAggregationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.indicator_created_by import IndicatorCreatedBy
    from ..models.indicator_data_sets_item import IndicatorDataSetsItem
    from ..models.indicator_indicator_groups_item import IndicatorIndicatorGroupsItem
    from ..models.indicator_indicator_type import IndicatorIndicatorType
    from ..models.indicator_last_updated_by import IndicatorLastUpdatedBy
    from ..models.indicator_legend_set import IndicatorLegendSet
    from ..models.indicator_legend_sets_item import IndicatorLegendSetsItem
    from ..models.indicator_user import IndicatorUser
    from ..models.object_style import ObjectStyle
    from ..models.query_modifiers import QueryModifiers
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="Indicator")


@_attrs_define
class Indicator:
    """
    Attributes:
        aggregation_type (IndicatorAggregationType):
        access (Union[Unset, Access]):
        aggregate_export_attribute_option_combo (Union[Unset, str]):
        aggregate_export_category_option_combo (Union[Unset, str]):
        annualized (Union[Unset, bool]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, IndicatorCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        data_sets (Union[Unset, list['IndicatorDataSetsItem']]):
        decimals (Union[Unset, int]):
        denominator (Union[Unset, str]):
        denominator_description (Union[Unset, str]):
        description (Union[Unset, str]):
        dimension_item (Union[Unset, str]):
        display_denominator_description (Union[Unset, str]):
        display_description (Union[Unset, str]):
        display_form_name (Union[Unset, str]):
        display_name (Union[Unset, str]):
        display_numerator_description (Union[Unset, str]):
        display_short_name (Union[Unset, str]):
        exploded_denominator (Union[Unset, str]):
        exploded_numerator (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        form_name (Union[Unset, str]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        indicator_groups (Union[Unset, list['IndicatorIndicatorGroupsItem']]):
        indicator_type (Union[Unset, IndicatorIndicatorType]): A UID reference to a IndicatorType
            (Java name `org.hisp.dhis.indicator.IndicatorType`)
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, IndicatorLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        legend_set (Union[Unset, IndicatorLegendSet]): A UID reference to a LegendSet
            (Java name `org.hisp.dhis.legend.LegendSet`)
        legend_sets (Union[Unset, list['IndicatorLegendSetsItem']]):
        name (Union[Unset, str]):
        numerator (Union[Unset, str]):
        numerator_description (Union[Unset, str]):
        query_mods (Union[Unset, QueryModifiers]):
        sharing (Union[Unset, Sharing]):
        short_name (Union[Unset, str]):
        style (Union[Unset, ObjectStyle]):
        translations (Union[Unset, list['Translation']]):
        url (Union[Unset, str]):
        user (Union[Unset, IndicatorUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    aggregation_type: IndicatorAggregationType
    access: Union[Unset, "Access"] = UNSET
    aggregate_export_attribute_option_combo: Union[Unset, str] = UNSET
    aggregate_export_category_option_combo: Union[Unset, str] = UNSET
    annualized: Union[Unset, bool] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "IndicatorCreatedBy"] = UNSET
    data_sets: Union[Unset, list["IndicatorDataSetsItem"]] = UNSET
    decimals: Union[Unset, int] = UNSET
    denominator: Union[Unset, str] = UNSET
    denominator_description: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    dimension_item: Union[Unset, str] = UNSET
    display_denominator_description: Union[Unset, str] = UNSET
    display_description: Union[Unset, str] = UNSET
    display_form_name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    display_numerator_description: Union[Unset, str] = UNSET
    display_short_name: Union[Unset, str] = UNSET
    exploded_denominator: Union[Unset, str] = UNSET
    exploded_numerator: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    form_name: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    indicator_groups: Union[Unset, list["IndicatorIndicatorGroupsItem"]] = UNSET
    indicator_type: Union[Unset, "IndicatorIndicatorType"] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "IndicatorLastUpdatedBy"] = UNSET
    legend_set: Union[Unset, "IndicatorLegendSet"] = UNSET
    legend_sets: Union[Unset, list["IndicatorLegendSetsItem"]] = UNSET
    name: Union[Unset, str] = UNSET
    numerator: Union[Unset, str] = UNSET
    numerator_description: Union[Unset, str] = UNSET
    query_mods: Union[Unset, "QueryModifiers"] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    short_name: Union[Unset, str] = UNSET
    style: Union[Unset, "ObjectStyle"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    url: Union[Unset, str] = UNSET
    user: Union[Unset, "IndicatorUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregation_type = self.aggregation_type.value

        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        aggregate_export_attribute_option_combo = self.aggregate_export_attribute_option_combo

        aggregate_export_category_option_combo = self.aggregate_export_category_option_combo

        annualized = self.annualized

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

        data_sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_sets, Unset):
            data_sets = []
            for data_sets_item_data in self.data_sets:
                data_sets_item = data_sets_item_data.to_dict()
                data_sets.append(data_sets_item)

        decimals = self.decimals

        denominator = self.denominator

        denominator_description = self.denominator_description

        description = self.description

        dimension_item = self.dimension_item

        display_denominator_description = self.display_denominator_description

        display_description = self.display_description

        display_form_name = self.display_form_name

        display_name = self.display_name

        display_numerator_description = self.display_numerator_description

        display_short_name = self.display_short_name

        exploded_denominator = self.exploded_denominator

        exploded_numerator = self.exploded_numerator

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        form_name = self.form_name

        href = self.href

        id = self.id

        indicator_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.indicator_groups, Unset):
            indicator_groups = []
            for indicator_groups_item_data in self.indicator_groups:
                indicator_groups_item = indicator_groups_item_data.to_dict()
                indicator_groups.append(indicator_groups_item)

        indicator_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.indicator_type, Unset):
            indicator_type = self.indicator_type.to_dict()

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

        numerator = self.numerator

        numerator_description = self.numerator_description

        query_mods: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.query_mods, Unset):
            query_mods = self.query_mods.to_dict()

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        short_name = self.short_name

        style: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.style, Unset):
            style = self.style.to_dict()

        translations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        url = self.url

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
        if aggregate_export_attribute_option_combo is not UNSET:
            field_dict["aggregateExportAttributeOptionCombo"] = aggregate_export_attribute_option_combo
        if aggregate_export_category_option_combo is not UNSET:
            field_dict["aggregateExportCategoryOptionCombo"] = aggregate_export_category_option_combo
        if annualized is not UNSET:
            field_dict["annualized"] = annualized
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if code is not UNSET:
            field_dict["code"] = code
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if data_sets is not UNSET:
            field_dict["dataSets"] = data_sets
        if decimals is not UNSET:
            field_dict["decimals"] = decimals
        if denominator is not UNSET:
            field_dict["denominator"] = denominator
        if denominator_description is not UNSET:
            field_dict["denominatorDescription"] = denominator_description
        if description is not UNSET:
            field_dict["description"] = description
        if dimension_item is not UNSET:
            field_dict["dimensionItem"] = dimension_item
        if display_denominator_description is not UNSET:
            field_dict["displayDenominatorDescription"] = display_denominator_description
        if display_description is not UNSET:
            field_dict["displayDescription"] = display_description
        if display_form_name is not UNSET:
            field_dict["displayFormName"] = display_form_name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_numerator_description is not UNSET:
            field_dict["displayNumeratorDescription"] = display_numerator_description
        if display_short_name is not UNSET:
            field_dict["displayShortName"] = display_short_name
        if exploded_denominator is not UNSET:
            field_dict["explodedDenominator"] = exploded_denominator
        if exploded_numerator is not UNSET:
            field_dict["explodedNumerator"] = exploded_numerator
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
        if indicator_groups is not UNSET:
            field_dict["indicatorGroups"] = indicator_groups
        if indicator_type is not UNSET:
            field_dict["indicatorType"] = indicator_type
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
        if numerator is not UNSET:
            field_dict["numerator"] = numerator
        if numerator_description is not UNSET:
            field_dict["numeratorDescription"] = numerator_description
        if query_mods is not UNSET:
            field_dict["queryMods"] = query_mods
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if style is not UNSET:
            field_dict["style"] = style
        if translations is not UNSET:
            field_dict["translations"] = translations
        if url is not UNSET:
            field_dict["url"] = url
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.indicator_created_by import IndicatorCreatedBy
        from ..models.indicator_data_sets_item import IndicatorDataSetsItem
        from ..models.indicator_indicator_groups_item import IndicatorIndicatorGroupsItem
        from ..models.indicator_indicator_type import IndicatorIndicatorType
        from ..models.indicator_last_updated_by import IndicatorLastUpdatedBy
        from ..models.indicator_legend_set import IndicatorLegendSet
        from ..models.indicator_legend_sets_item import IndicatorLegendSetsItem
        from ..models.indicator_user import IndicatorUser
        from ..models.object_style import ObjectStyle
        from ..models.query_modifiers import QueryModifiers
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        aggregation_type = IndicatorAggregationType(d.pop("aggregationType"))

        _access = d.pop("access", UNSET)
        access: Union[Unset, Access]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

        aggregate_export_attribute_option_combo = d.pop("aggregateExportAttributeOptionCombo", UNSET)

        aggregate_export_category_option_combo = d.pop("aggregateExportCategoryOptionCombo", UNSET)

        annualized = d.pop("annualized", UNSET)

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
        created_by: Union[Unset, IndicatorCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = IndicatorCreatedBy.from_dict(_created_by)

        data_sets = []
        _data_sets = d.pop("dataSets", UNSET)
        for data_sets_item_data in _data_sets or []:
            data_sets_item = IndicatorDataSetsItem.from_dict(data_sets_item_data)

            data_sets.append(data_sets_item)

        decimals = d.pop("decimals", UNSET)

        denominator = d.pop("denominator", UNSET)

        denominator_description = d.pop("denominatorDescription", UNSET)

        description = d.pop("description", UNSET)

        dimension_item = d.pop("dimensionItem", UNSET)

        display_denominator_description = d.pop("displayDenominatorDescription", UNSET)

        display_description = d.pop("displayDescription", UNSET)

        display_form_name = d.pop("displayFormName", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_numerator_description = d.pop("displayNumeratorDescription", UNSET)

        display_short_name = d.pop("displayShortName", UNSET)

        exploded_denominator = d.pop("explodedDenominator", UNSET)

        exploded_numerator = d.pop("explodedNumerator", UNSET)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        form_name = d.pop("formName", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        indicator_groups = []
        _indicator_groups = d.pop("indicatorGroups", UNSET)
        for indicator_groups_item_data in _indicator_groups or []:
            indicator_groups_item = IndicatorIndicatorGroupsItem.from_dict(indicator_groups_item_data)

            indicator_groups.append(indicator_groups_item)

        _indicator_type = d.pop("indicatorType", UNSET)
        indicator_type: Union[Unset, IndicatorIndicatorType]
        if isinstance(_indicator_type, Unset):
            indicator_type = UNSET
        else:
            indicator_type = IndicatorIndicatorType.from_dict(_indicator_type)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, IndicatorLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = IndicatorLastUpdatedBy.from_dict(_last_updated_by)

        _legend_set = d.pop("legendSet", UNSET)
        legend_set: Union[Unset, IndicatorLegendSet]
        if isinstance(_legend_set, Unset):
            legend_set = UNSET
        else:
            legend_set = IndicatorLegendSet.from_dict(_legend_set)

        legend_sets = []
        _legend_sets = d.pop("legendSets", UNSET)
        for legend_sets_item_data in _legend_sets or []:
            legend_sets_item = IndicatorLegendSetsItem.from_dict(legend_sets_item_data)

            legend_sets.append(legend_sets_item)

        name = d.pop("name", UNSET)

        numerator = d.pop("numerator", UNSET)

        numerator_description = d.pop("numeratorDescription", UNSET)

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

        url = d.pop("url", UNSET)

        _user = d.pop("user", UNSET)
        user: Union[Unset, IndicatorUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = IndicatorUser.from_dict(_user)

        indicator = cls(
            aggregation_type=aggregation_type,
            access=access,
            aggregate_export_attribute_option_combo=aggregate_export_attribute_option_combo,
            aggregate_export_category_option_combo=aggregate_export_category_option_combo,
            annualized=annualized,
            attribute_values=attribute_values,
            code=code,
            created=created,
            created_by=created_by,
            data_sets=data_sets,
            decimals=decimals,
            denominator=denominator,
            denominator_description=denominator_description,
            description=description,
            dimension_item=dimension_item,
            display_denominator_description=display_denominator_description,
            display_description=display_description,
            display_form_name=display_form_name,
            display_name=display_name,
            display_numerator_description=display_numerator_description,
            display_short_name=display_short_name,
            exploded_denominator=exploded_denominator,
            exploded_numerator=exploded_numerator,
            favorite=favorite,
            favorites=favorites,
            form_name=form_name,
            href=href,
            id=id,
            indicator_groups=indicator_groups,
            indicator_type=indicator_type,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            legend_set=legend_set,
            legend_sets=legend_sets,
            name=name,
            numerator=numerator,
            numerator_description=numerator_description,
            query_mods=query_mods,
            sharing=sharing,
            short_name=short_name,
            style=style,
            translations=translations,
            url=url,
            user=user,
        )

        indicator.additional_properties = d
        return indicator

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
