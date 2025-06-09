from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cascade_sharing_report_update_objects import CascadeSharingReportUpdateObjects
    from ..models.error_report import ErrorReport


T = TypeVar("T", bound="CascadeSharingReport")


@_attrs_define
class CascadeSharingReport:
    """
    Attributes:
        count_updated_dashboard_items (int):
        error_reports (Union[Unset, list['ErrorReport']]):
        update_objects (Union[Unset, CascadeSharingReportUpdateObjects]):
    """

    count_updated_dashboard_items: int
    error_reports: Union[Unset, list["ErrorReport"]] = UNSET
    update_objects: Union[Unset, "CascadeSharingReportUpdateObjects"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count_updated_dashboard_items = self.count_updated_dashboard_items

        error_reports: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.error_reports, Unset):
            error_reports = []
            for error_reports_item_data in self.error_reports:
                error_reports_item = error_reports_item_data.to_dict()
                error_reports.append(error_reports_item)

        update_objects: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.update_objects, Unset):
            update_objects = self.update_objects.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "countUpdatedDashboardItems": count_updated_dashboard_items,
            }
        )
        if error_reports is not UNSET:
            field_dict["errorReports"] = error_reports
        if update_objects is not UNSET:
            field_dict["updateObjects"] = update_objects

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.cascade_sharing_report_update_objects import CascadeSharingReportUpdateObjects
        from ..models.error_report import ErrorReport

        d = src_dict.copy()
        count_updated_dashboard_items = d.pop("countUpdatedDashboardItems")

        error_reports = []
        _error_reports = d.pop("errorReports", UNSET)
        for error_reports_item_data in _error_reports or []:
            error_reports_item = ErrorReport.from_dict(error_reports_item_data)

            error_reports.append(error_reports_item)

        _update_objects = d.pop("updateObjects", UNSET)
        update_objects: Union[Unset, CascadeSharingReportUpdateObjects]
        if isinstance(_update_objects, Unset):
            update_objects = UNSET
        else:
            update_objects = CascadeSharingReportUpdateObjects.from_dict(_update_objects)

        cascade_sharing_report = cls(
            count_updated_dashboard_items=count_updated_dashboard_items,
            error_reports=error_reports,
            update_objects=update_objects,
        )

        cascade_sharing_report.additional_properties = d
        return cascade_sharing_report

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
