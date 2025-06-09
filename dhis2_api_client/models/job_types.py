from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_type_info import JobTypeInfo


T = TypeVar("T", bound="JobTypes")


@_attrs_define
class JobTypes:
    """
    Attributes:
        job_types (Union[Unset, list['JobTypeInfo']]):
    """

    job_types: Union[Unset, list["JobTypeInfo"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_types: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.job_types, Unset):
            job_types = []
            for job_types_item_data in self.job_types:
                job_types_item = job_types_item_data.to_dict()
                job_types.append(job_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_types is not UNSET:
            field_dict["jobTypes"] = job_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.job_type_info import JobTypeInfo

        d = src_dict.copy()
        job_types = []
        _job_types = d.pop("jobTypes", UNSET)
        for job_types_item_data in _job_types or []:
            job_types_item = JobTypeInfo.from_dict(job_types_item_data)

            job_types.append(job_types_item)

        job_types = cls(
            job_types=job_types,
        )

        job_types.additional_properties = d
        return job_types

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
