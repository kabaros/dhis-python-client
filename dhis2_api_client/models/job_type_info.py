from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.job_type_info_job_type import JobTypeInfoJobType
from ..models.job_type_info_scheduling_type import JobTypeInfoSchedulingType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.property_ import Property


T = TypeVar("T", bound="JobTypeInfo")


@_attrs_define
class JobTypeInfo:
    """
    Attributes:
        job_type (JobTypeInfoJobType):
        scheduling_type (JobTypeInfoSchedulingType):
        job_parameters (Union[Unset, list['Property']]):
        name (Union[Unset, str]):
    """

    job_type: JobTypeInfoJobType
    scheduling_type: JobTypeInfoSchedulingType
    job_parameters: Union[Unset, list["Property"]] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_type = self.job_type.value

        scheduling_type = self.scheduling_type.value

        job_parameters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.job_parameters, Unset):
            job_parameters = []
            for job_parameters_item_data in self.job_parameters:
                job_parameters_item = job_parameters_item_data.to_dict()
                job_parameters.append(job_parameters_item)

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jobType": job_type,
                "schedulingType": scheduling_type,
            }
        )
        if job_parameters is not UNSET:
            field_dict["jobParameters"] = job_parameters
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.property_ import Property

        d = src_dict.copy()
        job_type = JobTypeInfoJobType(d.pop("jobType"))

        scheduling_type = JobTypeInfoSchedulingType(d.pop("schedulingType"))

        job_parameters = []
        _job_parameters = d.pop("jobParameters", UNSET)
        for job_parameters_item_data in _job_parameters or []:
            job_parameters_item = Property.from_dict(job_parameters_item_data)

            job_parameters.append(job_parameters_item)

        name = d.pop("name", UNSET)

        job_type_info = cls(
            job_type=job_type,
            scheduling_type=scheduling_type,
            job_parameters=job_parameters,
            name=name,
        )

        job_type_info.additional_properties = d
        return job_type_info

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
