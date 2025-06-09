from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_report import ErrorReport


T = TypeVar("T", bound="ObjectReport")


@_attrs_define
class ObjectReport:
    """
    Attributes:
        error_reports (list['ErrorReport']):
        display_name (Union[Unset, str]):
        index (Union[Unset, int]):
        klass (Union[Unset, str]):
        uid (Union[Unset, str]):
    """

    error_reports: list["ErrorReport"]
    display_name: Union[Unset, str] = UNSET
    index: Union[Unset, int] = UNSET
    klass: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_reports = []
        for error_reports_item_data in self.error_reports:
            error_reports_item = error_reports_item_data.to_dict()
            error_reports.append(error_reports_item)

        display_name = self.display_name

        index = self.index

        klass = self.klass

        uid = self.uid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "errorReports": error_reports,
            }
        )
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if index is not UNSET:
            field_dict["index"] = index
        if klass is not UNSET:
            field_dict["klass"] = klass
        if uid is not UNSET:
            field_dict["uid"] = uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.error_report import ErrorReport

        d = src_dict.copy()
        error_reports = []
        _error_reports = d.pop("errorReports")
        for error_reports_item_data in _error_reports:
            error_reports_item = ErrorReport.from_dict(error_reports_item_data)

            error_reports.append(error_reports_item)

        display_name = d.pop("displayName", UNSET)

        index = d.pop("index", UNSET)

        klass = d.pop("klass", UNSET)

        uid = d.pop("uid", UNSET)

        object_report = cls(
            error_reports=error_reports,
            display_name=display_name,
            index=index,
            klass=klass,
            uid=uid,
        )

        object_report.additional_properties = d
        return object_report

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
