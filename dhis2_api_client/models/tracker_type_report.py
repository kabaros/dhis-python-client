from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tracker_type_report_tracker_type import TrackerTypeReportTrackerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity import Entity
    from ..models.tracker_stats import TrackerStats


T = TypeVar("T", bound="TrackerTypeReport")


@_attrs_define
class TrackerTypeReport:
    """
    Attributes:
        tracker_type (TrackerTypeReportTrackerType):
        object_reports (Union[Unset, list['Entity']]):
        stats (Union[Unset, TrackerStats]):
    """

    tracker_type: TrackerTypeReportTrackerType
    object_reports: Union[Unset, list["Entity"]] = UNSET
    stats: Union[Unset, "TrackerStats"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tracker_type = self.tracker_type.value

        object_reports: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.object_reports, Unset):
            object_reports = []
            for object_reports_item_data in self.object_reports:
                object_reports_item = object_reports_item_data.to_dict()
                object_reports.append(object_reports_item)

        stats: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trackerType": tracker_type,
            }
        )
        if object_reports is not UNSET:
            field_dict["objectReports"] = object_reports
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.entity import Entity
        from ..models.tracker_stats import TrackerStats

        d = src_dict.copy()
        tracker_type = TrackerTypeReportTrackerType(d.pop("trackerType"))

        object_reports = []
        _object_reports = d.pop("objectReports", UNSET)
        for object_reports_item_data in _object_reports or []:
            object_reports_item = Entity.from_dict(object_reports_item_data)

            object_reports.append(object_reports_item)

        _stats = d.pop("stats", UNSET)
        stats: Union[Unset, TrackerStats]
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = TrackerStats.from_dict(_stats)

        tracker_type_report = cls(
            tracker_type=tracker_type,
            object_reports=object_reports,
            stats=stats,
        )

        tracker_type_report.additional_properties = d
        return tracker_type_report

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
