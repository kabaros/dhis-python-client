import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.visualization_aggregation_type import VisualizationAggregationType
from ..models.visualization_digit_group_separator import VisualizationDigitGroupSeparator
from ..models.visualization_display_density import VisualizationDisplayDensity
from ..models.visualization_font_size import VisualizationFontSize
from ..models.visualization_hide_empty_row_items import VisualizationHideEmptyRowItems
from ..models.visualization_number_type import VisualizationNumberType
from ..models.visualization_regression_type import VisualizationRegressionType
from ..models.visualization_type import VisualizationType
from ..models.visualization_user_org_unit_type import VisualizationUserOrgUnitType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.axis import Axis
    from ..models.axis_v2 import AxisV2
    from ..models.category_dimension import CategoryDimension
    from ..models.category_option_group_set_dimension import CategoryOptionGroupSetDimension
    from ..models.data_dimension_item import DataDimensionItem
    from ..models.data_element_group_set_dimension import DataElementGroupSetDimension
    from ..models.legend_definitions import LegendDefinitions
    from ..models.organisation_unit_group_set_dimension import OrganisationUnitGroupSetDimension
    from ..models.outlier_analysis import OutlierAnalysis
    from ..models.relative_periods import RelativePeriods
    from ..models.reporting_params import ReportingParams
    from ..models.series import Series
    from ..models.series_key import SeriesKey
    from ..models.sharing import Sharing
    from ..models.sorting import Sorting
    from ..models.tracked_entity_attribute_dimension import TrackedEntityAttributeDimension
    from ..models.tracked_entity_data_element_dimension import TrackedEntityDataElementDimension
    from ..models.tracked_entity_program_indicator_dimension import TrackedEntityProgramIndicatorDimension
    from ..models.translation import Translation
    from ..models.visualization_columns_item import VisualizationColumnsItem
    from ..models.visualization_created_by import VisualizationCreatedBy
    from ..models.visualization_filters_item import VisualizationFiltersItem
    from ..models.visualization_font_style import VisualizationFontStyle
    from ..models.visualization_icon import VisualizationIcon
    from ..models.visualization_interpretations_item import VisualizationInterpretationsItem
    from ..models.visualization_item_organisation_unit_groups_item import VisualizationItemOrganisationUnitGroupsItem
    from ..models.visualization_last_updated_by import VisualizationLastUpdatedBy
    from ..models.visualization_organisation_units_item import VisualizationOrganisationUnitsItem
    from ..models.visualization_parent_graph_map import VisualizationParentGraphMap
    from ..models.visualization_rows_item import VisualizationRowsItem
    from ..models.visualization_user import VisualizationUser


T = TypeVar("T", bound="Visualization")


@_attrs_define
class Visualization:
    """
    Attributes:
        aggregation_type (VisualizationAggregationType):
        digit_group_separator (VisualizationDigitGroupSeparator):
        display_density (VisualizationDisplayDensity):
        font_size (VisualizationFontSize):
        hide_empty_row_items (VisualizationHideEmptyRowItems):
        number_type (VisualizationNumberType):
        regression_type (VisualizationRegressionType):
        sort_order (int):
        top_limit (int):
        type_ (VisualizationType):
        user_org_unit_type (VisualizationUserOrgUnitType):
        access (Union[Unset, Access]):
        attribute_dimensions (Union[Unset, list['TrackedEntityAttributeDimension']]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        axes (Union[Unset, list['AxisV2']]):
        base_line_label (Union[Unset, str]):
        base_line_value (Union[Unset, float]):
        category_dimensions (Union[Unset, list['CategoryDimension']]):
        category_option_group_set_dimensions (Union[Unset, list['CategoryOptionGroupSetDimension']]):
        code (Union[Unset, str]):
        col_sub_totals (Union[Unset, bool]):
        col_totals (Union[Unset, bool]):
        color_set (Union[Unset, str]):
        column_dimensions (Union[Unset, list[str]]):
        columns (Union[Unset, list['VisualizationColumnsItem']]):
        completed_only (Union[Unset, bool]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, VisualizationCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        cumulative_values (Union[Unset, bool]):
        data_dimension_items (Union[Unset, list['DataDimensionItem']]):
        data_element_dimensions (Union[Unset, list['TrackedEntityDataElementDimension']]):
        data_element_group_set_dimensions (Union[Unset, list['DataElementGroupSetDimension']]):
        description (Union[Unset, str]):
        display_base_line_label (Union[Unset, str]):
        display_description (Union[Unset, str]):
        display_domain_axis_label (Union[Unset, str]):
        display_form_name (Union[Unset, str]):
        display_name (Union[Unset, str]):
        display_range_axis_label (Union[Unset, str]):
        display_short_name (Union[Unset, str]):
        display_subtitle (Union[Unset, str]):
        display_target_line_label (Union[Unset, str]):
        display_title (Union[Unset, str]):
        domain_axis_label (Union[Unset, str]):
        end_date (Union[Unset, datetime.datetime]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        filter_dimensions (Union[Unset, list[str]]):
        filters (Union[Unset, list['VisualizationFiltersItem']]):
        fix_column_headers (Union[Unset, bool]):
        fix_row_headers (Union[Unset, bool]):
        font_style (Union[Unset, VisualizationFontStyle]):
        form_name (Union[Unset, str]):
        hide_empty_columns (Union[Unset, bool]):
        hide_empty_rows (Union[Unset, bool]):
        hide_legend (Union[Unset, bool]):
        hide_subtitle (Union[Unset, bool]):
        hide_title (Union[Unset, bool]):
        href (Union[Unset, str]):
        icons (Union[Unset, list['VisualizationIcon']]):
        id (Union[Unset, str]):
        interpretations (Union[Unset, list['VisualizationInterpretationsItem']]):
        item_organisation_unit_groups (Union[Unset, list['VisualizationItemOrganisationUnitGroupsItem']]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, VisualizationLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        legend (Union[Unset, LegendDefinitions]):
        measure_criteria (Union[Unset, str]):
        name (Union[Unset, str]):
        no_space_between_columns (Union[Unset, bool]):
        optional_axes (Union[Unset, list['Axis']]):
        org_unit_field (Union[Unset, str]):
        organisation_unit_group_set_dimensions (Union[Unset, list['OrganisationUnitGroupSetDimension']]):
        organisation_unit_levels (Union[Unset, list[int]]):
        organisation_units (Union[Unset, list['VisualizationOrganisationUnitsItem']]):
        outlier_analysis (Union[Unset, OutlierAnalysis]):
        parent_graph_map (Union[Unset, VisualizationParentGraphMap]):
        percent_stacked_values (Union[Unset, bool]):
        periods (Union[Unset, list[str]]):
        program_indicator_dimensions (Union[Unset, list['TrackedEntityProgramIndicatorDimension']]):
        range_axis_decimals (Union[Unset, int]):
        range_axis_label (Union[Unset, str]):
        range_axis_max_value (Union[Unset, float]):
        range_axis_min_value (Union[Unset, float]):
        range_axis_steps (Union[Unset, int]):
        regression (Union[Unset, bool]):
        relative_periods (Union[Unset, RelativePeriods]):
        reporting_params (Union[Unset, ReportingParams]):
        row_dimensions (Union[Unset, list[str]]):
        row_sub_totals (Union[Unset, bool]):
        row_totals (Union[Unset, bool]):
        rows (Union[Unset, list['VisualizationRowsItem']]):
        series (Union[Unset, list['Series']]):
        series_key (Union[Unset, SeriesKey]):
        sharing (Union[Unset, Sharing]):
        short_name (Union[Unset, str]):
        show_data (Union[Unset, bool]):
        show_dimension_labels (Union[Unset, bool]):
        show_hierarchy (Union[Unset, bool]):
        skip_rounding (Union[Unset, bool]):
        sorting (Union[Unset, list['Sorting']]):
        start_date (Union[Unset, datetime.datetime]):
        subscribed (Union[Unset, bool]):
        subscribers (Union[Unset, list[str]]):
        subtitle (Union[Unset, str]):
        target_line_label (Union[Unset, str]):
        target_line_value (Union[Unset, float]):
        time_field (Union[Unset, str]):
        title (Union[Unset, str]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, VisualizationUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        user_organisation_unit (Union[Unset, bool]):
        user_organisation_unit_children (Union[Unset, bool]):
        user_organisation_unit_grand_children (Union[Unset, bool]):
        visualization_period_name (Union[Unset, str]):
        yearly_series (Union[Unset, list[str]]):
    """

    aggregation_type: VisualizationAggregationType
    digit_group_separator: VisualizationDigitGroupSeparator
    display_density: VisualizationDisplayDensity
    font_size: VisualizationFontSize
    hide_empty_row_items: VisualizationHideEmptyRowItems
    number_type: VisualizationNumberType
    regression_type: VisualizationRegressionType
    sort_order: int
    top_limit: int
    type_: VisualizationType
    user_org_unit_type: VisualizationUserOrgUnitType
    access: Union[Unset, "Access"] = UNSET
    attribute_dimensions: Union[Unset, list["TrackedEntityAttributeDimension"]] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    axes: Union[Unset, list["AxisV2"]] = UNSET
    base_line_label: Union[Unset, str] = UNSET
    base_line_value: Union[Unset, float] = UNSET
    category_dimensions: Union[Unset, list["CategoryDimension"]] = UNSET
    category_option_group_set_dimensions: Union[Unset, list["CategoryOptionGroupSetDimension"]] = UNSET
    code: Union[Unset, str] = UNSET
    col_sub_totals: Union[Unset, bool] = UNSET
    col_totals: Union[Unset, bool] = UNSET
    color_set: Union[Unset, str] = UNSET
    column_dimensions: Union[Unset, list[str]] = UNSET
    columns: Union[Unset, list["VisualizationColumnsItem"]] = UNSET
    completed_only: Union[Unset, bool] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "VisualizationCreatedBy"] = UNSET
    cumulative_values: Union[Unset, bool] = UNSET
    data_dimension_items: Union[Unset, list["DataDimensionItem"]] = UNSET
    data_element_dimensions: Union[Unset, list["TrackedEntityDataElementDimension"]] = UNSET
    data_element_group_set_dimensions: Union[Unset, list["DataElementGroupSetDimension"]] = UNSET
    description: Union[Unset, str] = UNSET
    display_base_line_label: Union[Unset, str] = UNSET
    display_description: Union[Unset, str] = UNSET
    display_domain_axis_label: Union[Unset, str] = UNSET
    display_form_name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    display_range_axis_label: Union[Unset, str] = UNSET
    display_short_name: Union[Unset, str] = UNSET
    display_subtitle: Union[Unset, str] = UNSET
    display_target_line_label: Union[Unset, str] = UNSET
    display_title: Union[Unset, str] = UNSET
    domain_axis_label: Union[Unset, str] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    filter_dimensions: Union[Unset, list[str]] = UNSET
    filters: Union[Unset, list["VisualizationFiltersItem"]] = UNSET
    fix_column_headers: Union[Unset, bool] = UNSET
    fix_row_headers: Union[Unset, bool] = UNSET
    font_style: Union[Unset, "VisualizationFontStyle"] = UNSET
    form_name: Union[Unset, str] = UNSET
    hide_empty_columns: Union[Unset, bool] = UNSET
    hide_empty_rows: Union[Unset, bool] = UNSET
    hide_legend: Union[Unset, bool] = UNSET
    hide_subtitle: Union[Unset, bool] = UNSET
    hide_title: Union[Unset, bool] = UNSET
    href: Union[Unset, str] = UNSET
    icons: Union[Unset, list["VisualizationIcon"]] = UNSET
    id: Union[Unset, str] = UNSET
    interpretations: Union[Unset, list["VisualizationInterpretationsItem"]] = UNSET
    item_organisation_unit_groups: Union[Unset, list["VisualizationItemOrganisationUnitGroupsItem"]] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "VisualizationLastUpdatedBy"] = UNSET
    legend: Union[Unset, "LegendDefinitions"] = UNSET
    measure_criteria: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    no_space_between_columns: Union[Unset, bool] = UNSET
    optional_axes: Union[Unset, list["Axis"]] = UNSET
    org_unit_field: Union[Unset, str] = UNSET
    organisation_unit_group_set_dimensions: Union[Unset, list["OrganisationUnitGroupSetDimension"]] = UNSET
    organisation_unit_levels: Union[Unset, list[int]] = UNSET
    organisation_units: Union[Unset, list["VisualizationOrganisationUnitsItem"]] = UNSET
    outlier_analysis: Union[Unset, "OutlierAnalysis"] = UNSET
    parent_graph_map: Union[Unset, "VisualizationParentGraphMap"] = UNSET
    percent_stacked_values: Union[Unset, bool] = UNSET
    periods: Union[Unset, list[str]] = UNSET
    program_indicator_dimensions: Union[Unset, list["TrackedEntityProgramIndicatorDimension"]] = UNSET
    range_axis_decimals: Union[Unset, int] = UNSET
    range_axis_label: Union[Unset, str] = UNSET
    range_axis_max_value: Union[Unset, float] = UNSET
    range_axis_min_value: Union[Unset, float] = UNSET
    range_axis_steps: Union[Unset, int] = UNSET
    regression: Union[Unset, bool] = UNSET
    relative_periods: Union[Unset, "RelativePeriods"] = UNSET
    reporting_params: Union[Unset, "ReportingParams"] = UNSET
    row_dimensions: Union[Unset, list[str]] = UNSET
    row_sub_totals: Union[Unset, bool] = UNSET
    row_totals: Union[Unset, bool] = UNSET
    rows: Union[Unset, list["VisualizationRowsItem"]] = UNSET
    series: Union[Unset, list["Series"]] = UNSET
    series_key: Union[Unset, "SeriesKey"] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    short_name: Union[Unset, str] = UNSET
    show_data: Union[Unset, bool] = UNSET
    show_dimension_labels: Union[Unset, bool] = UNSET
    show_hierarchy: Union[Unset, bool] = UNSET
    skip_rounding: Union[Unset, bool] = UNSET
    sorting: Union[Unset, list["Sorting"]] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    subscribed: Union[Unset, bool] = UNSET
    subscribers: Union[Unset, list[str]] = UNSET
    subtitle: Union[Unset, str] = UNSET
    target_line_label: Union[Unset, str] = UNSET
    target_line_value: Union[Unset, float] = UNSET
    time_field: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "VisualizationUser"] = UNSET
    user_organisation_unit: Union[Unset, bool] = UNSET
    user_organisation_unit_children: Union[Unset, bool] = UNSET
    user_organisation_unit_grand_children: Union[Unset, bool] = UNSET
    visualization_period_name: Union[Unset, str] = UNSET
    yearly_series: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregation_type = self.aggregation_type.value

        digit_group_separator = self.digit_group_separator.value

        display_density = self.display_density.value

        font_size = self.font_size.value

        hide_empty_row_items = self.hide_empty_row_items.value

        number_type = self.number_type.value

        regression_type = self.regression_type.value

        sort_order = self.sort_order

        top_limit = self.top_limit

        type_ = self.type_.value

        user_org_unit_type = self.user_org_unit_type.value

        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        attribute_dimensions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_dimensions, Unset):
            attribute_dimensions = []
            for attribute_dimensions_item_data in self.attribute_dimensions:
                attribute_dimensions_item = attribute_dimensions_item_data.to_dict()
                attribute_dimensions.append(attribute_dimensions_item)

        attribute_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_values, Unset):
            attribute_values = []
            for attribute_values_item_data in self.attribute_values:
                attribute_values_item = attribute_values_item_data.to_dict()
                attribute_values.append(attribute_values_item)

        axes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.axes, Unset):
            axes = []
            for axes_item_data in self.axes:
                axes_item = axes_item_data.to_dict()
                axes.append(axes_item)

        base_line_label = self.base_line_label

        base_line_value = self.base_line_value

        category_dimensions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.category_dimensions, Unset):
            category_dimensions = []
            for category_dimensions_item_data in self.category_dimensions:
                category_dimensions_item = category_dimensions_item_data.to_dict()
                category_dimensions.append(category_dimensions_item)

        category_option_group_set_dimensions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.category_option_group_set_dimensions, Unset):
            category_option_group_set_dimensions = []
            for category_option_group_set_dimensions_item_data in self.category_option_group_set_dimensions:
                category_option_group_set_dimensions_item = category_option_group_set_dimensions_item_data.to_dict()
                category_option_group_set_dimensions.append(category_option_group_set_dimensions_item)

        code = self.code

        col_sub_totals = self.col_sub_totals

        col_totals = self.col_totals

        color_set = self.color_set

        column_dimensions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.column_dimensions, Unset):
            column_dimensions = self.column_dimensions

        columns: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.columns, Unset):
            columns = []
            for columns_item_data in self.columns:
                columns_item = columns_item_data.to_dict()
                columns.append(columns_item)

        completed_only = self.completed_only

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        cumulative_values = self.cumulative_values

        data_dimension_items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_dimension_items, Unset):
            data_dimension_items = []
            for data_dimension_items_item_data in self.data_dimension_items:
                data_dimension_items_item = data_dimension_items_item_data.to_dict()
                data_dimension_items.append(data_dimension_items_item)

        data_element_dimensions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_element_dimensions, Unset):
            data_element_dimensions = []
            for data_element_dimensions_item_data in self.data_element_dimensions:
                data_element_dimensions_item = data_element_dimensions_item_data.to_dict()
                data_element_dimensions.append(data_element_dimensions_item)

        data_element_group_set_dimensions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_element_group_set_dimensions, Unset):
            data_element_group_set_dimensions = []
            for data_element_group_set_dimensions_item_data in self.data_element_group_set_dimensions:
                data_element_group_set_dimensions_item = data_element_group_set_dimensions_item_data.to_dict()
                data_element_group_set_dimensions.append(data_element_group_set_dimensions_item)

        description = self.description

        display_base_line_label = self.display_base_line_label

        display_description = self.display_description

        display_domain_axis_label = self.display_domain_axis_label

        display_form_name = self.display_form_name

        display_name = self.display_name

        display_range_axis_label = self.display_range_axis_label

        display_short_name = self.display_short_name

        display_subtitle = self.display_subtitle

        display_target_line_label = self.display_target_line_label

        display_title = self.display_title

        domain_axis_label = self.domain_axis_label

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        filter_dimensions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.filter_dimensions, Unset):
            filter_dimensions = self.filter_dimensions

        filters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()
                filters.append(filters_item)

        fix_column_headers = self.fix_column_headers

        fix_row_headers = self.fix_row_headers

        font_style: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.font_style, Unset):
            font_style = self.font_style.to_dict()

        form_name = self.form_name

        hide_empty_columns = self.hide_empty_columns

        hide_empty_rows = self.hide_empty_rows

        hide_legend = self.hide_legend

        hide_subtitle = self.hide_subtitle

        hide_title = self.hide_title

        href = self.href

        icons: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.icons, Unset):
            icons = []
            for icons_item_data in self.icons:
                icons_item = icons_item_data.to_dict()
                icons.append(icons_item)

        id = self.id

        interpretations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.interpretations, Unset):
            interpretations = []
            for interpretations_item_data in self.interpretations:
                interpretations_item = interpretations_item_data.to_dict()
                interpretations.append(interpretations_item)

        item_organisation_unit_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.item_organisation_unit_groups, Unset):
            item_organisation_unit_groups = []
            for item_organisation_unit_groups_item_data in self.item_organisation_unit_groups:
                item_organisation_unit_groups_item = item_organisation_unit_groups_item_data.to_dict()
                item_organisation_unit_groups.append(item_organisation_unit_groups_item)

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        legend: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.legend, Unset):
            legend = self.legend.to_dict()

        measure_criteria = self.measure_criteria

        name = self.name

        no_space_between_columns = self.no_space_between_columns

        optional_axes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.optional_axes, Unset):
            optional_axes = []
            for optional_axes_item_data in self.optional_axes:
                optional_axes_item = optional_axes_item_data.to_dict()
                optional_axes.append(optional_axes_item)

        org_unit_field = self.org_unit_field

        organisation_unit_group_set_dimensions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.organisation_unit_group_set_dimensions, Unset):
            organisation_unit_group_set_dimensions = []
            for organisation_unit_group_set_dimensions_item_data in self.organisation_unit_group_set_dimensions:
                organisation_unit_group_set_dimensions_item = organisation_unit_group_set_dimensions_item_data.to_dict()
                organisation_unit_group_set_dimensions.append(organisation_unit_group_set_dimensions_item)

        organisation_unit_levels: Union[Unset, list[int]] = UNSET
        if not isinstance(self.organisation_unit_levels, Unset):
            organisation_unit_levels = self.organisation_unit_levels

        organisation_units: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.organisation_units, Unset):
            organisation_units = []
            for organisation_units_item_data in self.organisation_units:
                organisation_units_item = organisation_units_item_data.to_dict()
                organisation_units.append(organisation_units_item)

        outlier_analysis: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.outlier_analysis, Unset):
            outlier_analysis = self.outlier_analysis.to_dict()

        parent_graph_map: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_graph_map, Unset):
            parent_graph_map = self.parent_graph_map.to_dict()

        percent_stacked_values = self.percent_stacked_values

        periods: Union[Unset, list[str]] = UNSET
        if not isinstance(self.periods, Unset):
            periods = self.periods

        program_indicator_dimensions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.program_indicator_dimensions, Unset):
            program_indicator_dimensions = []
            for program_indicator_dimensions_item_data in self.program_indicator_dimensions:
                program_indicator_dimensions_item = program_indicator_dimensions_item_data.to_dict()
                program_indicator_dimensions.append(program_indicator_dimensions_item)

        range_axis_decimals = self.range_axis_decimals

        range_axis_label = self.range_axis_label

        range_axis_max_value = self.range_axis_max_value

        range_axis_min_value = self.range_axis_min_value

        range_axis_steps = self.range_axis_steps

        regression = self.regression

        relative_periods: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.relative_periods, Unset):
            relative_periods = self.relative_periods.to_dict()

        reporting_params: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.reporting_params, Unset):
            reporting_params = self.reporting_params.to_dict()

        row_dimensions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.row_dimensions, Unset):
            row_dimensions = self.row_dimensions

        row_sub_totals = self.row_sub_totals

        row_totals = self.row_totals

        rows: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)

        series: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.series, Unset):
            series = []
            for series_item_data in self.series:
                series_item = series_item_data.to_dict()
                series.append(series_item)

        series_key: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.series_key, Unset):
            series_key = self.series_key.to_dict()

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        short_name = self.short_name

        show_data = self.show_data

        show_dimension_labels = self.show_dimension_labels

        show_hierarchy = self.show_hierarchy

        skip_rounding = self.skip_rounding

        sorting: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sorting, Unset):
            sorting = []
            for sorting_item_data in self.sorting:
                sorting_item = sorting_item_data.to_dict()
                sorting.append(sorting_item)

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        subscribed = self.subscribed

        subscribers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.subscribers, Unset):
            subscribers = self.subscribers

        subtitle = self.subtitle

        target_line_label = self.target_line_label

        target_line_value = self.target_line_value

        time_field = self.time_field

        title = self.title

        translations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        user_organisation_unit = self.user_organisation_unit

        user_organisation_unit_children = self.user_organisation_unit_children

        user_organisation_unit_grand_children = self.user_organisation_unit_grand_children

        visualization_period_name = self.visualization_period_name

        yearly_series: Union[Unset, list[str]] = UNSET
        if not isinstance(self.yearly_series, Unset):
            yearly_series = self.yearly_series

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aggregationType": aggregation_type,
                "digitGroupSeparator": digit_group_separator,
                "displayDensity": display_density,
                "fontSize": font_size,
                "hideEmptyRowItems": hide_empty_row_items,
                "numberType": number_type,
                "regressionType": regression_type,
                "sortOrder": sort_order,
                "topLimit": top_limit,
                "type": type_,
                "userOrgUnitType": user_org_unit_type,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if attribute_dimensions is not UNSET:
            field_dict["attributeDimensions"] = attribute_dimensions
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if axes is not UNSET:
            field_dict["axes"] = axes
        if base_line_label is not UNSET:
            field_dict["baseLineLabel"] = base_line_label
        if base_line_value is not UNSET:
            field_dict["baseLineValue"] = base_line_value
        if category_dimensions is not UNSET:
            field_dict["categoryDimensions"] = category_dimensions
        if category_option_group_set_dimensions is not UNSET:
            field_dict["categoryOptionGroupSetDimensions"] = category_option_group_set_dimensions
        if code is not UNSET:
            field_dict["code"] = code
        if col_sub_totals is not UNSET:
            field_dict["colSubTotals"] = col_sub_totals
        if col_totals is not UNSET:
            field_dict["colTotals"] = col_totals
        if color_set is not UNSET:
            field_dict["colorSet"] = color_set
        if column_dimensions is not UNSET:
            field_dict["columnDimensions"] = column_dimensions
        if columns is not UNSET:
            field_dict["columns"] = columns
        if completed_only is not UNSET:
            field_dict["completedOnly"] = completed_only
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if cumulative_values is not UNSET:
            field_dict["cumulativeValues"] = cumulative_values
        if data_dimension_items is not UNSET:
            field_dict["dataDimensionItems"] = data_dimension_items
        if data_element_dimensions is not UNSET:
            field_dict["dataElementDimensions"] = data_element_dimensions
        if data_element_group_set_dimensions is not UNSET:
            field_dict["dataElementGroupSetDimensions"] = data_element_group_set_dimensions
        if description is not UNSET:
            field_dict["description"] = description
        if display_base_line_label is not UNSET:
            field_dict["displayBaseLineLabel"] = display_base_line_label
        if display_description is not UNSET:
            field_dict["displayDescription"] = display_description
        if display_domain_axis_label is not UNSET:
            field_dict["displayDomainAxisLabel"] = display_domain_axis_label
        if display_form_name is not UNSET:
            field_dict["displayFormName"] = display_form_name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_range_axis_label is not UNSET:
            field_dict["displayRangeAxisLabel"] = display_range_axis_label
        if display_short_name is not UNSET:
            field_dict["displayShortName"] = display_short_name
        if display_subtitle is not UNSET:
            field_dict["displaySubtitle"] = display_subtitle
        if display_target_line_label is not UNSET:
            field_dict["displayTargetLineLabel"] = display_target_line_label
        if display_title is not UNSET:
            field_dict["displayTitle"] = display_title
        if domain_axis_label is not UNSET:
            field_dict["domainAxisLabel"] = domain_axis_label
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if filter_dimensions is not UNSET:
            field_dict["filterDimensions"] = filter_dimensions
        if filters is not UNSET:
            field_dict["filters"] = filters
        if fix_column_headers is not UNSET:
            field_dict["fixColumnHeaders"] = fix_column_headers
        if fix_row_headers is not UNSET:
            field_dict["fixRowHeaders"] = fix_row_headers
        if font_style is not UNSET:
            field_dict["fontStyle"] = font_style
        if form_name is not UNSET:
            field_dict["formName"] = form_name
        if hide_empty_columns is not UNSET:
            field_dict["hideEmptyColumns"] = hide_empty_columns
        if hide_empty_rows is not UNSET:
            field_dict["hideEmptyRows"] = hide_empty_rows
        if hide_legend is not UNSET:
            field_dict["hideLegend"] = hide_legend
        if hide_subtitle is not UNSET:
            field_dict["hideSubtitle"] = hide_subtitle
        if hide_title is not UNSET:
            field_dict["hideTitle"] = hide_title
        if href is not UNSET:
            field_dict["href"] = href
        if icons is not UNSET:
            field_dict["icons"] = icons
        if id is not UNSET:
            field_dict["id"] = id
        if interpretations is not UNSET:
            field_dict["interpretations"] = interpretations
        if item_organisation_unit_groups is not UNSET:
            field_dict["itemOrganisationUnitGroups"] = item_organisation_unit_groups
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if legend is not UNSET:
            field_dict["legend"] = legend
        if measure_criteria is not UNSET:
            field_dict["measureCriteria"] = measure_criteria
        if name is not UNSET:
            field_dict["name"] = name
        if no_space_between_columns is not UNSET:
            field_dict["noSpaceBetweenColumns"] = no_space_between_columns
        if optional_axes is not UNSET:
            field_dict["optionalAxes"] = optional_axes
        if org_unit_field is not UNSET:
            field_dict["orgUnitField"] = org_unit_field
        if organisation_unit_group_set_dimensions is not UNSET:
            field_dict["organisationUnitGroupSetDimensions"] = organisation_unit_group_set_dimensions
        if organisation_unit_levels is not UNSET:
            field_dict["organisationUnitLevels"] = organisation_unit_levels
        if organisation_units is not UNSET:
            field_dict["organisationUnits"] = organisation_units
        if outlier_analysis is not UNSET:
            field_dict["outlierAnalysis"] = outlier_analysis
        if parent_graph_map is not UNSET:
            field_dict["parentGraphMap"] = parent_graph_map
        if percent_stacked_values is not UNSET:
            field_dict["percentStackedValues"] = percent_stacked_values
        if periods is not UNSET:
            field_dict["periods"] = periods
        if program_indicator_dimensions is not UNSET:
            field_dict["programIndicatorDimensions"] = program_indicator_dimensions
        if range_axis_decimals is not UNSET:
            field_dict["rangeAxisDecimals"] = range_axis_decimals
        if range_axis_label is not UNSET:
            field_dict["rangeAxisLabel"] = range_axis_label
        if range_axis_max_value is not UNSET:
            field_dict["rangeAxisMaxValue"] = range_axis_max_value
        if range_axis_min_value is not UNSET:
            field_dict["rangeAxisMinValue"] = range_axis_min_value
        if range_axis_steps is not UNSET:
            field_dict["rangeAxisSteps"] = range_axis_steps
        if regression is not UNSET:
            field_dict["regression"] = regression
        if relative_periods is not UNSET:
            field_dict["relativePeriods"] = relative_periods
        if reporting_params is not UNSET:
            field_dict["reportingParams"] = reporting_params
        if row_dimensions is not UNSET:
            field_dict["rowDimensions"] = row_dimensions
        if row_sub_totals is not UNSET:
            field_dict["rowSubTotals"] = row_sub_totals
        if row_totals is not UNSET:
            field_dict["rowTotals"] = row_totals
        if rows is not UNSET:
            field_dict["rows"] = rows
        if series is not UNSET:
            field_dict["series"] = series
        if series_key is not UNSET:
            field_dict["seriesKey"] = series_key
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if show_data is not UNSET:
            field_dict["showData"] = show_data
        if show_dimension_labels is not UNSET:
            field_dict["showDimensionLabels"] = show_dimension_labels
        if show_hierarchy is not UNSET:
            field_dict["showHierarchy"] = show_hierarchy
        if skip_rounding is not UNSET:
            field_dict["skipRounding"] = skip_rounding
        if sorting is not UNSET:
            field_dict["sorting"] = sorting
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if subscribed is not UNSET:
            field_dict["subscribed"] = subscribed
        if subscribers is not UNSET:
            field_dict["subscribers"] = subscribers
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if target_line_label is not UNSET:
            field_dict["targetLineLabel"] = target_line_label
        if target_line_value is not UNSET:
            field_dict["targetLineValue"] = target_line_value
        if time_field is not UNSET:
            field_dict["timeField"] = time_field
        if title is not UNSET:
            field_dict["title"] = title
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user
        if user_organisation_unit is not UNSET:
            field_dict["userOrganisationUnit"] = user_organisation_unit
        if user_organisation_unit_children is not UNSET:
            field_dict["userOrganisationUnitChildren"] = user_organisation_unit_children
        if user_organisation_unit_grand_children is not UNSET:
            field_dict["userOrganisationUnitGrandChildren"] = user_organisation_unit_grand_children
        if visualization_period_name is not UNSET:
            field_dict["visualizationPeriodName"] = visualization_period_name
        if yearly_series is not UNSET:
            field_dict["yearlySeries"] = yearly_series

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.axis import Axis
        from ..models.axis_v2 import AxisV2
        from ..models.category_dimension import CategoryDimension
        from ..models.category_option_group_set_dimension import CategoryOptionGroupSetDimension
        from ..models.data_dimension_item import DataDimensionItem
        from ..models.data_element_group_set_dimension import DataElementGroupSetDimension
        from ..models.legend_definitions import LegendDefinitions
        from ..models.organisation_unit_group_set_dimension import OrganisationUnitGroupSetDimension
        from ..models.outlier_analysis import OutlierAnalysis
        from ..models.relative_periods import RelativePeriods
        from ..models.reporting_params import ReportingParams
        from ..models.series import Series
        from ..models.series_key import SeriesKey
        from ..models.sharing import Sharing
        from ..models.sorting import Sorting
        from ..models.tracked_entity_attribute_dimension import TrackedEntityAttributeDimension
        from ..models.tracked_entity_data_element_dimension import TrackedEntityDataElementDimension
        from ..models.tracked_entity_program_indicator_dimension import TrackedEntityProgramIndicatorDimension
        from ..models.translation import Translation
        from ..models.visualization_columns_item import VisualizationColumnsItem
        from ..models.visualization_created_by import VisualizationCreatedBy
        from ..models.visualization_filters_item import VisualizationFiltersItem
        from ..models.visualization_font_style import VisualizationFontStyle
        from ..models.visualization_icon import VisualizationIcon
        from ..models.visualization_interpretations_item import VisualizationInterpretationsItem
        from ..models.visualization_item_organisation_unit_groups_item import (
            VisualizationItemOrganisationUnitGroupsItem,
        )
        from ..models.visualization_last_updated_by import VisualizationLastUpdatedBy
        from ..models.visualization_organisation_units_item import VisualizationOrganisationUnitsItem
        from ..models.visualization_parent_graph_map import VisualizationParentGraphMap
        from ..models.visualization_rows_item import VisualizationRowsItem
        from ..models.visualization_user import VisualizationUser

        d = src_dict.copy()
        aggregation_type = VisualizationAggregationType(d.pop("aggregationType"))

        digit_group_separator = VisualizationDigitGroupSeparator(d.pop("digitGroupSeparator"))

        display_density = VisualizationDisplayDensity(d.pop("displayDensity"))

        font_size = VisualizationFontSize(d.pop("fontSize"))

        hide_empty_row_items = VisualizationHideEmptyRowItems(d.pop("hideEmptyRowItems"))

        number_type = VisualizationNumberType(d.pop("numberType"))

        regression_type = VisualizationRegressionType(d.pop("regressionType"))

        sort_order = d.pop("sortOrder")

        top_limit = d.pop("topLimit")

        type_ = VisualizationType(d.pop("type"))

        user_org_unit_type = VisualizationUserOrgUnitType(d.pop("userOrgUnitType"))

        _access = d.pop("access", UNSET)
        access: Union[Unset, Access]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

        attribute_dimensions = []
        _attribute_dimensions = d.pop("attributeDimensions", UNSET)
        for attribute_dimensions_item_data in _attribute_dimensions or []:
            attribute_dimensions_item = TrackedEntityAttributeDimension.from_dict(attribute_dimensions_item_data)

            attribute_dimensions.append(attribute_dimensions_item)

        attribute_values = []
        _attribute_values = d.pop("attributeValues", UNSET)
        for attribute_values_item_data in _attribute_values or []:
            attribute_values_item = AttributeValue.from_dict(attribute_values_item_data)

            attribute_values.append(attribute_values_item)

        axes = []
        _axes = d.pop("axes", UNSET)
        for axes_item_data in _axes or []:
            axes_item = AxisV2.from_dict(axes_item_data)

            axes.append(axes_item)

        base_line_label = d.pop("baseLineLabel", UNSET)

        base_line_value = d.pop("baseLineValue", UNSET)

        category_dimensions = []
        _category_dimensions = d.pop("categoryDimensions", UNSET)
        for category_dimensions_item_data in _category_dimensions or []:
            category_dimensions_item = CategoryDimension.from_dict(category_dimensions_item_data)

            category_dimensions.append(category_dimensions_item)

        category_option_group_set_dimensions = []
        _category_option_group_set_dimensions = d.pop("categoryOptionGroupSetDimensions", UNSET)
        for category_option_group_set_dimensions_item_data in _category_option_group_set_dimensions or []:
            category_option_group_set_dimensions_item = CategoryOptionGroupSetDimension.from_dict(
                category_option_group_set_dimensions_item_data
            )

            category_option_group_set_dimensions.append(category_option_group_set_dimensions_item)

        code = d.pop("code", UNSET)

        col_sub_totals = d.pop("colSubTotals", UNSET)

        col_totals = d.pop("colTotals", UNSET)

        color_set = d.pop("colorSet", UNSET)

        column_dimensions = cast(list[str], d.pop("columnDimensions", UNSET))

        columns = []
        _columns = d.pop("columns", UNSET)
        for columns_item_data in _columns or []:
            columns_item = VisualizationColumnsItem.from_dict(columns_item_data)

            columns.append(columns_item)

        completed_only = d.pop("completedOnly", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, VisualizationCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = VisualizationCreatedBy.from_dict(_created_by)

        cumulative_values = d.pop("cumulativeValues", UNSET)

        data_dimension_items = []
        _data_dimension_items = d.pop("dataDimensionItems", UNSET)
        for data_dimension_items_item_data in _data_dimension_items or []:
            data_dimension_items_item = DataDimensionItem.from_dict(data_dimension_items_item_data)

            data_dimension_items.append(data_dimension_items_item)

        data_element_dimensions = []
        _data_element_dimensions = d.pop("dataElementDimensions", UNSET)
        for data_element_dimensions_item_data in _data_element_dimensions or []:
            data_element_dimensions_item = TrackedEntityDataElementDimension.from_dict(
                data_element_dimensions_item_data
            )

            data_element_dimensions.append(data_element_dimensions_item)

        data_element_group_set_dimensions = []
        _data_element_group_set_dimensions = d.pop("dataElementGroupSetDimensions", UNSET)
        for data_element_group_set_dimensions_item_data in _data_element_group_set_dimensions or []:
            data_element_group_set_dimensions_item = DataElementGroupSetDimension.from_dict(
                data_element_group_set_dimensions_item_data
            )

            data_element_group_set_dimensions.append(data_element_group_set_dimensions_item)

        description = d.pop("description", UNSET)

        display_base_line_label = d.pop("displayBaseLineLabel", UNSET)

        display_description = d.pop("displayDescription", UNSET)

        display_domain_axis_label = d.pop("displayDomainAxisLabel", UNSET)

        display_form_name = d.pop("displayFormName", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_range_axis_label = d.pop("displayRangeAxisLabel", UNSET)

        display_short_name = d.pop("displayShortName", UNSET)

        display_subtitle = d.pop("displaySubtitle", UNSET)

        display_target_line_label = d.pop("displayTargetLineLabel", UNSET)

        display_title = d.pop("displayTitle", UNSET)

        domain_axis_label = d.pop("domainAxisLabel", UNSET)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        filter_dimensions = cast(list[str], d.pop("filterDimensions", UNSET))

        filters = []
        _filters = d.pop("filters", UNSET)
        for filters_item_data in _filters or []:
            filters_item = VisualizationFiltersItem.from_dict(filters_item_data)

            filters.append(filters_item)

        fix_column_headers = d.pop("fixColumnHeaders", UNSET)

        fix_row_headers = d.pop("fixRowHeaders", UNSET)

        _font_style = d.pop("fontStyle", UNSET)
        font_style: Union[Unset, VisualizationFontStyle]
        if isinstance(_font_style, Unset):
            font_style = UNSET
        else:
            font_style = VisualizationFontStyle.from_dict(_font_style)

        form_name = d.pop("formName", UNSET)

        hide_empty_columns = d.pop("hideEmptyColumns", UNSET)

        hide_empty_rows = d.pop("hideEmptyRows", UNSET)

        hide_legend = d.pop("hideLegend", UNSET)

        hide_subtitle = d.pop("hideSubtitle", UNSET)

        hide_title = d.pop("hideTitle", UNSET)

        href = d.pop("href", UNSET)

        icons = []
        _icons = d.pop("icons", UNSET)
        for icons_item_data in _icons or []:
            icons_item = VisualizationIcon.from_dict(icons_item_data)

            icons.append(icons_item)

        id = d.pop("id", UNSET)

        interpretations = []
        _interpretations = d.pop("interpretations", UNSET)
        for interpretations_item_data in _interpretations or []:
            interpretations_item = VisualizationInterpretationsItem.from_dict(interpretations_item_data)

            interpretations.append(interpretations_item)

        item_organisation_unit_groups = []
        _item_organisation_unit_groups = d.pop("itemOrganisationUnitGroups", UNSET)
        for item_organisation_unit_groups_item_data in _item_organisation_unit_groups or []:
            item_organisation_unit_groups_item = VisualizationItemOrganisationUnitGroupsItem.from_dict(
                item_organisation_unit_groups_item_data
            )

            item_organisation_unit_groups.append(item_organisation_unit_groups_item)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, VisualizationLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = VisualizationLastUpdatedBy.from_dict(_last_updated_by)

        _legend = d.pop("legend", UNSET)
        legend: Union[Unset, LegendDefinitions]
        if isinstance(_legend, Unset):
            legend = UNSET
        else:
            legend = LegendDefinitions.from_dict(_legend)

        measure_criteria = d.pop("measureCriteria", UNSET)

        name = d.pop("name", UNSET)

        no_space_between_columns = d.pop("noSpaceBetweenColumns", UNSET)

        optional_axes = []
        _optional_axes = d.pop("optionalAxes", UNSET)
        for optional_axes_item_data in _optional_axes or []:
            optional_axes_item = Axis.from_dict(optional_axes_item_data)

            optional_axes.append(optional_axes_item)

        org_unit_field = d.pop("orgUnitField", UNSET)

        organisation_unit_group_set_dimensions = []
        _organisation_unit_group_set_dimensions = d.pop("organisationUnitGroupSetDimensions", UNSET)
        for organisation_unit_group_set_dimensions_item_data in _organisation_unit_group_set_dimensions or []:
            organisation_unit_group_set_dimensions_item = OrganisationUnitGroupSetDimension.from_dict(
                organisation_unit_group_set_dimensions_item_data
            )

            organisation_unit_group_set_dimensions.append(organisation_unit_group_set_dimensions_item)

        organisation_unit_levels = cast(list[int], d.pop("organisationUnitLevels", UNSET))

        organisation_units = []
        _organisation_units = d.pop("organisationUnits", UNSET)
        for organisation_units_item_data in _organisation_units or []:
            organisation_units_item = VisualizationOrganisationUnitsItem.from_dict(organisation_units_item_data)

            organisation_units.append(organisation_units_item)

        _outlier_analysis = d.pop("outlierAnalysis", UNSET)
        outlier_analysis: Union[Unset, OutlierAnalysis]
        if isinstance(_outlier_analysis, Unset):
            outlier_analysis = UNSET
        else:
            outlier_analysis = OutlierAnalysis.from_dict(_outlier_analysis)

        _parent_graph_map = d.pop("parentGraphMap", UNSET)
        parent_graph_map: Union[Unset, VisualizationParentGraphMap]
        if isinstance(_parent_graph_map, Unset):
            parent_graph_map = UNSET
        else:
            parent_graph_map = VisualizationParentGraphMap.from_dict(_parent_graph_map)

        percent_stacked_values = d.pop("percentStackedValues", UNSET)

        periods = cast(list[str], d.pop("periods", UNSET))

        program_indicator_dimensions = []
        _program_indicator_dimensions = d.pop("programIndicatorDimensions", UNSET)
        for program_indicator_dimensions_item_data in _program_indicator_dimensions or []:
            program_indicator_dimensions_item = TrackedEntityProgramIndicatorDimension.from_dict(
                program_indicator_dimensions_item_data
            )

            program_indicator_dimensions.append(program_indicator_dimensions_item)

        range_axis_decimals = d.pop("rangeAxisDecimals", UNSET)

        range_axis_label = d.pop("rangeAxisLabel", UNSET)

        range_axis_max_value = d.pop("rangeAxisMaxValue", UNSET)

        range_axis_min_value = d.pop("rangeAxisMinValue", UNSET)

        range_axis_steps = d.pop("rangeAxisSteps", UNSET)

        regression = d.pop("regression", UNSET)

        _relative_periods = d.pop("relativePeriods", UNSET)
        relative_periods: Union[Unset, RelativePeriods]
        if isinstance(_relative_periods, Unset):
            relative_periods = UNSET
        else:
            relative_periods = RelativePeriods.from_dict(_relative_periods)

        _reporting_params = d.pop("reportingParams", UNSET)
        reporting_params: Union[Unset, ReportingParams]
        if isinstance(_reporting_params, Unset):
            reporting_params = UNSET
        else:
            reporting_params = ReportingParams.from_dict(_reporting_params)

        row_dimensions = cast(list[str], d.pop("rowDimensions", UNSET))

        row_sub_totals = d.pop("rowSubTotals", UNSET)

        row_totals = d.pop("rowTotals", UNSET)

        rows = []
        _rows = d.pop("rows", UNSET)
        for rows_item_data in _rows or []:
            rows_item = VisualizationRowsItem.from_dict(rows_item_data)

            rows.append(rows_item)

        series = []
        _series = d.pop("series", UNSET)
        for series_item_data in _series or []:
            series_item = Series.from_dict(series_item_data)

            series.append(series_item)

        _series_key = d.pop("seriesKey", UNSET)
        series_key: Union[Unset, SeriesKey]
        if isinstance(_series_key, Unset):
            series_key = UNSET
        else:
            series_key = SeriesKey.from_dict(_series_key)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        short_name = d.pop("shortName", UNSET)

        show_data = d.pop("showData", UNSET)

        show_dimension_labels = d.pop("showDimensionLabels", UNSET)

        show_hierarchy = d.pop("showHierarchy", UNSET)

        skip_rounding = d.pop("skipRounding", UNSET)

        sorting = []
        _sorting = d.pop("sorting", UNSET)
        for sorting_item_data in _sorting or []:
            sorting_item = Sorting.from_dict(sorting_item_data)

            sorting.append(sorting_item)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        subscribed = d.pop("subscribed", UNSET)

        subscribers = cast(list[str], d.pop("subscribers", UNSET))

        subtitle = d.pop("subtitle", UNSET)

        target_line_label = d.pop("targetLineLabel", UNSET)

        target_line_value = d.pop("targetLineValue", UNSET)

        time_field = d.pop("timeField", UNSET)

        title = d.pop("title", UNSET)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, VisualizationUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = VisualizationUser.from_dict(_user)

        user_organisation_unit = d.pop("userOrganisationUnit", UNSET)

        user_organisation_unit_children = d.pop("userOrganisationUnitChildren", UNSET)

        user_organisation_unit_grand_children = d.pop("userOrganisationUnitGrandChildren", UNSET)

        visualization_period_name = d.pop("visualizationPeriodName", UNSET)

        yearly_series = cast(list[str], d.pop("yearlySeries", UNSET))

        visualization = cls(
            aggregation_type=aggregation_type,
            digit_group_separator=digit_group_separator,
            display_density=display_density,
            font_size=font_size,
            hide_empty_row_items=hide_empty_row_items,
            number_type=number_type,
            regression_type=regression_type,
            sort_order=sort_order,
            top_limit=top_limit,
            type_=type_,
            user_org_unit_type=user_org_unit_type,
            access=access,
            attribute_dimensions=attribute_dimensions,
            attribute_values=attribute_values,
            axes=axes,
            base_line_label=base_line_label,
            base_line_value=base_line_value,
            category_dimensions=category_dimensions,
            category_option_group_set_dimensions=category_option_group_set_dimensions,
            code=code,
            col_sub_totals=col_sub_totals,
            col_totals=col_totals,
            color_set=color_set,
            column_dimensions=column_dimensions,
            columns=columns,
            completed_only=completed_only,
            created=created,
            created_by=created_by,
            cumulative_values=cumulative_values,
            data_dimension_items=data_dimension_items,
            data_element_dimensions=data_element_dimensions,
            data_element_group_set_dimensions=data_element_group_set_dimensions,
            description=description,
            display_base_line_label=display_base_line_label,
            display_description=display_description,
            display_domain_axis_label=display_domain_axis_label,
            display_form_name=display_form_name,
            display_name=display_name,
            display_range_axis_label=display_range_axis_label,
            display_short_name=display_short_name,
            display_subtitle=display_subtitle,
            display_target_line_label=display_target_line_label,
            display_title=display_title,
            domain_axis_label=domain_axis_label,
            end_date=end_date,
            favorite=favorite,
            favorites=favorites,
            filter_dimensions=filter_dimensions,
            filters=filters,
            fix_column_headers=fix_column_headers,
            fix_row_headers=fix_row_headers,
            font_style=font_style,
            form_name=form_name,
            hide_empty_columns=hide_empty_columns,
            hide_empty_rows=hide_empty_rows,
            hide_legend=hide_legend,
            hide_subtitle=hide_subtitle,
            hide_title=hide_title,
            href=href,
            icons=icons,
            id=id,
            interpretations=interpretations,
            item_organisation_unit_groups=item_organisation_unit_groups,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            legend=legend,
            measure_criteria=measure_criteria,
            name=name,
            no_space_between_columns=no_space_between_columns,
            optional_axes=optional_axes,
            org_unit_field=org_unit_field,
            organisation_unit_group_set_dimensions=organisation_unit_group_set_dimensions,
            organisation_unit_levels=organisation_unit_levels,
            organisation_units=organisation_units,
            outlier_analysis=outlier_analysis,
            parent_graph_map=parent_graph_map,
            percent_stacked_values=percent_stacked_values,
            periods=periods,
            program_indicator_dimensions=program_indicator_dimensions,
            range_axis_decimals=range_axis_decimals,
            range_axis_label=range_axis_label,
            range_axis_max_value=range_axis_max_value,
            range_axis_min_value=range_axis_min_value,
            range_axis_steps=range_axis_steps,
            regression=regression,
            relative_periods=relative_periods,
            reporting_params=reporting_params,
            row_dimensions=row_dimensions,
            row_sub_totals=row_sub_totals,
            row_totals=row_totals,
            rows=rows,
            series=series,
            series_key=series_key,
            sharing=sharing,
            short_name=short_name,
            show_data=show_data,
            show_dimension_labels=show_dimension_labels,
            show_hierarchy=show_hierarchy,
            skip_rounding=skip_rounding,
            sorting=sorting,
            start_date=start_date,
            subscribed=subscribed,
            subscribers=subscribers,
            subtitle=subtitle,
            target_line_label=target_line_label,
            target_line_value=target_line_value,
            time_field=time_field,
            title=title,
            translations=translations,
            user=user,
            user_organisation_unit=user_organisation_unit,
            user_organisation_unit_children=user_organisation_unit_children,
            user_organisation_unit_grand_children=user_organisation_unit_grand_children,
            visualization_period_name=visualization_period_name,
            yearly_series=yearly_series,
        )

        visualization.additional_properties = d
        return visualization

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
