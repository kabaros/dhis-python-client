import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_integrity_issue import DataIntegrityIssue


T = TypeVar("T", bound="DataIntegrityDetails")


@_attrs_define
class DataIntegrityDetails:
    """
    Attributes:
        error (Union[Unset, str]):
        finished_time (Union[Unset, datetime.datetime]):
        issues (Union[Unset, list['DataIntegrityIssue']]):
        start_time (Union[Unset, datetime.datetime]):
    """

    error: Union[Unset, str] = UNSET
    finished_time: Union[Unset, datetime.datetime] = UNSET
    issues: Union[Unset, list["DataIntegrityIssue"]] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        finished_time: Union[Unset, str] = UNSET
        if not isinstance(self.finished_time, Unset):
            finished_time = self.finished_time.isoformat()

        issues: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.issues, Unset):
            issues = []
            for issues_item_data in self.issues:
                issues_item = issues_item_data.to_dict()
                issues.append(issues_item)

        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if finished_time is not UNSET:
            field_dict["finishedTime"] = finished_time
        if issues is not UNSET:
            field_dict["issues"] = issues
        if start_time is not UNSET:
            field_dict["startTime"] = start_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.data_integrity_issue import DataIntegrityIssue

        d = src_dict.copy()
        error = d.pop("error", UNSET)

        _finished_time = d.pop("finishedTime", UNSET)
        finished_time: Union[Unset, datetime.datetime]
        if isinstance(_finished_time, Unset):
            finished_time = UNSET
        else:
            finished_time = isoparse(_finished_time)

        issues = []
        _issues = d.pop("issues", UNSET)
        for issues_item_data in _issues or []:
            issues_item = DataIntegrityIssue.from_dict(issues_item_data)

            issues.append(issues_item)

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        data_integrity_details = cls(
            error=error,
            finished_time=finished_time,
            issues=issues,
            start_time=start_time,
        )

        data_integrity_details.additional_properties = d
        return data_integrity_details

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
