from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SchedulerQueue")


@_attrs_define
class SchedulerQueue:
    """
    Attributes:
        cron_expression (str):
        sequence (list[str]):
        name (Union[Unset, str]):
    """

    cron_expression: str
    sequence: list[str]
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cron_expression = self.cron_expression

        sequence = self.sequence

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cronExpression": cron_expression,
                "sequence": sequence,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        cron_expression = d.pop("cronExpression")

        sequence = cast(list[str], d.pop("sequence"))

        name = d.pop("name", UNSET)

        scheduler_queue = cls(
            cron_expression=cron_expression,
            sequence=sequence,
            name=name,
        )

        scheduler_queue.additional_properties = d
        return scheduler_queue

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
