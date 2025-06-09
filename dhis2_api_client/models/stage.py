import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.stage_on_failure import StageOnFailure
from ..models.stage_status import StageStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item import Item


T = TypeVar("T", bound="Stage")


@_attrs_define
class Stage:
    """
    Attributes:
        duration (int):
        on_failure (StageOnFailure):
        status (StageStatus):
        total_items (int):
        complete (Union[Unset, bool]):
        completed_time (Union[Unset, datetime.datetime]):
        description (Union[Unset, str]):
        error (Union[Unset, str]):
        items (Union[Unset, list['Item']]):
        summary (Union[Unset, str]):
    """

    duration: int
    on_failure: StageOnFailure
    status: StageStatus
    total_items: int
    complete: Union[Unset, bool] = UNSET
    completed_time: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    error: Union[Unset, str] = UNSET
    items: Union[Unset, list["Item"]] = UNSET
    summary: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration = self.duration

        on_failure = self.on_failure.value

        status = self.status.value

        total_items = self.total_items

        complete = self.complete

        completed_time: Union[Unset, str] = UNSET
        if not isinstance(self.completed_time, Unset):
            completed_time = self.completed_time.isoformat()

        description = self.description

        error = self.error

        items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        summary = self.summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duration": duration,
                "onFailure": on_failure,
                "status": status,
                "totalItems": total_items,
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
        if items is not UNSET:
            field_dict["items"] = items
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.item import Item

        d = src_dict.copy()
        duration = d.pop("duration")

        on_failure = StageOnFailure(d.pop("onFailure"))

        status = StageStatus(d.pop("status"))

        total_items = d.pop("totalItems")

        complete = d.pop("complete", UNSET)

        _completed_time = d.pop("completedTime", UNSET)
        completed_time: Union[Unset, datetime.datetime]
        if isinstance(_completed_time, Unset):
            completed_time = UNSET
        else:
            completed_time = isoparse(_completed_time)

        description = d.pop("description", UNSET)

        error = d.pop("error", UNSET)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = Item.from_dict(items_item_data)

            items.append(items_item)

        summary = d.pop("summary", UNSET)

        stage = cls(
            duration=duration,
            on_failure=on_failure,
            status=status,
            total_items=total_items,
            complete=complete,
            completed_time=completed_time,
            description=description,
            error=error,
            items=items,
            summary=summary,
        )

        stage.additional_properties = d
        return stage

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
