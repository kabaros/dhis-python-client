from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.order_criteria_direction import OrderCriteriaDirection
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderCriteria")


@_attrs_define
class OrderCriteria:
    """
    Attributes:
        direction (OrderCriteriaDirection):
        field (Union[Unset, str]):
    """

    direction: OrderCriteriaDirection
    field: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        direction = self.direction.value

        field = self.field

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "direction": direction,
            }
        )
        if field is not UNSET:
            field_dict["field"] = field

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        direction = OrderCriteriaDirection(d.pop("direction"))

        field = d.pop("field", UNSET)

        order_criteria = cls(
            direction=direction,
            field=field,
        )

        order_criteria.additional_properties = d
        return order_criteria

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
