from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_settings_analysis_display_property import UserSettingsAnalysisDisplayProperty
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserSettings")


@_attrs_define
class UserSettings:
    """
    Attributes:
        analysis_display_property (UserSettingsAnalysisDisplayProperty):
        db_locale (Union[Unset, str]):
        message_email_notification (Union[Unset, bool]):
        message_sms_notification (Union[Unset, bool]):
        style (Union[Unset, str]):
        tracker_dashboard_layout (Union[Unset, str]):
        ui_locale (Union[Unset, str]):
    """

    analysis_display_property: UserSettingsAnalysisDisplayProperty
    db_locale: Union[Unset, str] = UNSET
    message_email_notification: Union[Unset, bool] = UNSET
    message_sms_notification: Union[Unset, bool] = UNSET
    style: Union[Unset, str] = UNSET
    tracker_dashboard_layout: Union[Unset, str] = UNSET
    ui_locale: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        analysis_display_property = self.analysis_display_property.value

        db_locale = self.db_locale

        message_email_notification = self.message_email_notification

        message_sms_notification = self.message_sms_notification

        style = self.style

        tracker_dashboard_layout = self.tracker_dashboard_layout

        ui_locale = self.ui_locale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "analysisDisplayProperty": analysis_display_property,
            }
        )
        if db_locale is not UNSET:
            field_dict["dbLocale"] = db_locale
        if message_email_notification is not UNSET:
            field_dict["messageEmailNotification"] = message_email_notification
        if message_sms_notification is not UNSET:
            field_dict["messageSmsNotification"] = message_sms_notification
        if style is not UNSET:
            field_dict["style"] = style
        if tracker_dashboard_layout is not UNSET:
            field_dict["trackerDashboardLayout"] = tracker_dashboard_layout
        if ui_locale is not UNSET:
            field_dict["uiLocale"] = ui_locale

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        analysis_display_property = UserSettingsAnalysisDisplayProperty(d.pop("analysisDisplayProperty"))

        db_locale = d.pop("dbLocale", UNSET)

        message_email_notification = d.pop("messageEmailNotification", UNSET)

        message_sms_notification = d.pop("messageSmsNotification", UNSET)

        style = d.pop("style", UNSET)

        tracker_dashboard_layout = d.pop("trackerDashboardLayout", UNSET)

        ui_locale = d.pop("uiLocale", UNSET)

        user_settings = cls(
            analysis_display_property=analysis_display_property,
            db_locale=db_locale,
            message_email_notification=message_email_notification,
            message_sms_notification=message_sms_notification,
            style=style,
            tracker_dashboard_layout=tracker_dashboard_layout,
            ui_locale=ui_locale,
        )

        user_settings.additional_properties = d
        return user_settings

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
