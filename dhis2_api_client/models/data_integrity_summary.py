import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataIntegritySummary")


@_attrs_define
class DataIntegritySummary:
    """
    Attributes:
        count (int):
        error (Union[Unset, str]):
        finished_time (Union[Unset, datetime.datetime]):
        percentage (Union[Unset, float]):
        start_time (Union[Unset, datetime.datetime]):
    """

    count: int
    error: Union[Unset, str] = UNSET
    finished_time: Union[Unset, datetime.datetime] = UNSET
    percentage: Union[Unset, float] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        error = self.error

        finished_time: Union[Unset, str] = UNSET
        if not isinstance(self.finished_time, Unset):
            finished_time = self.finished_time.isoformat()

        percentage = self.percentage

        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if finished_time is not UNSET:
            field_dict["finishedTime"] = finished_time
        if percentage is not UNSET:
            field_dict["percentage"] = percentage
        if start_time is not UNSET:
            field_dict["startTime"] = start_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        count = d.pop("count")

        error = d.pop("error", UNSET)

        _finished_time = d.pop("finishedTime", UNSET)
        finished_time: Union[Unset, datetime.datetime]
        if isinstance(_finished_time, Unset):
            finished_time = UNSET
        else:
            finished_time = isoparse(_finished_time)

        percentage = d.pop("percentage", UNSET)

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        data_integrity_summary = cls(
            count=count,
            error=error,
            finished_time=finished_time,
            percentage=percentage,
            start_time=start_time,
        )

        data_integrity_summary.additional_properties = d
        return data_integrity_summary

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
