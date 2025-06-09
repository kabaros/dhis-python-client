from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.data_integrity_job_parameters_type import DataIntegrityJobParametersType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataIntegrityJobParameters")


@_attrs_define
class DataIntegrityJobParameters:
    """
    Attributes:
        type_ (DataIntegrityJobParametersType):
        checks (Union[Unset, list[str]]):
    """

    type_: DataIntegrityJobParametersType
    checks: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        checks: Union[Unset, list[str]] = UNSET
        if not isinstance(self.checks, Unset):
            checks = self.checks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if checks is not UNSET:
            field_dict["checks"] = checks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        type_ = DataIntegrityJobParametersType(d.pop("type"))

        checks = cast(list[str], d.pop("checks", UNSET))

        data_integrity_job_parameters = cls(
            type_=type_,
            checks=checks,
        )

        data_integrity_job_parameters.additional_properties = d
        return data_integrity_job_parameters

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
