from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tracker_import_error import TrackerImportError
    from ..models.warning import Warning_


T = TypeVar("T", bound="ValidationReport")


@_attrs_define
class ValidationReport:
    """
    Attributes:
        error_reports (Union[Unset, list['TrackerImportError']]):
        warning_reports (Union[Unset, list['Warning_']]):
    """

    error_reports: Union[Unset, list["TrackerImportError"]] = UNSET
    warning_reports: Union[Unset, list["Warning_"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_reports: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.error_reports, Unset):
            error_reports = []
            for error_reports_item_data in self.error_reports:
                error_reports_item = error_reports_item_data.to_dict()
                error_reports.append(error_reports_item)

        warning_reports: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.warning_reports, Unset):
            warning_reports = []
            for warning_reports_item_data in self.warning_reports:
                warning_reports_item = warning_reports_item_data.to_dict()
                warning_reports.append(warning_reports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_reports is not UNSET:
            field_dict["errorReports"] = error_reports
        if warning_reports is not UNSET:
            field_dict["warningReports"] = warning_reports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tracker_import_error import TrackerImportError
        from ..models.warning import Warning_

        d = src_dict.copy()
        error_reports = []
        _error_reports = d.pop("errorReports", UNSET)
        for error_reports_item_data in _error_reports or []:
            error_reports_item = TrackerImportError.from_dict(error_reports_item_data)

            error_reports.append(error_reports_item)

        warning_reports = []
        _warning_reports = d.pop("warningReports", UNSET)
        for warning_reports_item_data in _warning_reports or []:
            warning_reports_item = Warning_.from_dict(warning_reports_item_data)

            warning_reports.append(warning_reports_item)

        validation_report = cls(
            error_reports=error_reports,
            warning_reports=warning_reports,
        )

        validation_report.additional_properties = d
        return validation_report

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
