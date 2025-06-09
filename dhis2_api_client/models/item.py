import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.item_on_failure import ItemOnFailure
from ..models.item_status import ItemStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Item")


@_attrs_define
class Item:
    """
    Attributes:
        duration (int):
        on_failure (ItemOnFailure):
        status (ItemStatus):
        complete (Union[Unset, bool]):
        completed_time (Union[Unset, datetime.datetime]):
        description (Union[Unset, str]):
        error (Union[Unset, str]):
        summary (Union[Unset, str]):
    """

    duration: int
    on_failure: ItemOnFailure
    status: ItemStatus
    complete: Union[Unset, bool] = UNSET
    completed_time: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    error: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration = self.duration

        on_failure = self.on_failure.value

        status = self.status.value

        complete = self.complete

        completed_time: Union[Unset, str] = UNSET
        if not isinstance(self.completed_time, Unset):
            completed_time = self.completed_time.isoformat()

        description = self.description

        error = self.error

        summary = self.summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duration": duration,
                "onFailure": on_failure,
                "status": status,
            }
        )
        if complete is not UNSET:
            field_dict["complete"] = complete
        if completed_time is not UNSET:
            field_dict["completedTime"] = completed_time
        if description is not UNSET:
            field_dict["description"] = description
        if error is not UNSET:
            field_dict["error"] = error
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duration = d.pop("duration")

        on_failure = ItemOnFailure(d.pop("onFailure"))

        status = ItemStatus(d.pop("status"))

        complete = d.pop("complete", UNSET)

        _completed_time = d.pop("completedTime", UNSET)
        completed_time: Union[Unset, datetime.datetime]
        if isinstance(_completed_time, Unset):
            completed_time = UNSET
        else:
            completed_time = isoparse(_completed_time)

        description = d.pop("description", UNSET)

        error = d.pop("error", UNSET)

        summary = d.pop("summary", UNSET)

        item = cls(
            duration=duration,
            on_failure=on_failure,
            status=status,
            complete=complete,
            completed_time=completed_time,
            description=description,
            error=error,
            summary=summary,
        )

        item.additional_properties = d
        return item

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
