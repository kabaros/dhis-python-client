import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.program_indicator_aggregation_type import ProgramIndicatorAggregationType
from ..models.program_indicator_analytics_type import ProgramIndicatorAnalyticsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.analytics_period_boundary import AnalyticsPeriodBoundary
    from ..models.attribute_value import AttributeValue
    from ..models.object_style import ObjectStyle
    from ..models.program_indicator_created_by import ProgramIndicatorCreatedBy
    from ..models.program_indicator_last_updated_by import ProgramIndicatorLastUpdatedBy
    from ..models.program_indicator_legend_set import ProgramIndicatorLegendSet
    from ..models.program_indicator_legend_sets_item import ProgramIndicatorLegendSetsItem
    from ..models.program_indicator_program import ProgramIndicatorProgram
    from ..models.program_indicator_program_indicator_groups_item import ProgramIndicatorProgramIndicatorGroupsItem
    from ..models.program_indicator_user import ProgramIndicatorUser
    from ..models.query_modifiers import QueryModifiers
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="ProgramIndicator")


@_attrs_define
class ProgramIndicator:
    """
    Attributes:
        aggregation_type (ProgramIndicatorAggregationType):
        analytics_type (ProgramIndicatorAnalyticsType):
        access (Union[Unset, Access]):
        aggregate_export_attribute_option_combo (Union[Unset, str]):
        aggregate_export_category_option_combo (Union[Unset, str]):
        analytics_period_boundaries (Union[Unset, list['AnalyticsPeriodBoundary']]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, ProgramIndicatorCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        decimals (Union[Unset, int]):
        description (Union[Unset, str]):
        dimension_item (Union[Unset, str]):
        display_description (Union[Unset, str]):
        display_form_name (Union[Unset, str]):
        display_in_form (Union[Unset, bool]):
        display_name (Union[Unset, str]):
        display_short_name (Union[Unset, str]):
        expression (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        filter_ (Union[Unset, str]):
        form_name (Union[Unset, str]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, ProgramIndicatorLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        legend_set (Union[Unset, ProgramIndicatorLegendSet]): A UID reference to a LegendSet
            (Java name `org.hisp.dhis.legend.LegendSet`)
        legend_sets (Union[Unset, list['ProgramIndicatorLegendSetsItem']]):
        name (Union[Unset, str]):
        org_unit_field (Union[Unset, str]):
        program (Union[Unset, ProgramIndicatorProgram]): A UID reference to a Program
            (Java name `org.hisp.dhis.program.Program`)
        program_indicator_groups (Union[Unset, list['ProgramIndicatorProgramIndicatorGroupsItem']]):
        query_mods (Union[Unset, QueryModifiers]):
        sharing (Union[Unset, Sharing]):
        short_name (Union[Unset, str]):
        style (Union[Unset, ObjectStyle]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, ProgramIndicatorUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    aggregation_type: ProgramIndicatorAggregationType
    analytics_type: ProgramIndicatorAnalyticsType
    access: Union[Unset, "Access"] = UNSET
    aggregate_export_attribute_option_combo: Union[Unset, str] = UNSET
    aggregate_export_category_option_combo: Union[Unset, str] = UNSET
    analytics_period_boundaries: Union[Unset, list["AnalyticsPeriodBoundary"]] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "ProgramIndicatorCreatedBy"] = UNSET
    decimals: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    dimension_item: Union[Unset, str] = UNSET
    display_description: Union[Unset, str] = UNSET
    display_form_name: Union[Unset, str] = UNSET
    display_in_form: Union[Unset, bool] = UNSET
    display_name: Union[Unset, str] = UNSET
    display_short_name: Union[Unset, str] = UNSET
    expression: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    filter_: Union[Unset, str] = UNSET
    form_name: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "ProgramIndicatorLastUpdatedBy"] = UNSET
    legend_set: Union[Unset, "ProgramIndicatorLegendSet"] = UNSET
    legend_sets: Union[Unset, list["ProgramIndicatorLegendSetsItem"]] = UNSET
    name: Union[Unset, str] = UNSET
    org_unit_field: Union[Unset, str] = UNSET
    program: Union[Unset, "ProgramIndicatorProgram"] = UNSET
    program_indicator_groups: Union[Unset, list["ProgramIndicatorProgramIndicatorGroupsItem"]] = UNSET
    query_mods: Union[Unset, "QueryModifiers"] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    short_name: Union[Unset, str] = UNSET
    style: Union[Unset, "ObjectStyle"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "ProgramIndicatorUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregation_type = self.aggregation_type.value

        analytics_type = self.analytics_type.value

        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        aggregate_export_attribute_option_combo = self.aggregate_export_attribute_option_combo

        aggregate_export_category_option_combo = self.aggregate_export_category_option_combo

        analytics_period_boundaries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.analytics_period_boundaries, Unset):
            analytics_period_boundaries = []
            for analytics_period_boundaries_item_data in self.analytics_period_boundaries:
                analytics_period_boundaries_item = analytics_period_boundaries_item_data.to_dict()
                analytics_period_boundaries.append(analytics_period_boundaries_item)

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

        decimals = self.decimals

        description = self.description

        dimension_item = self.dimension_item

        display_description = self.display_description

        display_form_name = self.display_form_name

        display_in_form = self.display_in_form

        display_name = self.display_name

        display_short_name = self.display_short_name

        expression = self.expression

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        filter_ = self.filter_

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

        legend_sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.legend_sets, Unset):
            legend_sets = []
            for legend_sets_item_data in self.legend_sets:
                legend_sets_item = legend_sets_item_data.to_dict()
                legend_sets.append(legend_sets_item)

        name = self.name

        org_unit_field = self.org_unit_field

        program: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program, Unset):
            program = self.program.to_dict()

        program_indicator_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.program_indicator_groups, Unset):
            program_indicator_groups = []
            for program_indicator_groups_item_data in self.program_indicator_groups:
                program_indicator_groups_item = program_indicator_groups_item_data.to_dict()
                program_indicator_groups.append(program_indicator_groups_item)

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

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aggregationType": aggregation_type,
                "analyticsType": analytics_type,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if aggregate_export_attribute_option_combo is not UNSET:
            field_dict["aggregateExportAttributeOptionCombo"] = aggregate_export_attribute_option_combo
        if aggregate_export_category_option_combo is not UNSET:
            field_dict["aggregateExportCategoryOptionCombo"] = aggregate_export_category_option_combo
        if analytics_period_boundaries is not UNSET:
            field_dict["analyticsPeriodBoundaries"] = analytics_period_boundaries
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if code is not UNSET:
            field_dict["code"] = code
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if decimals is not UNSET:
            field_dict["decimals"] = decimals
        if description is not UNSET:
            field_dict["description"] = description
        if dimension_item is not UNSET:
            field_dict["dimensionItem"] = dimension_item
        if display_description is not UNSET:
            field_dict["displayDescription"] = display_description
        if display_form_name is not UNSET:
            field_dict["displayFormName"] = display_form_name
        if display_in_form is not UNSET:
            field_dict["displayInForm"] = display_in_form
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_short_name is not UNSET:
            field_dict["displayShortName"] = display_short_name
        if expression is not UNSET:
            field_dict["expression"] = expression
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
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
        if legend_sets is not UNSET:
            field_dict["legendSets"] = legend_sets
        if name is not UNSET:
            field_dict["name"] = name
        if org_unit_field is not UNSET:
            field_dict["orgUnitField"] = org_unit_field
        if program is not UNSET:
            field_dict["program"] = program
        if program_indicator_groups is not UNSET:
            field_dict["programIndicatorGroups"] = program_indicator_groups
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
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.analytics_period_boundary import AnalyticsPeriodBoundary
        from ..models.attribute_value import AttributeValue
        from ..models.object_style import ObjectStyle
        from ..models.program_indicator_created_by import ProgramIndicatorCreatedBy
        from ..models.program_indicator_last_updated_by import ProgramIndicatorLastUpdatedBy
        from ..models.program_indicator_legend_set import ProgramIndicatorLegendSet
        from ..models.program_indicator_legend_sets_item import ProgramIndicatorLegendSetsItem
        from ..models.program_indicator_program import ProgramIndicatorProgram
        from ..models.program_indicator_program_indicator_groups_item import ProgramIndicatorProgramIndicatorGroupsItem
        from ..models.program_indicator_user import ProgramIndicatorUser
        from ..models.query_modifiers import QueryModifiers
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        aggregation_type = ProgramIndicatorAggregationType(d.pop("aggregationType"))

        analytics_type = ProgramIndicatorAnalyticsType(d.pop("analyticsType"))

        _access = d.pop("access", UNSET)
        access: Union[Unset, Access]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

        aggregate_export_attribute_option_combo = d.pop("aggregateExportAttributeOptionCombo", UNSET)

        aggregate_export_category_option_combo = d.pop("aggregateExportCategoryOptionCombo", UNSET)

        analytics_period_boundaries = []
        _analytics_period_boundaries = d.pop("analyticsPeriodBoundaries", UNSET)
        for analytics_period_boundaries_item_data in _analytics_period_boundaries or []:
            analytics_period_boundaries_item = AnalyticsPeriodBoundary.from_dict(analytics_period_boundaries_item_data)

            analytics_period_boundaries.append(analytics_period_boundaries_item)

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
        created_by: Union[Unset, ProgramIndicatorCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = ProgramIndicatorCreatedBy.from_dict(_created_by)

        decimals = d.pop("decimals", UNSET)

        description = d.pop("description", UNSET)

        dimension_item = d.pop("dimensionItem", UNSET)

        display_description = d.pop("displayDescription", UNSET)

        display_form_name = d.pop("displayFormName", UNSET)

        display_in_form = d.pop("displayInForm", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_short_name = d.pop("displayShortName", UNSET)

        expression = d.pop("expression", UNSET)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        filter_ = d.pop("filter", UNSET)

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
        last_updated_by: Union[Unset, ProgramIndicatorLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = ProgramIndicatorLastUpdatedBy.from_dict(_last_updated_by)

        _legend_set = d.pop("legendSet", UNSET)
        legend_set: Union[Unset, ProgramIndicatorLegendSet]
        if isinstance(_legend_set, Unset):
            legend_set = UNSET
        else:
            legend_set = ProgramIndicatorLegendSet.from_dict(_legend_set)

        legend_sets = []
        _legend_sets = d.pop("legendSets", UNSET)
        for legend_sets_item_data in _legend_sets or []:
            legend_sets_item = ProgramIndicatorLegendSetsItem.from_dict(legend_sets_item_data)

            legend_sets.append(legend_sets_item)

        name = d.pop("name", UNSET)

        org_unit_field = d.pop("orgUnitField", UNSET)

        _program = d.pop("program", UNSET)
        program: Union[Unset, ProgramIndicatorProgram]
        if isinstance(_program, Unset):
            program = UNSET
        else:
            program = ProgramIndicatorProgram.from_dict(_program)

        program_indicator_groups = []
        _program_indicator_groups = d.pop("programIndicatorGroups", UNSET)
        for program_indicator_groups_item_data in _program_indicator_groups or []:
            program_indicator_groups_item = ProgramIndicatorProgramIndicatorGroupsItem.from_dict(
                program_indicator_groups_item_data
            )

            program_indicator_groups.append(program_indicator_groups_item)

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

        _user = d.pop("user", UNSET)
        user: Union[Unset, ProgramIndicatorUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ProgramIndicatorUser.from_dict(_user)

        program_indicator = cls(
            aggregation_type=aggregation_type,
            analytics_type=analytics_type,
            access=access,
            aggregate_export_attribute_option_combo=aggregate_export_attribute_option_combo,
            aggregate_export_category_option_combo=aggregate_export_category_option_combo,
            analytics_period_boundaries=analytics_period_boundaries,
            attribute_values=attribute_values,
            code=code,
            created=created,
            created_by=created_by,
            decimals=decimals,
            description=description,
            dimension_item=dimension_item,
            display_description=display_description,
            display_form_name=display_form_name,
            display_in_form=display_in_form,
            display_name=display_name,
            display_short_name=display_short_name,
            expression=expression,
            favorite=favorite,
            favorites=favorites,
            filter_=filter_,
            form_name=form_name,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            legend_set=legend_set,
            legend_sets=legend_sets,
            name=name,
            org_unit_field=org_unit_field,
            program=program,
            program_indicator_groups=program_indicator_groups,
            query_mods=query_mods,
            sharing=sharing,
            short_name=short_name,
            style=style,
            translations=translations,
            user=user,
        )

        program_indicator.additional_properties = d
        return program_indicator

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
