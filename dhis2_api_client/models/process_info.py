import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.process_info_status import ProcessInfoStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessInfo")


@_attrs_define
class ProcessInfo:
    """
    Attributes:
        status (ProcessInfoStatus):
        cancelled_time (Union[Unset, datetime.datetime]):
        completed_time (Union[Unset, datetime.datetime]):
        description (Union[Unset, str]):
        error (Union[Unset, str]):
        job_id (Union[Unset, str]):
        stages (Union[Unset, list[str]]):
        started_time (Union[Unset, datetime.datetime]):
        summary (Union[Unset, str]):
    """

    status: ProcessInfoStatus
    cancelled_time: Union[Unset, datetime.datetime] = UNSET
    completed_time: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    error: Union[Unset, str] = UNSET
    job_id: Union[Unset, str] = UNSET
    stages: Union[Unset, list[str]] = UNSET
    started_time: Union[Unset, datetime.datetime] = UNSET
    summary: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        cancelled_time: Union[Unset, str] = UNSET
        if not isinstance(self.cancelled_time, Unset):
            cancelled_time = self.cancelled_time.isoformat()

        completed_time: Union[Unset, str] = UNSET
        if not isinstance(self.completed_time, Unset):
            completed_time = self.completed_time.isoformat()

        description = self.description

        error = self.error

        job_id = self.job_id

        stages: Union[Unset, list[str]] = UNSET
        if not isinstance(self.stages, Unset):
            stages = self.stages

        started_time: Union[Unset, str] = UNSET
        if not isinstance(self.started_time, Unset):
            started_time = self.started_time.isoformat()

        summary = self.summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if cancelled_time is not UNSET:
            field_dict["cancelledTime"] = cancelled_time
        if completed_time is not UNSET:
            field_dict["completedTime"] = completed_time
        if description is not UNSET:
            field_dict["description"] = description
        if error is not UNSET:
            field_dict["error"] = error
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if stages is not UNSET:
            field_dict["stages"] = stages
        if started_time is not UNSET:
            field_dict["startedTime"] = started_time
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        status = ProcessInfoStatus(d.pop("status"))

        _cancelled_time = d.pop("cancelledTime", UNSET)
        cancelled_time: Union[Unset, datetime.datetime]
        if isinstance(_cancelled_time, Unset):
            cancelled_time = UNSET
        else:
            cancelled_time = isoparse(_cancelled_time)

        _completed_time = d.pop("completedTime", UNSET)
        completed_time: Union[Unset, datetime.datetime]
        if isinstance(_completed_time, Unset):
            completed_time = UNSET
        else:
            completed_time = isoparse(_completed_time)

        description = d.pop("description", UNSET)

        error = d.pop("error", UNSET)

        job_id = d.pop("jobId", UNSET)

        stages = cast(list[str], d.pop("stages", UNSET))

        _started_time = d.pop("startedTime", UNSET)
        started_time: Union[Unset, datetime.datetime]
        if isinstance(_started_time, Unset):
            started_time = UNSET
        else:
            started_time = isoparse(_started_time)

        summary = d.pop("summary", UNSET)

        process_info = cls(
            status=status,
            cancelled_time=cancelled_time,
            completed_time=completed_time,
            description=description,
            error=error,
            job_id=job_id,
            stages=stages,
            started_time=started_time,
            summary=summary,
        )

        process_info.additional_properties = d
        return process_info

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
