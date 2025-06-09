import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.dashboard_item_shape import DashboardItemShape
from ..models.dashboard_item_type import DashboardItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.dashboard_item_created_by import DashboardItemCreatedBy
    from ..models.dashboard_item_event_chart import DashboardItemEventChart
    from ..models.dashboard_item_event_report import DashboardItemEventReport
    from ..models.dashboard_item_event_visualization import DashboardItemEventVisualization
    from ..models.dashboard_item_last_updated_by import DashboardItemLastUpdatedBy
    from ..models.dashboard_item_map import DashboardItemMap
    from ..models.dashboard_item_reports_item import DashboardItemReportsItem
    from ..models.dashboard_item_resources_item import DashboardItemResourcesItem
    from ..models.dashboard_item_user import DashboardItemUser
    from ..models.dashboard_item_users_item import DashboardItemUsersItem
    from ..models.dashboard_item_visualization import DashboardItemVisualization
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="DashboardItem")


@_attrs_define
class DashboardItem:
    """
    Attributes:
        content_count (int):
        interpretation_count (int):
        interpretation_like_count (int):
        shape (DashboardItemShape):
        type_ (DashboardItemType):
        access (Union[Unset, Access]):
        app_key (Union[Unset, str]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, DashboardItemCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        display_name (Union[Unset, str]):
        event_chart (Union[Unset, DashboardItemEventChart]): A UID reference to a EventChart
            (Java name `org.hisp.dhis.eventchart.EventChart`)
        event_report (Union[Unset, DashboardItemEventReport]): A UID reference to a EventReport
            (Java name `org.hisp.dhis.eventreport.EventReport`)
        event_visualization (Union[Unset, DashboardItemEventVisualization]): A UID reference to a EventVisualization
            (Java name `org.hisp.dhis.eventvisualization.EventVisualization`)
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        height (Union[Unset, int]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, DashboardItemLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        map_ (Union[Unset, DashboardItemMap]): A UID reference to a Map
            (Java name `org.hisp.dhis.mapping.Map`)
        messages (Union[Unset, bool]):
        name (Union[Unset, str]):
        reports (Union[Unset, list['DashboardItemReportsItem']]):
        resources (Union[Unset, list['DashboardItemResourcesItem']]):
        sharing (Union[Unset, Sharing]):
        text (Union[Unset, str]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, DashboardItemUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        users (Union[Unset, list['DashboardItemUsersItem']]):
        visualization (Union[Unset, DashboardItemVisualization]): A UID reference to a Visualization
            (Java name `org.hisp.dhis.visualization.Visualization`)
        width (Union[Unset, int]):
        x (Union[Unset, int]):
        y (Union[Unset, int]):
    """

    content_count: int
    interpretation_count: int
    interpretation_like_count: int
    shape: DashboardItemShape
    type_: DashboardItemType
    access: Union[Unset, "Access"] = UNSET
    app_key: Union[Unset, str] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "DashboardItemCreatedBy"] = UNSET
    display_name: Union[Unset, str] = UNSET
    event_chart: Union[Unset, "DashboardItemEventChart"] = UNSET
    event_report: Union[Unset, "DashboardItemEventReport"] = UNSET
    event_visualization: Union[Unset, "DashboardItemEventVisualization"] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    height: Union[Unset, int] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "DashboardItemLastUpdatedBy"] = UNSET
    map_: Union[Unset, "DashboardItemMap"] = UNSET
    messages: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    reports: Union[Unset, list["DashboardItemReportsItem"]] = UNSET
    resources: Union[Unset, list["DashboardItemResourcesItem"]] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    text: Union[Unset, str] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "DashboardItemUser"] = UNSET
    users: Union[Unset, list["DashboardItemUsersItem"]] = UNSET
    visualization: Union[Unset, "DashboardItemVisualization"] = UNSET
    width: Union[Unset, int] = UNSET
    x: Union[Unset, int] = UNSET
    y: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_count = self.content_count

        interpretation_count = self.interpretation_count

        interpretation_like_count = self.interpretation_like_count

        shape = self.shape.value

        type_ = self.type_.value

        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        app_key = self.app_key

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

        display_name = self.display_name

        event_chart: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event_chart, Unset):
            event_chart = self.event_chart.to_dict()

        event_report: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event_report, Unset):
            event_report = self.event_report.to_dict()

        event_visualization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event_visualization, Unset):
            event_visualization = self.event_visualization.to_dict()

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        height = self.height

        href = self.href

        id = self.id

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        map_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.map_, Unset):
            map_ = self.map_.to_dict()

        messages = self.messages

        name = self.name

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

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        text = self.text

        translations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        users: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        visualization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.visualization, Unset):
            visualization = self.visualization.to_dict()

        width = self.width

        x = self.x

        y = self.y

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contentCount": content_count,
                "interpretationCount": interpretation_count,
                "interpretationLikeCount": interpretation_like_count,
                "shape": shape,
                "type": type_,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if app_key is not UNSET:
            field_dict["appKey"] = app_key
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if code is not UNSET:
            field_dict["code"] = code
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if event_chart is not UNSET:
            field_dict["eventChart"] = event_chart
        if event_report is not UNSET:
            field_dict["eventReport"] = event_report
        if event_visualization is not UNSET:
            field_dict["eventVisualization"] = event_visualization
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if height is not UNSET:
            field_dict["height"] = height
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if map_ is not UNSET:
            field_dict["map"] = map_
        if messages is not UNSET:
            field_dict["messages"] = messages
        if name is not UNSET:
            field_dict["name"] = name
        if reports is not UNSET:
            field_dict["reports"] = reports
        if resources is not UNSET:
            field_dict["resources"] = resources
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if text is not UNSET:
            field_dict["text"] = text
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user
        if users is not UNSET:
            field_dict["users"] = users
        if visualization is not UNSET:
            field_dict["visualization"] = visualization
        if width is not UNSET:
            field_dict["width"] = width
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.dashboard_item_created_by import DashboardItemCreatedBy
        from ..models.dashboard_item_event_chart import DashboardItemEventChart
        from ..models.dashboard_item_event_report import DashboardItemEventReport
        from ..models.dashboard_item_event_visualization import DashboardItemEventVisualization
        from ..models.dashboard_item_last_updated_by import DashboardItemLastUpdatedBy
        from ..models.dashboard_item_map import DashboardItemMap
        from ..models.dashboard_item_reports_item import DashboardItemReportsItem
        from ..models.dashboard_item_resources_item import DashboardItemResourcesItem
        from ..models.dashboard_item_user import DashboardItemUser
        from ..models.dashboard_item_users_item import DashboardItemUsersItem
        from ..models.dashboard_item_visualization import DashboardItemVisualization
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        content_count = d.pop("contentCount")

        interpretation_count = d.pop("interpretationCount")

        interpretation_like_count = d.pop("interpretationLikeCount")

        shape = DashboardItemShape(d.pop("shape"))

        type_ = DashboardItemType(d.pop("type"))

        _access = d.pop("access", UNSET)
        access: Union[Unset, Access]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

        app_key = d.pop("appKey", UNSET)

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
        created_by: Union[Unset, DashboardItemCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = DashboardItemCreatedBy.from_dict(_created_by)

        display_name = d.pop("displayName", UNSET)

        _event_chart = d.pop("eventChart", UNSET)
        event_chart: Union[Unset, DashboardItemEventChart]
        if isinstance(_event_chart, Unset):
            event_chart = UNSET
        else:
            event_chart = DashboardItemEventChart.from_dict(_event_chart)

        _event_report = d.pop("eventReport", UNSET)
        event_report: Union[Unset, DashboardItemEventReport]
        if isinstance(_event_report, Unset):
            event_report = UNSET
        else:
            event_report = DashboardItemEventReport.from_dict(_event_report)

        _event_visualization = d.pop("eventVisualization", UNSET)
        event_visualization: Union[Unset, DashboardItemEventVisualization]
        if isinstance(_event_visualization, Unset):
            event_visualization = UNSET
        else:
            event_visualization = DashboardItemEventVisualization.from_dict(_event_visualization)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        height = d.pop("height", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, DashboardItemLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = DashboardItemLastUpdatedBy.from_dict(_last_updated_by)

        _map_ = d.pop("map", UNSET)
        map_: Union[Unset, DashboardItemMap]
        if isinstance(_map_, Unset):
            map_ = UNSET
        else:
            map_ = DashboardItemMap.from_dict(_map_)

        messages = d.pop("messages", UNSET)

        name = d.pop("name", UNSET)

        reports = []
        _reports = d.pop("reports", UNSET)
        for reports_item_data in _reports or []:
            reports_item = DashboardItemReportsItem.from_dict(reports_item_data)

            reports.append(reports_item)

        resources = []
        _resources = d.pop("resources", UNSET)
        for resources_item_data in _resources or []:
            resources_item = DashboardItemResourcesItem.from_dict(resources_item_data)

            resources.append(resources_item)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        text = d.pop("text", UNSET)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, DashboardItemUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = DashboardItemUser.from_dict(_user)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = DashboardItemUsersItem.from_dict(users_item_data)

            users.append(users_item)

        _visualization = d.pop("visualization", UNSET)
        visualization: Union[Unset, DashboardItemVisualization]
        if isinstance(_visualization, Unset):
            visualization = UNSET
        else:
            visualization = DashboardItemVisualization.from_dict(_visualization)

        width = d.pop("width", UNSET)

        x = d.pop("x", UNSET)

        y = d.pop("y", UNSET)

        dashboard_item = cls(
            content_count=content_count,
            interpretation_count=interpretation_count,
            interpretation_like_count=interpretation_like_count,
            shape=shape,
            type_=type_,
            access=access,
            app_key=app_key,
            attribute_values=attribute_values,
            code=code,
            created=created,
            created_by=created_by,
            display_name=display_name,
            event_chart=event_chart,
            event_report=event_report,
            event_visualization=event_visualization,
            favorite=favorite,
            favorites=favorites,
            height=height,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            map_=map_,
            messages=messages,
            name=name,
            reports=reports,
            resources=resources,
            sharing=sharing,
            text=text,
            translations=translations,
            user=user,
            users=users,
            visualization=visualization,
            width=width,
            x=x,
            y=y,
        )

        dashboard_item.additional_properties = d
        return dashboard_item

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
