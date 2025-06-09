import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.map_view_aggregation_type import MapViewAggregationType
from ..models.map_view_digit_group_separator import MapViewDigitGroupSeparator
from ..models.map_view_event_status import MapViewEventStatus
from ..models.map_view_hide_empty_row_items import MapViewHideEmptyRowItems
from ..models.map_view_organisation_unit_selection_mode import MapViewOrganisationUnitSelectionMode
from ..models.map_view_program_status import MapViewProgramStatus
from ..models.map_view_regression_type import MapViewRegressionType
from ..models.map_view_rendering_strategy import MapViewRenderingStrategy
from ..models.map_view_thematic_map_type import MapViewThematicMapType
from ..models.map_view_user_org_unit_type import MapViewUserOrgUnitType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.category_dimension import CategoryDimension
    from ..models.category_option_group_set_dimension import CategoryOptionGroupSetDimension
    from ..models.data_dimension_item import DataDimensionItem
    from ..models.data_element_group_set_dimension import DataElementGroupSetDimension
    from ..models.legend_definitions import LegendDefinitions
    from ..models.map_view_columns_item import MapViewColumnsItem
    from ..models.map_view_created_by import MapViewCreatedBy
    from ..models.map_view_filters_item import MapViewFiltersItem
    from ..models.map_view_interpretations_item import MapViewInterpretationsItem
    from ..models.map_view_item_organisation_unit_groups_item import MapViewItemOrganisationUnitGroupsItem
    from ..models.map_view_last_updated_by import MapViewLastUpdatedBy
    from ..models.map_view_legend_set import MapViewLegendSet
    from ..models.map_view_organisation_unit_group_set import MapViewOrganisationUnitGroupSet
    from ..models.map_view_organisation_units_item import MapViewOrganisationUnitsItem
    from ..models.map_view_parent_graph_map import MapViewParentGraphMap
    from ..models.map_view_program import MapViewProgram
    from ..models.map_view_program_stage import MapViewProgramStage
    from ..models.map_view_rows_item import MapViewRowsItem
    from ..models.map_view_style_data_item import MapViewStyleDataItem
    from ..models.map_view_tracked_entity_type import MapViewTrackedEntityType
    from ..models.map_view_user import MapViewUser
    from ..models.organisation_unit_group_set_dimension import OrganisationUnitGroupSetDimension
    from ..models.relative_periods import RelativePeriods
    from ..models.sharing import Sharing
    from ..models.tracked_entity_attribute_dimension import TrackedEntityAttributeDimension
    from ..models.tracked_entity_data_element_dimension import TrackedEntityDataElementDimension
    from ..models.tracked_entity_program_indicator_dimension import TrackedEntityProgramIndicatorDimension
    from ..models.translation import Translation


T = TypeVar("T", bound="MapView")


@_attrs_define
class MapView:
    """
    Attributes:
        aggregation_type (MapViewAggregationType):
        digit_group_separator (MapViewDigitGroupSeparator):
        event_point_radius (int):
        event_status (MapViewEventStatus):
        hide_empty_row_items (MapViewHideEmptyRowItems):
        organisation_unit_selection_mode (MapViewOrganisationUnitSelectionMode):
        parent_level (int):
        program_status (MapViewProgramStatus):
        regression_type (MapViewRegressionType):
        rendering_strategy (MapViewRenderingStrategy):
        sort_order (int):
        thematic_map_type (MapViewThematicMapType):
        top_limit (int):
        user_org_unit_type (MapViewUserOrgUnitType):
        access (Union[Unset, Access]):
        area_radius (Union[Unset, int]):
        attribute_dimensions (Union[Unset, list['TrackedEntityAttributeDimension']]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        category_dimensions (Union[Unset, list['CategoryDimension']]):
        category_option_group_set_dimensions (Union[Unset, list['CategoryOptionGroupSetDimension']]):
        classes (Union[Unset, int]):
        code (Union[Unset, str]):
        col_sub_totals (Union[Unset, bool]):
        col_totals (Union[Unset, bool]):
        color_high (Union[Unset, str]):
        color_low (Union[Unset, str]):
        color_scale (Union[Unset, str]):
        column_dimensions (Union[Unset, list[str]]):
        columns (Union[Unset, list['MapViewColumnsItem']]):
        completed_only (Union[Unset, bool]):
        config (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, MapViewCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        cumulative_values (Union[Unset, bool]):
        data_dimension_items (Union[Unset, list['DataDimensionItem']]):
        data_element_dimensions (Union[Unset, list['TrackedEntityDataElementDimension']]):
        data_element_group_set_dimensions (Union[Unset, list['DataElementGroupSetDimension']]):
        description (Union[Unset, str]):
        display_base_line_label (Union[Unset, str]):
        display_description (Union[Unset, str]):
        display_form_name (Union[Unset, str]):
        display_name (Union[Unset, str]):
        display_short_name (Union[Unset, str]):
        display_subtitle (Union[Unset, str]):
        display_target_line_label (Union[Unset, str]):
        display_title (Union[Unset, str]):
        end_date (Union[Unset, datetime.datetime]):
        event_clustering (Union[Unset, bool]):
        event_coordinate_field (Union[Unset, str]):
        event_point_color (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        filter_dimensions (Union[Unset, list[str]]):
        filters (Union[Unset, list['MapViewFiltersItem']]):
        follow_up (Union[Unset, bool]):
        form_name (Union[Unset, str]):
        hidden (Union[Unset, bool]):
        hide_empty_rows (Union[Unset, bool]):
        hide_legend (Union[Unset, bool]):
        hide_subtitle (Union[Unset, bool]):
        hide_title (Union[Unset, bool]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        interpretations (Union[Unset, list['MapViewInterpretationsItem']]):
        item_organisation_unit_groups (Union[Unset, list['MapViewItemOrganisationUnitGroupsItem']]):
        label_font_color (Union[Unset, str]):
        label_font_size (Union[Unset, str]):
        label_font_style (Union[Unset, str]):
        label_font_weight (Union[Unset, str]):
        label_template (Union[Unset, str]):
        labels (Union[Unset, bool]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, MapViewLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        layer (Union[Unset, str]):
        legend (Union[Unset, LegendDefinitions]):
        legend_set (Union[Unset, MapViewLegendSet]): A UID reference to a LegendSet
            (Java name `org.hisp.dhis.legend.LegendSet`)
        method (Union[Unset, int]):
        no_data_color (Union[Unset, str]):
        no_space_between_columns (Union[Unset, bool]):
        opacity (Union[Unset, float]):
        org_unit_field (Union[Unset, str]):
        org_unit_field_display_name (Union[Unset, str]):
        organisation_unit_color (Union[Unset, str]):
        organisation_unit_group_set (Union[Unset, MapViewOrganisationUnitGroupSet]): A UID reference to a
            OrganisationUnitGroupSet
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnitGroupSet`)
        organisation_unit_group_set_dimensions (Union[Unset, list['OrganisationUnitGroupSetDimension']]):
        organisation_unit_levels (Union[Unset, list[int]]):
        organisation_units (Union[Unset, list['MapViewOrganisationUnitsItem']]):
        parent_graph (Union[Unset, str]):
        parent_graph_map (Union[Unset, MapViewParentGraphMap]):
        percent_stacked_values (Union[Unset, bool]):
        periods (Union[Unset, list[str]]):
        program (Union[Unset, MapViewProgram]): A UID reference to a Program
            (Java name `org.hisp.dhis.program.Program`)
        program_indicator_dimensions (Union[Unset, list['TrackedEntityProgramIndicatorDimension']]):
        program_stage (Union[Unset, MapViewProgramStage]): A UID reference to a ProgramStage
            (Java name `org.hisp.dhis.program.ProgramStage`)
        radius_high (Union[Unset, int]):
        radius_low (Union[Unset, int]):
        relative_periods (Union[Unset, RelativePeriods]):
        row_sub_totals (Union[Unset, bool]):
        row_totals (Union[Unset, bool]):
        rows (Union[Unset, list['MapViewRowsItem']]):
        sharing (Union[Unset, Sharing]):
        short_name (Union[Unset, str]):
        show_data (Union[Unset, bool]):
        show_dimension_labels (Union[Unset, bool]):
        show_hierarchy (Union[Unset, bool]):
        skip_rounding (Union[Unset, bool]):
        start_date (Union[Unset, datetime.datetime]):
        style_data_item (Union[Unset, MapViewStyleDataItem]): The actual type is unknown.
            (Java type was: `class java.lang.Object`)
        subscribed (Union[Unset, bool]):
        subscribers (Union[Unset, list[str]]):
        subtitle (Union[Unset, str]):
        time_field (Union[Unset, str]):
        title (Union[Unset, str]):
        tracked_entity_type (Union[Unset, MapViewTrackedEntityType]): A UID reference to a TrackedEntityType
            (Java name `org.hisp.dhis.trackedentity.TrackedEntityType`)
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, MapViewUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        user_organisation_unit (Union[Unset, bool]):
        user_organisation_unit_children (Union[Unset, bool]):
        user_organisation_unit_grand_children (Union[Unset, bool]):
    """

    aggregation_type: MapViewAggregationType
    digit_group_separator: MapViewDigitGroupSeparator
    event_point_radius: int
    event_status: MapViewEventStatus
    hide_empty_row_items: MapViewHideEmptyRowItems
    organisation_unit_selection_mode: MapViewOrganisationUnitSelectionMode
    parent_level: int
    program_status: MapViewProgramStatus
    regression_type: MapViewRegressionType
    rendering_strategy: MapViewRenderingStrategy
    sort_order: int
    thematic_map_type: MapViewThematicMapType
    top_limit: int
    user_org_unit_type: MapViewUserOrgUnitType
    access: Union[Unset, "Access"] = UNSET
    area_radius: Union[Unset, int] = UNSET
    attribute_dimensions: Union[Unset, list["TrackedEntityAttributeDimension"]] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    category_dimensions: Union[Unset, list["CategoryDimension"]] = UNSET
    category_option_group_set_dimensions: Union[Unset, list["CategoryOptionGroupSetDimension"]] = UNSET
    classes: Union[Unset, int] = UNSET
    code: Union[Unset, str] = UNSET
    col_sub_totals: Union[Unset, bool] = UNSET
    col_totals: Union[Unset, bool] = UNSET
    color_high: Union[Unset, str] = UNSET
    color_low: Union[Unset, str] = UNSET
    color_scale: Union[Unset, str] = UNSET
    column_dimensions: Union[Unset, list[str]] = UNSET
    columns: Union[Unset, list["MapViewColumnsItem"]] = UNSET
    completed_only: Union[Unset, bool] = UNSET
    config: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "MapViewCreatedBy"] = UNSET
    cumulative_values: Union[Unset, bool] = UNSET
    data_dimension_items: Union[Unset, list["DataDimensionItem"]] = UNSET
    data_element_dimensions: Union[Unset, list["TrackedEntityDataElementDimension"]] = UNSET
    data_element_group_set_dimensions: Union[Unset, list["DataElementGroupSetDimension"]] = UNSET
    description: Union[Unset, str] = UNSET
    display_base_line_label: Union[Unset, str] = UNSET
    display_description: Union[Unset, str] = UNSET
    display_form_name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    display_short_name: Union[Unset, str] = UNSET
    display_subtitle: Union[Unset, str] = UNSET
    display_target_line_label: Union[Unset, str] = UNSET
    display_title: Union[Unset, str] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    event_clustering: Union[Unset, bool] = UNSET
    event_coordinate_field: Union[Unset, str] = UNSET
    event_point_color: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    filter_dimensions: Union[Unset, list[str]] = UNSET
    filters: Union[Unset, list["MapViewFiltersItem"]] = UNSET
    follow_up: Union[Unset, bool] = UNSET
    form_name: Union[Unset, str] = UNSET
    hidden: Union[Unset, bool] = UNSET
    hide_empty_rows: Union[Unset, bool] = UNSET
    hide_legend: Union[Unset, bool] = UNSET
    hide_subtitle: Union[Unset, bool] = UNSET
    hide_title: Union[Unset, bool] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    interpretations: Union[Unset, list["MapViewInterpretationsItem"]] = UNSET
    item_organisation_unit_groups: Union[Unset, list["MapViewItemOrganisationUnitGroupsItem"]] = UNSET
    label_font_color: Union[Unset, str] = UNSET
    label_font_size: Union[Unset, str] = UNSET
    label_font_style: Union[Unset, str] = UNSET
    label_font_weight: Union[Unset, str] = UNSET
    label_template: Union[Unset, str] = UNSET
    labels: Union[Unset, bool] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "MapViewLastUpdatedBy"] = UNSET
    layer: Union[Unset, str] = UNSET
    legend: Union[Unset, "LegendDefinitions"] = UNSET
    legend_set: Union[Unset, "MapViewLegendSet"] = UNSET
    method: Union[Unset, int] = UNSET
    no_data_color: Union[Unset, str] = UNSET
    no_space_between_columns: Union[Unset, bool] = UNSET
    opacity: Union[Unset, float] = UNSET
    org_unit_field: Union[Unset, str] = UNSET
    org_unit_field_display_name: Union[Unset, str] = UNSET
    organisation_unit_color: Union[Unset, str] = UNSET
    organisation_unit_group_set: Union[Unset, "MapViewOrganisationUnitGroupSet"] = UNSET
    organisation_unit_group_set_dimensions: Union[Unset, list["OrganisationUnitGroupSetDimension"]] = UNSET
    organisation_unit_levels: Union[Unset, list[int]] = UNSET
    organisation_units: Union[Unset, list["MapViewOrganisationUnitsItem"]] = UNSET
    parent_graph: Union[Unset, str] = UNSET
    parent_graph_map: Union[Unset, "MapViewParentGraphMap"] = UNSET
    percent_stacked_values: Union[Unset, bool] = UNSET
    periods: Union[Unset, list[str]] = UNSET
    program: Union[Unset, "MapViewProgram"] = UNSET
    program_indicator_dimensions: Union[Unset, list["TrackedEntityProgramIndicatorDimension"]] = UNSET
    program_stage: Union[Unset, "MapViewProgramStage"] = UNSET
    radius_high: Union[Unset, int] = UNSET
    radius_low: Union[Unset, int] = UNSET
    relative_periods: Union[Unset, "RelativePeriods"] = UNSET
    row_sub_totals: Union[Unset, bool] = UNSET
    row_totals: Union[Unset, bool] = UNSET
    rows: Union[Unset, list["MapViewRowsItem"]] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    short_name: Union[Unset, str] = UNSET
    show_data: Union[Unset, bool] = UNSET
    show_dimension_labels: Union[Unset, bool] = UNSET
    show_hierarchy: Union[Unset, bool] = UNSET
    skip_rounding: Union[Unset, bool] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    style_data_item: Union[Unset, "MapViewStyleDataItem"] = UNSET
    subscribed: Union[Unset, bool] = UNSET
    subscribers: Union[Unset, list[str]] = UNSET
    subtitle: Union[Unset, str] = UNSET
    time_field: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    tracked_entity_type: Union[Unset, "MapViewTrackedEntityType"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "MapViewUser"] = UNSET
    user_organisation_unit: Union[Unset, bool] = UNSET
    user_organisation_unit_children: Union[Unset, bool] = UNSET
    user_organisation_unit_grand_children: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregation_type = self.aggregation_type.value

        digit_group_separator = self.digit_group_separator.value

        event_point_radius = self.event_point_radius

        event_status = self.event_status.value

        hide_empty_row_items = self.hide_empty_row_items.value

        organisation_unit_selection_mode = self.organisation_unit_selection_mode.value

        parent_level = self.parent_level

        program_status = self.program_status.value

        regression_type = self.regression_type.value

        rendering_strategy = self.rendering_strategy.value

        sort_order = self.sort_order

        thematic_map_type = self.thematic_map_type.value

        top_limit = self.top_limit

        user_org_unit_type = self.user_org_unit_type.value

        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        area_radius = self.area_radius

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

        classes = self.classes

        code = self.code

        col_sub_totals = self.col_sub_totals

        col_totals = self.col_totals

        color_high = self.color_high

        color_low = self.color_low

        color_scale = self.color_scale

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

        config = self.config

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

        display_form_name = self.display_form_name

        display_name = self.display_name

        display_short_name = self.display_short_name

        display_subtitle = self.display_subtitle

        display_target_line_label = self.display_target_line_label

        display_title = self.display_title

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        event_clustering = self.event_clustering

        event_coordinate_field = self.event_coordinate_field

        event_point_color = self.event_point_color

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

        follow_up = self.follow_up

        form_name = self.form_name

        hidden = self.hidden

        hide_empty_rows = self.hide_empty_rows

        hide_legend = self.hide_legend

        hide_subtitle = self.hide_subtitle

        hide_title = self.hide_title

        href = self.href

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

        label_font_color = self.label_font_color

        label_font_size = self.label_font_size

        label_font_style = self.label_font_style

        label_font_weight = self.label_font_weight

        label_template = self.label_template

        labels = self.labels

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        layer = self.layer

        legend: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.legend, Unset):
            legend = self.legend.to_dict()

        legend_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.legend_set, Unset):
            legend_set = self.legend_set.to_dict()

        method = self.method

        no_data_color = self.no_data_color

        no_space_between_columns = self.no_space_between_columns

        opacity = self.opacity

        org_unit_field = self.org_unit_field

        org_unit_field_display_name = self.org_unit_field_display_name

        organisation_unit_color = self.organisation_unit_color

        organisation_unit_group_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organisation_unit_group_set, Unset):
            organisation_unit_group_set = self.organisation_unit_group_set.to_dict()

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

        parent_graph = self.parent_graph

        parent_graph_map: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_graph_map, Unset):
            parent_graph_map = self.parent_graph_map.to_dict()

        percent_stacked_values = self.percent_stacked_values

        periods: Union[Unset, list[str]] = UNSET
        if not isinstance(self.periods, Unset):
            periods = self.periods

        program: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program, Unset):
            program = self.program.to_dict()

        program_indicator_dimensions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.program_indicator_dimensions, Unset):
            program_indicator_dimensions = []
            for program_indicator_dimensions_item_data in self.program_indicator_dimensions:
                program_indicator_dimensions_item = program_indicator_dimensions_item_data.to_dict()
                program_indicator_dimensions.append(program_indicator_dimensions_item)

        program_stage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program_stage, Unset):
            program_stage = self.program_stage.to_dict()

        radius_high = self.radius_high

        radius_low = self.radius_low

        relative_periods: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.relative_periods, Unset):
            relative_periods = self.relative_periods.to_dict()

        row_sub_totals = self.row_sub_totals

        row_totals = self.row_totals

        rows: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        short_name = self.short_name

        show_data = self.show_data

        show_dimension_labels = self.show_dimension_labels

        show_hierarchy = self.show_hierarchy

        skip_rounding = self.skip_rounding

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        style_data_item: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.style_data_item, Unset):
            style_data_item = self.style_data_item.to_dict()

        subscribed = self.subscribed

        subscribers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.subscribers, Unset):
            subscribers = self.subscribers

        subtitle = self.subtitle

        time_field = self.time_field

        title = self.title

        tracked_entity_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tracked_entity_type, Unset):
            tracked_entity_type = self.tracked_entity_type.to_dict()

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aggregationType": aggregation_type,
                "digitGroupSeparator": digit_group_separator,
                "eventPointRadius": event_point_radius,
                "eventStatus": event_status,
                "hideEmptyRowItems": hide_empty_row_items,
                "organisationUnitSelectionMode": organisation_unit_selection_mode,
                "parentLevel": parent_level,
                "programStatus": program_status,
                "regressionType": regression_type,
                "renderingStrategy": rendering_strategy,
                "sortOrder": sort_order,
                "thematicMapType": thematic_map_type,
                "topLimit": top_limit,
                "userOrgUnitType": user_org_unit_type,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if area_radius is not UNSET:
            field_dict["areaRadius"] = area_radius
        if attribute_dimensions is not UNSET:
            field_dict["attributeDimensions"] = attribute_dimensions
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if category_dimensions is not UNSET:
            field_dict["categoryDimensions"] = category_dimensions
        if category_option_group_set_dimensions is not UNSET:
            field_dict["categoryOptionGroupSetDimensions"] = category_option_group_set_dimensions
        if classes is not UNSET:
            field_dict["classes"] = classes
        if code is not UNSET:
            field_dict["code"] = code
        if col_sub_totals is not UNSET:
            field_dict["colSubTotals"] = col_sub_totals
        if col_totals is not UNSET:
            field_dict["colTotals"] = col_totals
        if color_high is not UNSET:
            field_dict["colorHigh"] = color_high
        if color_low is not UNSET:
            field_dict["colorLow"] = color_low
        if color_scale is not UNSET:
            field_dict["colorScale"] = color_scale
        if column_dimensions is not UNSET:
            field_dict["columnDimensions"] = column_dimensions
        if columns is not UNSET:
            field_dict["columns"] = columns
        if completed_only is not UNSET:
            field_dict["completedOnly"] = completed_only
        if config is not UNSET:
            field_dict["config"] = config
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
        if display_form_name is not UNSET:
            field_dict["displayFormName"] = display_form_name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_short_name is not UNSET:
            field_dict["displayShortName"] = display_short_name
        if display_subtitle is not UNSET:
            field_dict["displaySubtitle"] = display_subtitle
        if display_target_line_label is not UNSET:
            field_dict["displayTargetLineLabel"] = display_target_line_label
        if display_title is not UNSET:
            field_dict["displayTitle"] = display_title
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if event_clustering is not UNSET:
            field_dict["eventClustering"] = event_clustering
        if event_coordinate_field is not UNSET:
            field_dict["eventCoordinateField"] = event_coordinate_field
        if event_point_color is not UNSET:
            field_dict["eventPointColor"] = event_point_color
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if filter_dimensions is not UNSET:
            field_dict["filterDimensions"] = filter_dimensions
        if filters is not UNSET:
            field_dict["filters"] = filters
        if follow_up is not UNSET:
            field_dict["followUp"] = follow_up
        if form_name is not UNSET:
            field_dict["formName"] = form_name
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
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
        if id is not UNSET:
            field_dict["id"] = id
        if interpretations is not UNSET:
            field_dict["interpretations"] = interpretations
        if item_organisation_unit_groups is not UNSET:
            field_dict["itemOrganisationUnitGroups"] = item_organisation_unit_groups
        if label_font_color is not UNSET:
            field_dict["labelFontColor"] = label_font_color
        if label_font_size is not UNSET:
            field_dict["labelFontSize"] = label_font_size
        if label_font_style is not UNSET:
            field_dict["labelFontStyle"] = label_font_style
        if label_font_weight is not UNSET:
            field_dict["labelFontWeight"] = label_font_weight
        if label_template is not UNSET:
            field_dict["labelTemplate"] = label_template
        if labels is not UNSET:
            field_dict["labels"] = labels
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if layer is not UNSET:
            field_dict["layer"] = layer
        if legend is not UNSET:
            field_dict["legend"] = legend
        if legend_set is not UNSET:
            field_dict["legendSet"] = legend_set
        if method is not UNSET:
            field_dict["method"] = method
        if no_data_color is not UNSET:
            field_dict["noDataColor"] = no_data_color
        if no_space_between_columns is not UNSET:
            field_dict["noSpaceBetweenColumns"] = no_space_between_columns
        if opacity is not UNSET:
            field_dict["opacity"] = opacity
        if org_unit_field is not UNSET:
            field_dict["orgUnitField"] = org_unit_field
        if org_unit_field_display_name is not UNSET:
            field_dict["orgUnitFieldDisplayName"] = org_unit_field_display_name
        if organisation_unit_color is not UNSET:
            field_dict["organisationUnitColor"] = organisation_unit_color
        if organisation_unit_group_set is not UNSET:
            field_dict["organisationUnitGroupSet"] = organisation_unit_group_set
        if organisation_unit_group_set_dimensions is not UNSET:
            field_dict["organisationUnitGroupSetDimensions"] = organisation_unit_group_set_dimensions
        if organisation_unit_levels is not UNSET:
            field_dict["organisationUnitLevels"] = organisation_unit_levels
        if organisation_units is not UNSET:
            field_dict["organisationUnits"] = organisation_units
        if parent_graph is not UNSET:
            field_dict["parentGraph"] = parent_graph
        if parent_graph_map is not UNSET:
            field_dict["parentGraphMap"] = parent_graph_map
        if percent_stacked_values is not UNSET:
            field_dict["percentStackedValues"] = percent_stacked_values
        if periods is not UNSET:
            field_dict["periods"] = periods
        if program is not UNSET:
            field_dict["program"] = program
        if program_indicator_dimensions is not UNSET:
            field_dict["programIndicatorDimensions"] = program_indicator_dimensions
        if program_stage is not UNSET:
            field_dict["programStage"] = program_stage
        if radius_high is not UNSET:
            field_dict["radiusHigh"] = radius_high
        if radius_low is not UNSET:
            field_dict["radiusLow"] = radius_low
        if relative_periods is not UNSET:
            field_dict["relativePeriods"] = relative_periods
        if row_sub_totals is not UNSET:
            field_dict["rowSubTotals"] = row_sub_totals
        if row_totals is not UNSET:
            field_dict["rowTotals"] = row_totals
        if rows is not UNSET:
            field_dict["rows"] = rows
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
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if style_data_item is not UNSET:
            field_dict["styleDataItem"] = style_data_item
        if subscribed is not UNSET:
            field_dict["subscribed"] = subscribed
        if subscribers is not UNSET:
            field_dict["subscribers"] = subscribers
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if time_field is not UNSET:
            field_dict["timeField"] = time_field
        if title is not UNSET:
            field_dict["title"] = title
        if tracked_entity_type is not UNSET:
            field_dict["trackedEntityType"] = tracked_entity_type
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.category_dimension import CategoryDimension
        from ..models.category_option_group_set_dimension import CategoryOptionGroupSetDimension
        from ..models.data_dimension_item import DataDimensionItem
        from ..models.data_element_group_set_dimension import DataElementGroupSetDimension
        from ..models.legend_definitions import LegendDefinitions
        from ..models.map_view_columns_item import MapViewColumnsItem
        from ..models.map_view_created_by import MapViewCreatedBy
        from ..models.map_view_filters_item import MapViewFiltersItem
        from ..models.map_view_interpretations_item import MapViewInterpretationsItem
        from ..models.map_view_item_organisation_unit_groups_item import MapViewItemOrganisationUnitGroupsItem
        from ..models.map_view_last_updated_by import MapViewLastUpdatedBy
        from ..models.map_view_legend_set import MapViewLegendSet
        from ..models.map_view_organisation_unit_group_set import MapViewOrganisationUnitGroupSet
        from ..models.map_view_organisation_units_item import MapViewOrganisationUnitsItem
        from ..models.map_view_parent_graph_map import MapViewParentGraphMap
        from ..models.map_view_program import MapViewProgram
        from ..models.map_view_program_stage import MapViewProgramStage
        from ..models.map_view_rows_item import MapViewRowsItem
        from ..models.map_view_style_data_item import MapViewStyleDataItem
        from ..models.map_view_tracked_entity_type import MapViewTrackedEntityType
        from ..models.map_view_user import MapViewUser
        from ..models.organisation_unit_group_set_dimension import OrganisationUnitGroupSetDimension
        from ..models.relative_periods import RelativePeriods
        from ..models.sharing import Sharing
        from ..models.tracked_entity_attribute_dimension import TrackedEntityAttributeDimension
        from ..models.tracked_entity_data_element_dimension import TrackedEntityDataElementDimension
        from ..models.tracked_entity_program_indicator_dimension import TrackedEntityProgramIndicatorDimension
        from ..models.translation import Translation

        d = src_dict.copy()
        aggregation_type = MapViewAggregationType(d.pop("aggregationType"))

        digit_group_separator = MapViewDigitGroupSeparator(d.pop("digitGroupSeparator"))

        event_point_radius = d.pop("eventPointRadius")

        event_status = MapViewEventStatus(d.pop("eventStatus"))

        hide_empty_row_items = MapViewHideEmptyRowItems(d.pop("hideEmptyRowItems"))

        organisation_unit_selection_mode = MapViewOrganisationUnitSelectionMode(d.pop("organisationUnitSelectionMode"))

        parent_level = d.pop("parentLevel")

        program_status = MapViewProgramStatus(d.pop("programStatus"))

        regression_type = MapViewRegressionType(d.pop("regressionType"))

        rendering_strategy = MapViewRenderingStrategy(d.pop("renderingStrategy"))

        sort_order = d.pop("sortOrder")

        thematic_map_type = MapViewThematicMapType(d.pop("thematicMapType"))

        top_limit = d.pop("topLimit")

        user_org_unit_type = MapViewUserOrgUnitType(d.pop("userOrgUnitType"))

        _access = d.pop("access", UNSET)
        access: Union[Unset, Access]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

        area_radius = d.pop("areaRadius", UNSET)

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

        classes = d.pop("classes", UNSET)

        code = d.pop("code", UNSET)

        col_sub_totals = d.pop("colSubTotals", UNSET)

        col_totals = d.pop("colTotals", UNSET)

        color_high = d.pop("colorHigh", UNSET)

        color_low = d.pop("colorLow", UNSET)

        color_scale = d.pop("colorScale", UNSET)

        column_dimensions = cast(list[str], d.pop("columnDimensions", UNSET))

        columns = []
        _columns = d.pop("columns", UNSET)
        for columns_item_data in _columns or []:
            columns_item = MapViewColumnsItem.from_dict(columns_item_data)

            columns.append(columns_item)

        completed_only = d.pop("completedOnly", UNSET)

        config = d.pop("config", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, MapViewCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = MapViewCreatedBy.from_dict(_created_by)

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

        display_form_name = d.pop("displayFormName", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_short_name = d.pop("displayShortName", UNSET)

        display_subtitle = d.pop("displaySubtitle", UNSET)

        display_target_line_label = d.pop("displayTargetLineLabel", UNSET)

        display_title = d.pop("displayTitle", UNSET)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        event_clustering = d.pop("eventClustering", UNSET)

        event_coordinate_field = d.pop("eventCoordinateField", UNSET)

        event_point_color = d.pop("eventPointColor", UNSET)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        filter_dimensions = cast(list[str], d.pop("filterDimensions", UNSET))

        filters = []
        _filters = d.pop("filters", UNSET)
        for filters_item_data in _filters or []:
            filters_item = MapViewFiltersItem.from_dict(filters_item_data)

            filters.append(filters_item)

        follow_up = d.pop("followUp", UNSET)

        form_name = d.pop("formName", UNSET)

        hidden = d.pop("hidden", UNSET)

        hide_empty_rows = d.pop("hideEmptyRows", UNSET)

        hide_legend = d.pop("hideLegend", UNSET)

        hide_subtitle = d.pop("hideSubtitle", UNSET)

        hide_title = d.pop("hideTitle", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        interpretations = []
        _interpretations = d.pop("interpretations", UNSET)
        for interpretations_item_data in _interpretations or []:
            interpretations_item = MapViewInterpretationsItem.from_dict(interpretations_item_data)

            interpretations.append(interpretations_item)

        item_organisation_unit_groups = []
        _item_organisation_unit_groups = d.pop("itemOrganisationUnitGroups", UNSET)
        for item_organisation_unit_groups_item_data in _item_organisation_unit_groups or []:
            item_organisation_unit_groups_item = MapViewItemOrganisationUnitGroupsItem.from_dict(
                item_organisation_unit_groups_item_data
            )

            item_organisation_unit_groups.append(item_organisation_unit_groups_item)

        label_font_color = d.pop("labelFontColor", UNSET)

        label_font_size = d.pop("labelFontSize", UNSET)

        label_font_style = d.pop("labelFontStyle", UNSET)

        label_font_weight = d.pop("labelFontWeight", UNSET)

        label_template = d.pop("labelTemplate", UNSET)

        labels = d.pop("labels", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, MapViewLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = MapViewLastUpdatedBy.from_dict(_last_updated_by)

        layer = d.pop("layer", UNSET)

        _legend = d.pop("legend", UNSET)
        legend: Union[Unset, LegendDefinitions]
        if isinstance(_legend, Unset):
            legend = UNSET
        else:
            legend = LegendDefinitions.from_dict(_legend)

        _legend_set = d.pop("legendSet", UNSET)
        legend_set: Union[Unset, MapViewLegendSet]
        if isinstance(_legend_set, Unset):
            legend_set = UNSET
        else:
            legend_set = MapViewLegendSet.from_dict(_legend_set)

        method = d.pop("method", UNSET)

        no_data_color = d.pop("noDataColor", UNSET)

        no_space_between_columns = d.pop("noSpaceBetweenColumns", UNSET)

        opacity = d.pop("opacity", UNSET)

        org_unit_field = d.pop("orgUnitField", UNSET)

        org_unit_field_display_name = d.pop("orgUnitFieldDisplayName", UNSET)

        organisation_unit_color = d.pop("organisationUnitColor", UNSET)

        _organisation_unit_group_set = d.pop("organisationUnitGroupSet", UNSET)
        organisation_unit_group_set: Union[Unset, MapViewOrganisationUnitGroupSet]
        if isinstance(_organisation_unit_group_set, Unset):
            organisation_unit_group_set = UNSET
        else:
            organisation_unit_group_set = MapViewOrganisationUnitGroupSet.from_dict(_organisation_unit_group_set)

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
            organisation_units_item = MapViewOrganisationUnitsItem.from_dict(organisation_units_item_data)

            organisation_units.append(organisation_units_item)

        parent_graph = d.pop("parentGraph", UNSET)

        _parent_graph_map = d.pop("parentGraphMap", UNSET)
        parent_graph_map: Union[Unset, MapViewParentGraphMap]
        if isinstance(_parent_graph_map, Unset):
            parent_graph_map = UNSET
        else:
            parent_graph_map = MapViewParentGraphMap.from_dict(_parent_graph_map)

        percent_stacked_values = d.pop("percentStackedValues", UNSET)

        periods = cast(list[str], d.pop("periods", UNSET))

        _program = d.pop("program", UNSET)
        program: Union[Unset, MapViewProgram]
        if isinstance(_program, Unset):
            program = UNSET
        else:
            program = MapViewProgram.from_dict(_program)

        program_indicator_dimensions = []
        _program_indicator_dimensions = d.pop("programIndicatorDimensions", UNSET)
        for program_indicator_dimensions_item_data in _program_indicator_dimensions or []:
            program_indicator_dimensions_item = TrackedEntityProgramIndicatorDimension.from_dict(
                program_indicator_dimensions_item_data
            )

            program_indicator_dimensions.append(program_indicator_dimensions_item)

        _program_stage = d.pop("programStage", UNSET)
        program_stage: Union[Unset, MapViewProgramStage]
        if isinstance(_program_stage, Unset):
            program_stage = UNSET
        else:
            program_stage = MapViewProgramStage.from_dict(_program_stage)

        radius_high = d.pop("radiusHigh", UNSET)

        radius_low = d.pop("radiusLow", UNSET)

        _relative_periods = d.pop("relativePeriods", UNSET)
        relative_periods: Union[Unset, RelativePeriods]
        if isinstance(_relative_periods, Unset):
            relative_periods = UNSET
        else:
            relative_periods = RelativePeriods.from_dict(_relative_periods)

        row_sub_totals = d.pop("rowSubTotals", UNSET)

        row_totals = d.pop("rowTotals", UNSET)

        rows = []
        _rows = d.pop("rows", UNSET)
        for rows_item_data in _rows or []:
            rows_item = MapViewRowsItem.from_dict(rows_item_data)

            rows.append(rows_item)

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

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _style_data_item = d.pop("styleDataItem", UNSET)
        style_data_item: Union[Unset, MapViewStyleDataItem]
        if isinstance(_style_data_item, Unset):
            style_data_item = UNSET
        else:
            style_data_item = MapViewStyleDataItem.from_dict(_style_data_item)

        subscribed = d.pop("subscribed", UNSET)

        subscribers = cast(list[str], d.pop("subscribers", UNSET))

        subtitle = d.pop("subtitle", UNSET)

        time_field = d.pop("timeField", UNSET)

        title = d.pop("title", UNSET)

        _tracked_entity_type = d.pop("trackedEntityType", UNSET)
        tracked_entity_type: Union[Unset, MapViewTrackedEntityType]
        if isinstance(_tracked_entity_type, Unset):
            tracked_entity_type = UNSET
        else:
            tracked_entity_type = MapViewTrackedEntityType.from_dict(_tracked_entity_type)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, MapViewUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = MapViewUser.from_dict(_user)

        user_organisation_unit = d.pop("userOrganisationUnit", UNSET)

        user_organisation_unit_children = d.pop("userOrganisationUnitChildren", UNSET)

        user_organisation_unit_grand_children = d.pop("userOrganisationUnitGrandChildren", UNSET)

        map_view = cls(
            aggregation_type=aggregation_type,
            digit_group_separator=digit_group_separator,
            event_point_radius=event_point_radius,
            event_status=event_status,
            hide_empty_row_items=hide_empty_row_items,
            organisation_unit_selection_mode=organisation_unit_selection_mode,
            parent_level=parent_level,
            program_status=program_status,
            regression_type=regression_type,
            rendering_strategy=rendering_strategy,
            sort_order=sort_order,
            thematic_map_type=thematic_map_type,
            top_limit=top_limit,
            user_org_unit_type=user_org_unit_type,
            access=access,
            area_radius=area_radius,
            attribute_dimensions=attribute_dimensions,
            attribute_values=attribute_values,
            category_dimensions=category_dimensions,
            category_option_group_set_dimensions=category_option_group_set_dimensions,
            classes=classes,
            code=code,
            col_sub_totals=col_sub_totals,
            col_totals=col_totals,
            color_high=color_high,
            color_low=color_low,
            color_scale=color_scale,
            column_dimensions=column_dimensions,
            columns=columns,
            completed_only=completed_only,
            config=config,
            created=created,
            created_by=created_by,
            cumulative_values=cumulative_values,
            data_dimension_items=data_dimension_items,
            data_element_dimensions=data_element_dimensions,
            data_element_group_set_dimensions=data_element_group_set_dimensions,
            description=description,
            display_base_line_label=display_base_line_label,
            display_description=display_description,
            display_form_name=display_form_name,
            display_name=display_name,
            display_short_name=display_short_name,
            display_subtitle=display_subtitle,
            display_target_line_label=display_target_line_label,
            display_title=display_title,
            end_date=end_date,
            event_clustering=event_clustering,
            event_coordinate_field=event_coordinate_field,
            event_point_color=event_point_color,
            favorite=favorite,
            favorites=favorites,
            filter_dimensions=filter_dimensions,
            filters=filters,
            follow_up=follow_up,
            form_name=form_name,
            hidden=hidden,
            hide_empty_rows=hide_empty_rows,
            hide_legend=hide_legend,
            hide_subtitle=hide_subtitle,
            hide_title=hide_title,
            href=href,
            id=id,
            interpretations=interpretations,
            item_organisation_unit_groups=item_organisation_unit_groups,
            label_font_color=label_font_color,
            label_font_size=label_font_size,
            label_font_style=label_font_style,
            label_font_weight=label_font_weight,
            label_template=label_template,
            labels=labels,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            layer=layer,
            legend=legend,
            legend_set=legend_set,
            method=method,
            no_data_color=no_data_color,
            no_space_between_columns=no_space_between_columns,
            opacity=opacity,
            org_unit_field=org_unit_field,
            org_unit_field_display_name=org_unit_field_display_name,
            organisation_unit_color=organisation_unit_color,
            organisation_unit_group_set=organisation_unit_group_set,
            organisation_unit_group_set_dimensions=organisation_unit_group_set_dimensions,
            organisation_unit_levels=organisation_unit_levels,
            organisation_units=organisation_units,
            parent_graph=parent_graph,
            parent_graph_map=parent_graph_map,
            percent_stacked_values=percent_stacked_values,
            periods=periods,
            program=program,
            program_indicator_dimensions=program_indicator_dimensions,
            program_stage=program_stage,
            radius_high=radius_high,
            radius_low=radius_low,
            relative_periods=relative_periods,
            row_sub_totals=row_sub_totals,
            row_totals=row_totals,
            rows=rows,
            sharing=sharing,
            short_name=short_name,
            show_data=show_data,
            show_dimension_labels=show_dimension_labels,
            show_hierarchy=show_hierarchy,
            skip_rounding=skip_rounding,
            start_date=start_date,
            style_data_item=style_data_item,
            subscribed=subscribed,
            subscribers=subscribers,
            subtitle=subtitle,
            time_field=time_field,
            title=title,
            tracked_entity_type=tracked_entity_type,
            translations=translations,
            user=user,
            user_organisation_unit=user_organisation_unit,
            user_organisation_unit_children=user_organisation_unit_children,
            user_organisation_unit_grand_children=user_organisation_unit_grand_children,
        )

        map_view.additional_properties = d
        return map_view

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
