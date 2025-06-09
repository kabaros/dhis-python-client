from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.import_report_status import ImportReportStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata_import_params import MetadataImportParams
    from ..models.stats import Stats
    from ..models.type_report import TypeReport


T = TypeVar("T", bound="ImportReport")


@_attrs_define
class ImportReport:
    """
    Attributes:
        status (ImportReportStatus):
        type_reports (list['TypeReport']):
        import_params (Union[Unset, MetadataImportParams]):
        stats (Union[Unset, Stats]):
    """

    status: ImportReportStatus
    type_reports: list["TypeReport"]
    import_params: Union[Unset, "MetadataImportParams"] = UNSET
    stats: Union[Unset, "Stats"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        type_reports = []
        for type_reports_item_data in self.type_reports:
            type_reports_item = type_reports_item_data.to_dict()
            type_reports.append(type_reports_item)

        import_params: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.import_params, Unset):
            import_params = self.import_params.to_dict()

        stats: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "typeReports": type_reports,
            }
        )
        if import_params is not UNSET:
            field_dict["importParams"] = import_params
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.metadata_import_params import MetadataImportParams
        from ..models.stats import Stats
        from ..models.type_report import TypeReport

        d = src_dict.copy()
        status = ImportReportStatus(d.pop("status"))

        type_reports = []
        _type_reports = d.pop("typeReports")
        for type_reports_item_data in _type_reports:
            type_reports_item = TypeReport.from_dict(type_reports_item_data)

            type_reports.append(type_reports_item)

        _import_params = d.pop("importParams", UNSET)
        import_params: Union[Unset, MetadataImportParams]
        if isinstance(_import_params, Unset):
            import_params = UNSET
        else:
            import_params = MetadataImportParams.from_dict(_import_params)

        _stats = d.pop("stats", UNSET)
        stats: Union[Unset, Stats]
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = Stats.from_dict(_stats)

        import_report = cls(
            status=status,
            type_reports=type_reports,
            import_params=import_params,
            stats=stats,
        )

        import_report.additional_properties = d
        return import_report

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
