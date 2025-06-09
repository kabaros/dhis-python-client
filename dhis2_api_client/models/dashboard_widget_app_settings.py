from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardWidgetAppSettings")


@_attrs_define
class DashboardWidgetAppSettings:
    """
    Attributes:
        hide_title (Union[Unset, bool]):
    """

    hide_title: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hide_title = self.hide_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hide_title is not UNSET:
            field_dict["hideTitle"] = hide_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        hide_title = d.pop("hideTitle", UNSET)

        dashboard_widget_app_settings = cls(
            hide_title=hide_title,
        )

        dashboard_widget_app_settings.additional_properties = d
        return dashboard_widget_app_settings

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
