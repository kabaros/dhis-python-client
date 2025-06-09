import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.scheduler_entry_status import SchedulerEntryStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scheduler_entry_job import SchedulerEntryJob


T = TypeVar("T", bound="SchedulerEntry")


@_attrs_define
class SchedulerEntry:
    """
    Attributes:
        status (SchedulerEntryStatus):
        configurable (Union[Unset, bool]):
        cron_expression (Union[Unset, str]):
        delay (Union[Unset, int]):
        enabled (Union[Unset, bool]):
        max_delayed_execution_time (Union[Unset, datetime.datetime]):
        name (Union[Unset, str]):
        next_execution_time (Union[Unset, datetime.datetime]):
        seconds_to_max_delayed_execution_time (Union[Unset, int]):
        seconds_to_next_execution_time (Union[Unset, int]):
        sequence (Union[Unset, list['SchedulerEntryJob']]):
        type_ (Union[Unset, str]):
    """

    status: SchedulerEntryStatus
    configurable: Union[Unset, bool] = UNSET
    cron_expression: Union[Unset, str] = UNSET
    delay: Union[Unset, int] = UNSET
    enabled: Union[Unset, bool] = UNSET
    max_delayed_execution_time: Union[Unset, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    next_execution_time: Union[Unset, datetime.datetime] = UNSET
    seconds_to_max_delayed_execution_time: Union[Unset, int] = UNSET
    seconds_to_next_execution_time: Union[Unset, int] = UNSET
    sequence: Union[Unset, list["SchedulerEntryJob"]] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        configurable = self.configurable

        cron_expression = self.cron_expression

        delay = self.delay

        enabled = self.enabled

        max_delayed_execution_time: Union[Unset, str] = UNSET
        if not isinstance(self.max_delayed_execution_time, Unset):
            max_delayed_execution_time = self.max_delayed_execution_time.isoformat()

        name = self.name

        next_execution_time: Union[Unset, str] = UNSET
        if not isinstance(self.next_execution_time, Unset):
            next_execution_time = self.next_execution_time.isoformat()

        seconds_to_max_delayed_execution_time = self.seconds_to_max_delayed_execution_time

        seconds_to_next_execution_time = self.seconds_to_next_execution_time

        sequence: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sequence, Unset):
            sequence = []
            for sequence_item_data in self.sequence:
                sequence_item = sequence_item_data.to_dict()
                sequence.append(sequence_item)

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if configurable is not UNSET:
            field_dict["configurable"] = configurable
        if cron_expression is not UNSET:
            field_dict["cronExpression"] = cron_expression
        if delay is not UNSET:
            field_dict["delay"] = delay
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if max_delayed_execution_time is not UNSET:
            field_dict["maxDelayedExecutionTime"] = max_delayed_execution_time
        if name is not UNSET:
            field_dict["name"] = name
        if next_execution_time is not UNSET:
            field_dict["nextExecutionTime"] = next_execution_time
        if seconds_to_max_delayed_execution_time is not UNSET:
            field_dict["secondsToMaxDelayedExecutionTime"] = seconds_to_max_delayed_execution_time
        if seconds_to_next_execution_time is not UNSET:
            field_dict["secondsToNextExecutionTime"] = seconds_to_next_execution_time
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.scheduler_entry_job import SchedulerEntryJob

        d = src_dict.copy()
        status = SchedulerEntryStatus(d.pop("status"))

        configurable = d.pop("configurable", UNSET)

        cron_expression = d.pop("cronExpression", UNSET)

        delay = d.pop("delay", UNSET)

        enabled = d.pop("enabled", UNSET)

        _max_delayed_execution_time = d.pop("maxDelayedExecutionTime", UNSET)
        max_delayed_execution_time: Union[Unset, datetime.datetime]
        if isinstance(_max_delayed_execution_time, Unset):
            max_delayed_execution_time = UNSET
        else:
            max_delayed_execution_time = isoparse(_max_delayed_execution_time)

        name = d.pop("name", UNSET)

        _next_execution_time = d.pop("nextExecutionTime", UNSET)
        next_execution_time: Union[Unset, datetime.datetime]
        if isinstance(_next_execution_time, Unset):
            next_execution_time = UNSET
        else:
            next_execution_time = isoparse(_next_execution_time)

        seconds_to_max_delayed_execution_time = d.pop("secondsToMaxDelayedExecutionTime", UNSET)

        seconds_to_next_execution_time = d.pop("secondsToNextExecutionTime", UNSET)

        sequence = []
        _sequence = d.pop("sequence", UNSET)
        for sequence_item_data in _sequence or []:
            sequence_item = SchedulerEntryJob.from_dict(sequence_item_data)

            sequence.append(sequence_item)

        type_ = d.pop("type", UNSET)

        scheduler_entry = cls(
            status=status,
            configurable=configurable,
            cron_expression=cron_expression,
            delay=delay,
            enabled=enabled,
            max_delayed_execution_time=max_delayed_execution_time,
            name=name,
            next_execution_time=next_execution_time,
            seconds_to_max_delayed_execution_time=seconds_to_max_delayed_execution_time,
            seconds_to_next_execution_time=seconds_to_next_execution_time,
            sequence=sequence,
            type_=type_,
        )

        scheduler_entry.additional_properties = d
        return scheduler_entry

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
