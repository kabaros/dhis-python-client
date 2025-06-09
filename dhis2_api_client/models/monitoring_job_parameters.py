from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitoringJobParameters")


@_attrs_define
class MonitoringJobParameters:
    """
    Attributes:
        relative_end (int):
        relative_start (int):
        persist_results (Union[Unset, bool]):
        send_notifications (Union[Unset, bool]):
        validation_rule_groups (Union[Unset, list[str]]):
    """

    relative_end: int
    relative_start: int
    persist_results: Union[Unset, bool] = UNSET
    send_notifications: Union[Unset, bool] = UNSET
    validation_rule_groups: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        relative_end = self.relative_end

        relative_start = self.relative_start

        persist_results = self.persist_results

        send_notifications = self.send_notifications

        validation_rule_groups: Union[Unset, list[str]] = UNSET
        if not isinstance(self.validation_rule_groups, Unset):
            validation_rule_groups = self.validation_rule_groups

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "relativeEnd": relative_end,
                "relativeStart": relative_start,
            }
        )
        if persist_results is not UNSET:
            field_dict["persistResults"] = persist_results
        if send_notifications is not UNSET:
            field_dict["sendNotifications"] = send_notifications
        if validation_rule_groups is not UNSET:
            field_dict["validationRuleGroups"] = validation_rule_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        relative_end = d.pop("relativeEnd")

        relative_start = d.pop("relativeStart")

        persist_results = d.pop("persistResults", UNSET)

        send_notifications = d.pop("sendNotifications", UNSET)

        validation_rule_groups = cast(list[str], d.pop("validationRuleGroups", UNSET))

        monitoring_job_parameters = cls(
            relative_end=relative_end,
            relative_start=relative_start,
            persist_results=persist_results,
            send_notifications=send_notifications,
            validation_rule_groups=validation_rule_groups,
        )

        monitoring_job_parameters.additional_properties = d
        return monitoring_job_parameters

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
