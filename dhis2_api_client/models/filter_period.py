from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FilterPeriod")


@_attrs_define
class FilterPeriod:
    """
    Attributes:
        period_from (int):
        period_to (int):
    """

    period_from: int
    period_to: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        period_from = self.period_from

        period_to = self.period_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "periodFrom": period_from,
                "periodTo": period_to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        period_from = d.pop("periodFrom")

        period_to = d.pop("periodTo")

        filter_period = cls(
            period_from=period_from,
            period_to=period_to,
        )

        filter_period.additional_properties = d
        return filter_period

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
