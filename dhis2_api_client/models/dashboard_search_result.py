from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app import App
    from ..models.dashboard_search_result_event_charts_item import DashboardSearchResultEventChartsItem
    from ..models.dashboard_search_result_event_reports_item import DashboardSearchResultEventReportsItem
    from ..models.dashboard_search_result_event_visualizations_item import DashboardSearchResultEventVisualizationsItem
    from ..models.dashboard_search_result_maps_item import DashboardSearchResultMapsItem
    from ..models.dashboard_search_result_reports_item import DashboardSearchResultReportsItem
    from ..models.dashboard_search_result_resources_item import DashboardSearchResultResourcesItem
    from ..models.dashboard_search_result_users_item import DashboardSearchResultUsersItem
    from ..models.dashboard_search_result_visualizations_item import DashboardSearchResultVisualizationsItem


T = TypeVar("T", bound="DashboardSearchResult")


@_attrs_define
class DashboardSearchResult:
    """
    Attributes:
        app_count (int):
        event_chart_count (int):
        event_report_count (int):
        event_visualization_count (int):
        map_count (int):
        report_count (int):
        resource_count (int):
        search_count (int):
        user_count (int):
        visualization_count (int):
        apps (Union[Unset, list['App']]):
        event_charts (Union[Unset, list['DashboardSearchResultEventChartsItem']]):
        event_reports (Union[Unset, list['DashboardSearchResultEventReportsItem']]):
        event_visualizations (Union[Unset, list['DashboardSearchResultEventVisualizationsItem']]):
        maps (Union[Unset, list['DashboardSearchResultMapsItem']]):
        reports (Union[Unset, list['DashboardSearchResultReportsItem']]):
        resources (Union[Unset, list['DashboardSearchResultResourcesItem']]):
        users (Union[Unset, list['DashboardSearchResultUsersItem']]):
        visualizations (Union[Unset, list['DashboardSearchResultVisualizationsItem']]):
    """

    app_count: int
    event_chart_count: int
    event_report_count: int
    event_visualization_count: int
    map_count: int
    report_count: int
    resource_count: int
    search_count: int
    user_count: int
    visualization_count: int
    apps: Union[Unset, list["App"]] = UNSET
    event_charts: Union[Unset, list["DashboardSearchResultEventChartsItem"]] = UNSET
    event_reports: Union[Unset, list["DashboardSearchResultEventReportsItem"]] = UNSET
    event_visualizations: Union[Unset, list["DashboardSearchResultEventVisualizationsItem"]] = UNSET
    maps: Union[Unset, list["DashboardSearchResultMapsItem"]] = UNSET
    reports: Union[Unset, list["DashboardSearchResultReportsItem"]] = UNSET
    resources: Union[Unset, list["DashboardSearchResultResourcesItem"]] = UNSET
    users: Union[Unset, list["DashboardSearchResultUsersItem"]] = UNSET
    visualizations: Union[Unset, list["DashboardSearchResultVisualizationsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_count = self.app_count

        event_chart_count = self.event_chart_count

        event_report_count = self.event_report_count

        event_visualization_count = self.event_visualization_count

        map_count = self.map_count

        report_count = self.report_count

        resource_count = self.resource_count

        search_count = self.search_count

        user_count = self.user_count

        visualization_count = self.visualization_count

        apps: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.apps, Unset):
            apps = []
            for apps_item_data in self.apps:
                apps_item = apps_item_data.to_dict()
                apps.append(apps_item)

        event_charts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.event_charts, Unset):
            event_charts = []
            for event_charts_item_data in self.event_charts:
                event_charts_item = event_charts_item_data.to_dict()
                event_charts.append(event_charts_item)

        event_reports: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.event_reports, Unset):
            event_reports = []
            for event_reports_item_data in self.event_reports:
                event_reports_item = event_reports_item_data.to_dict()
                event_reports.append(event_reports_item)

        event_visualizations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.event_visualizations, Unset):
            event_visualizations = []
            for event_visualizations_item_data in self.event_visualizations:
                event_visualizations_item = event_visualizations_item_data.to_dict()
                event_visualizations.append(event_visualizations_item)

        maps: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.maps, Unset):
            maps = []
            for maps_item_data in self.maps:
                maps_item = maps_item_data.to_dict()
                maps.append(maps_item)

        reports: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.reports, Unset):
            reports = []
            for reports_item_data in self.reports:
                reports_item = reports_item_data.to_dict()
                reports.append(reports_item)

        resources: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.resources, Unset):
            resources = []
            for resources_item_data in self.resources:
                resources_item = resources_item_data.to_dict()
                resources.append(resources_item)

        users: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        visualizations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.visualizations, Unset):
            visualizations = []
            for visualizations_item_data in self.visualizations:
                visualizations_item = visualizations_item_data.to_dict()
                visualizations.append(visualizations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "appCount": app_count,
                "eventChartCount": event_chart_count,
                "eventReportCount": event_report_count,
                "eventVisualizationCount": event_visualization_count,
                "mapCount": map_count,
                "reportCount": report_count,
                "resourceCount": resource_count,
                "searchCount": search_count,
                "userCount": user_count,
                "visualizationCount": visualization_count,
            }
        )
        if apps is not UNSET:
            field_dict["apps"] = apps
        if event_charts is not UNSET:
            field_dict["eventCharts"] = event_charts
        if event_reports is not UNSET:
            field_dict["eventReports"] = event_reports
        if event_visualizations is not UNSET:
            field_dict["eventVisualizations"] = event_visualizations
        if maps is not UNSET:
            field_dict["maps"] = maps
        if reports is not UNSET:
            field_dict["reports"] = reports
        if resources is not UNSET:
            field_dict["resources"] = resources
        if users is not UNSET:
            field_dict["users"] = users
        if visualizations is not UNSET:
            field_dict["visualizations"] = visualizations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.app import App
        from ..models.dashboard_search_result_event_charts_item import DashboardSearchResultEventChartsItem
        from ..models.dashboard_search_result_event_reports_item import DashboardSearchResultEventReportsItem
        from ..models.dashboard_search_result_event_visualizations_item import (
            DashboardSearchResultEventVisualizationsItem,
        )
        from ..models.dashboard_search_result_maps_item import DashboardSearchResultMapsItem
        from ..models.dashboard_search_result_reports_item import DashboardSearchResultReportsItem
        from ..models.dashboard_search_result_resources_item import DashboardSearchResultResourcesItem
        from ..models.dashboard_search_result_users_item import DashboardSearchResultUsersItem
        from ..models.dashboard_search_result_visualizations_item import DashboardSearchResultVisualizationsItem

        d = src_dict.copy()
        app_count = d.pop("appCount")

        event_chart_count = d.pop("eventChartCount")

        event_report_count = d.pop("eventReportCount")

        event_visualization_count = d.pop("eventVisualizationCount")

        map_count = d.pop("mapCount")

        report_count = d.pop("reportCount")

        resource_count = d.pop("resourceCount")

        search_count = d.pop("searchCount")

        user_count = d.pop("userCount")

        visualization_count = d.pop("visualizationCount")

        apps = []
        _apps = d.pop("apps", UNSET)
        for apps_item_data in _apps or []:
            apps_item = App.from_dict(apps_item_data)

            apps.append(apps_item)

        event_charts = []
        _event_charts = d.pop("eventCharts", UNSET)
        for event_charts_item_data in _event_charts or []:
            event_charts_item = DashboardSearchResultEventChartsItem.from_dict(event_charts_item_data)

            event_charts.append(event_charts_item)

        event_reports = []
        _event_reports = d.pop("eventReports", UNSET)
        for event_reports_item_data in _event_reports or []:
            event_reports_item = DashboardSearchResultEventReportsItem.from_dict(event_reports_item_data)

            event_reports.append(event_reports_item)

        event_visualizations = []
        _event_visualizations = d.pop("eventVisualizations", UNSET)
        for event_visualizations_item_data in _event_visualizations or []:
            event_visualizations_item = DashboardSearchResultEventVisualizationsItem.from_dict(
                event_visualizations_item_data
            )

            event_visualizations.append(event_visualizations_item)

        maps = []
        _maps = d.pop("maps", UNSET)
        for maps_item_data in _maps or []:
            maps_item = DashboardSearchResultMapsItem.from_dict(maps_item_data)

            maps.append(maps_item)

        reports = []
        _reports = d.pop("reports", UNSET)
        for reports_item_data in _reports or []:
            reports_item = DashboardSearchResultReportsItem.from_dict(reports_item_data)

            reports.append(reports_item)

        resources = []
        _resources = d.pop("resources", UNSET)
        for resources_item_data in _resources or []:
            resources_item = DashboardSearchResultResourcesItem.from_dict(resources_item_data)

            resources.append(resources_item)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = DashboardSearchResultUsersItem.from_dict(users_item_data)

            users.append(users_item)

        visualizations = []
        _visualizations = d.pop("visualizations", UNSET)
        for visualizations_item_data in _visualizations or []:
            visualizations_item = DashboardSearchResultVisualizationsItem.from_dict(visualizations_item_data)

            visualizations.append(visualizations_item)

        dashboard_search_result = cls(
            app_count=app_count,
            event_chart_count=event_chart_count,
            event_report_count=event_report_count,
            event_visualization_count=event_visualization_count,
            map_count=map_count,
            report_count=report_count,
            resource_count=resource_count,
            search_count=search_count,
            user_count=user_count,
            visualization_count=visualization_count,
            apps=apps,
            event_charts=event_charts,
            event_reports=event_reports,
            event_visualizations=event_visualizations,
            maps=maps,
            reports=reports,
            resources=resources,
            users=users,
            visualizations=visualizations,
        )

        dashboard_search_result.additional_properties = d
        return dashboard_search_result

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
