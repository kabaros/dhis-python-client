import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.process_status import ProcessStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stage import Stage


T = TypeVar("T", bound="Process")


@_attrs_define
class Process:
    """
    Attributes:
        duration (int):
        status (ProcessStatus):
        cancelled_time (Union[Unset, datetime.datetime]):
        complete (Union[Unset, bool]):
        completed_time (Union[Unset, datetime.datetime]):
        description (Union[Unset, str]):
        error (Union[Unset, str]):
        job_id (Union[Unset, str]):
        stages (Union[Unset, list['Stage']]):
        summary (Union[Unset, str]):
        user_id (Union[Unset, str]):
    """

    duration: int
    status: ProcessStatus
    cancelled_time: Union[Unset, datetime.datetime] = UNSET
    complete: Union[Unset, bool] = UNSET
    completed_time: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    error: Union[Unset, str] = UNSET
    job_id: Union[Unset, str] = UNSET
    stages: Union[Unset, list["Stage"]] = UNSET
    summary: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration = self.duration

        status = self.status.value

        cancelled_time: Union[Unset, str] = UNSET
        if not isinstance(self.cancelled_time, Unset):
            cancelled_time = self.cancelled_time.isoformat()

        complete = self.complete

        completed_time: Union[Unset, str] = UNSET
        if not isinstance(self.completed_time, Unset):
            completed_time = self.completed_time.isoformat()

        description = self.description

        error = self.error

        job_id = self.job_id

        stages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.stages, Unset):
            stages = []
            for stages_item_data in self.stages:
                stages_item = stages_item_data.to_dict()
                stages.append(stages_item)

        summary = self.summary

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duration": duration,
                "status": status,
            }
        )
        if cancelled_time is not UNSET:
            field_dict["cancelledTime"] = cancelled_time
        if complete is not UNSET:
            field_dict["complete"] = complete
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
        if summary is not UNSET:
            field_dict["summary"] = summary
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.stage import Stage

        d = src_dict.copy()
        duration = d.pop("duration")

        status = ProcessStatus(d.pop("status"))

        _cancelled_time = d.pop("cancelledTime", UNSET)
        cancelled_time: Union[Unset, datetime.datetime]
        if isinstance(_cancelled_time, Unset):
            cancelled_time = UNSET
        else:
            cancelled_time = isoparse(_cancelled_time)

        complete = d.pop("complete", UNSET)

        _completed_time = d.pop("completedTime", UNSET)
        completed_time: Union[Unset, datetime.datetime]
        if isinstance(_completed_time, Unset):
            completed_time = UNSET
        else:
            completed_time = isoparse(_completed_time)

        description = d.pop("description", UNSET)

        error = d.pop("error", UNSET)

        job_id = d.pop("jobId", UNSET)

        stages = []
        _stages = d.pop("stages", UNSET)
        for stages_item_data in _stages or []:
            stages_item = Stage.from_dict(stages_item_data)

            stages.append(stages_item)

        summary = d.pop("summary", UNSET)

        user_id = d.pop("userId", UNSET)

        process = cls(
            duration=duration,
            status=status,
            cancelled_time=cancelled_time,
            complete=complete,
            completed_time=completed_time,
            description=description,
            error=error,
            job_id=job_id,
            stages=stages,
            summary=summary,
            user_id=user_id,
        )

        process.additional_properties = d
        return process

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
