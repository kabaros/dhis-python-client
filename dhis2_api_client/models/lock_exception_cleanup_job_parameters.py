from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LockExceptionCleanupJobParameters")


@_attrs_define
class LockExceptionCleanupJobParameters:
    """
    Attributes:
        expires_after_months (Union[Unset, int]):
    """

    expires_after_months: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_after_months = self.expires_after_months

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expires_after_months is not UNSET:
            field_dict["expiresAfterMonths"] = expires_after_months

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        expires_after_months = d.pop("expiresAfterMonths", UNSET)

        lock_exception_cleanup_job_parameters = cls(
            expires_after_months=expires_after_months,
        )

        lock_exception_cleanup_job_parameters.additional_properties = d
        return lock_exception_cleanup_job_parameters

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
