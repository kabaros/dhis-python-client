import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.scheduler_entry_job_status import SchedulerEntryJobStatus
from ..models.scheduler_entry_job_type import SchedulerEntryJobType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SchedulerEntryJob")


@_attrs_define
class SchedulerEntryJob:
    """
    Attributes:
        status (SchedulerEntryJobStatus):
        type_ (SchedulerEntryJobType):
        cron_expression (Union[Unset, str]):
        delay (Union[Unset, int]):
        id (Union[Unset, str]): A UID for an JobConfiguration object
            (Java name `org.hisp.dhis.scheduling.JobConfiguration`) Example: sg2YT1aq02c.
        name (Union[Unset, str]):
        next_execution_time (Union[Unset, datetime.datetime]):
    """

    status: SchedulerEntryJobStatus
    type_: SchedulerEntryJobType
    cron_expression: Union[Unset, str] = UNSET
    delay: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    next_execution_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        type_ = self.type_.value

        cron_expression = self.cron_expression

        delay = self.delay

        id = self.id

        name = self.name

        next_execution_time: Union[Unset, str] = UNSET
        if not isinstance(self.next_execution_time, Unset):
            next_execution_time = self.next_execution_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "type": type_,
            }
        )
        if cron_expression is not UNSET:
            field_dict["cronExpression"] = cron_expression
        if delay is not UNSET:
            field_dict["delay"] = delay
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if next_execution_time is not UNSET:
            field_dict["nextExecutionTime"] = next_execution_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        status = SchedulerEntryJobStatus(d.pop("status"))

        type_ = SchedulerEntryJobType(d.pop("type"))

        cron_expression = d.pop("cronExpression", UNSET)

        delay = d.pop("delay", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _next_execution_time = d.pop("nextExecutionTime", UNSET)
        next_execution_time: Union[Unset, datetime.datetime]
        if isinstance(_next_execution_time, Unset):
            next_execution_time = UNSET
        else:
            next_execution_time = isoparse(_next_execution_time)

        scheduler_entry_job = cls(
            status=status,
            type_=type_,
            cron_expression=cron_expression,
            delay=delay,
            id=id,
            name=name,
            next_execution_time=next_execution_time,
        )

        scheduler_entry_job.additional_properties = d
        return scheduler_entry_job

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
