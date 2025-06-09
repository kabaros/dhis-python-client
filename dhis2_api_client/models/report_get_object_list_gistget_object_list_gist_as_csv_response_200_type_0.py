from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gist_pager import GistPager
    from ..models.report_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_reports_item import (
        ReportGetObjectListGistgetObjectListGistAsCsvResponse200Type0ReportsItem,
    )


T = TypeVar("T", bound="ReportGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class ReportGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        reports (Union[Unset, list['ReportGetObjectListGistgetObjectListGistAsCsvResponse200Type0ReportsItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    reports: Union[Unset, list["ReportGetObjectListGistgetObjectListGistAsCsvResponse200Type0ReportsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        reports: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.reports, Unset):
            reports = []
            for reports_item_data in self.reports:
                reports_item = reports_item_data.to_dict()
                reports.append(reports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if reports is not UNSET:
            field_dict["reports"] = reports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.gist_pager import GistPager
        from ..models.report_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_reports_item import (
            ReportGetObjectListGistgetObjectListGistAsCsvResponse200Type0ReportsItem,
        )

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        reports = []
        _reports = d.pop("reports", UNSET)
        for reports_item_data in _reports or []:
            reports_item = ReportGetObjectListGistgetObjectListGistAsCsvResponse200Type0ReportsItem.from_dict(
                reports_item_data
            )

            reports.append(reports_item)

        report_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            reports=reports,
        )

        report_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return report_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
