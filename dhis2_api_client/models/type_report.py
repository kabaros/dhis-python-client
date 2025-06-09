from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.object_report import ObjectReport
    from ..models.stats import Stats


T = TypeVar("T", bound="TypeReport")


@_attrs_define
class TypeReport:
    """
    Attributes:
        object_reports (list['ObjectReport']):
        klass (Union[Unset, str]):
        stats (Union[Unset, Stats]):
    """

    object_reports: list["ObjectReport"]
    klass: Union[Unset, str] = UNSET
    stats: Union[Unset, "Stats"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_reports = []
        for object_reports_item_data in self.object_reports:
            object_reports_item = object_reports_item_data.to_dict()
            object_reports.append(object_reports_item)

        klass = self.klass

        stats: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "objectReports": object_reports,
            }
        )
        if klass is not UNSET:
            field_dict["klass"] = klass
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.object_report import ObjectReport
        from ..models.stats import Stats

        d = src_dict.copy()
        object_reports = []
        _object_reports = d.pop("objectReports")
        for object_reports_item_data in _object_reports:
            object_reports_item = ObjectReport.from_dict(object_reports_item_data)

            object_reports.append(object_reports_item)

        klass = d.pop("klass", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: Union[Unset, Stats]
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = Stats.from_dict(_stats)

        type_report = cls(
            object_reports=object_reports,
            klass=klass,
            stats=stats,
        )

        type_report.additional_properties = d
        return type_report

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
