from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_widget_app_settings import DashboardWidgetAppSettings


T = TypeVar("T", bound="AppSettings")


@_attrs_define
class AppSettings:
    """
    Attributes:
        dashboard_widget (Union[Unset, DashboardWidgetAppSettings]):
    """

    dashboard_widget: Union[Unset, "DashboardWidgetAppSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dashboard_widget: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dashboard_widget, Unset):
            dashboard_widget = self.dashboard_widget.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dashboard_widget is not UNSET:
            field_dict["dashboardWidget"] = dashboard_widget

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.dashboard_widget_app_settings import DashboardWidgetAppSettings

        d = src_dict.copy()
        _dashboard_widget = d.pop("dashboardWidget", UNSET)
        dashboard_widget: Union[Unset, DashboardWidgetAppSettings]
        if isinstance(_dashboard_widget, Unset):
            dashboard_widget = UNSET
        else:
            dashboard_widget = DashboardWidgetAppSettings.from_dict(_dashboard_widget)

        app_settings = cls(
            dashboard_widget=dashboard_widget,
        )

        app_settings.additional_properties = d
        return app_settings

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
