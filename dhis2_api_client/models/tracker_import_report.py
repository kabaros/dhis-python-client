from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tracker_import_report_status import TrackerImportReportStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.persistence_report import PersistenceReport
    from ..models.tracker_stats import TrackerStats
    from ..models.validation_report import ValidationReport


T = TypeVar("T", bound="TrackerImportReport")


@_attrs_define
class TrackerImportReport:
    """
    Attributes:
        status (TrackerImportReportStatus):
        bundle_report (Union[Unset, PersistenceReport]):
        message (Union[Unset, str]):
        stats (Union[Unset, TrackerStats]):
        validation_report (Union[Unset, ValidationReport]):
    """

    status: TrackerImportReportStatus
    bundle_report: Union[Unset, "PersistenceReport"] = UNSET
    message: Union[Unset, str] = UNSET
    stats: Union[Unset, "TrackerStats"] = UNSET
    validation_report: Union[Unset, "ValidationReport"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        bundle_report: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bundle_report, Unset):
            bundle_report = self.bundle_report.to_dict()

        message = self.message

        stats: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        validation_report: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.validation_report, Unset):
            validation_report = self.validation_report.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if bundle_report is not UNSET:
            field_dict["bundleReport"] = bundle_report
        if message is not UNSET:
            field_dict["message"] = message
        if stats is not UNSET:
            field_dict["stats"] = stats
        if validation_report is not UNSET:
            field_dict["validationReport"] = validation_report

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.persistence_report import PersistenceReport
        from ..models.tracker_stats import TrackerStats
        from ..models.validation_report import ValidationReport

        d = src_dict.copy()
        status = TrackerImportReportStatus(d.pop("status"))

        _bundle_report = d.pop("bundleReport", UNSET)
        bundle_report: Union[Unset, PersistenceReport]
        if isinstance(_bundle_report, Unset):
            bundle_report = UNSET
        else:
            bundle_report = PersistenceReport.from_dict(_bundle_report)

        message = d.pop("message", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: Union[Unset, TrackerStats]
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = TrackerStats.from_dict(_stats)

        _validation_report = d.pop("validationReport", UNSET)
        validation_report: Union[Unset, ValidationReport]
        if isinstance(_validation_report, Unset):
            validation_report = UNSET
        else:
            validation_report = ValidationReport.from_dict(_validation_report)

        tracker_import_report = cls(
            status=status,
            bundle_report=bundle_report,
            message=message,
            stats=stats,
            validation_report=validation_report,
        )

        tracker_import_report.additional_properties = d
        return tracker_import_report

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
