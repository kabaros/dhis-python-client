from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.html_push_analytics_job_parameters_mode import HtmlPushAnalyticsJobParametersMode

T = TypeVar("T", bound="HtmlPushAnalyticsJobParameters")


@_attrs_define
class HtmlPushAnalyticsJobParameters:
    """
    Attributes:
        dashboard (str): A UID for an Dashboard object
            (Java name `org.hisp.dhis.dashboard.Dashboard`) Example: fV5sz4Ys38O.
        mode (HtmlPushAnalyticsJobParametersMode):
        receivers (str): A UID for an UserGroup object
            (Java name `org.hisp.dhis.user.UserGroup`) Example: wd5C82cv3p6.
    """

    dashboard: str
    mode: HtmlPushAnalyticsJobParametersMode
    receivers: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dashboard = self.dashboard

        mode = self.mode.value

        receivers = self.receivers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dashboard": dashboard,
                "mode": mode,
                "receivers": receivers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        dashboard = d.pop("dashboard")

        mode = HtmlPushAnalyticsJobParametersMode(d.pop("mode"))

        receivers = d.pop("receivers")

        html_push_analytics_job_parameters = cls(
            dashboard=dashboard,
            mode=mode,
            receivers=receivers,
        )

        html_push_analytics_job_parameters.additional_properties = d
        return html_push_analytics_job_parameters

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
