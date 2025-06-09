from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DisableInactiveUsersJobParameters")


@_attrs_define
class DisableInactiveUsersJobParameters:
    """
    Attributes:
        inactive_months (int):
        reminder_days_before (Union[Unset, int]):
    """

    inactive_months: int
    reminder_days_before: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inactive_months = self.inactive_months

        reminder_days_before = self.reminder_days_before

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inactiveMonths": inactive_months,
            }
        )
        if reminder_days_before is not UNSET:
            field_dict["reminderDaysBefore"] = reminder_days_before

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        inactive_months = d.pop("inactiveMonths")

        reminder_days_before = d.pop("reminderDaysBefore", UNSET)

        disable_inactive_users_job_parameters = cls(
            inactive_months=inactive_months,
            reminder_days_before=reminder_days_before,
        )

        disable_inactive_users_job_parameters.additional_properties = d
        return disable_inactive_users_job_parameters

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
