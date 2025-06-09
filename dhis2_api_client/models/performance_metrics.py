from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_plan import ExecutionPlan


T = TypeVar("T", bound="PerformanceMetrics")


@_attrs_define
class PerformanceMetrics:
    """
    Attributes:
        total_time_in_millis (float):
        execution_plans (Union[Unset, list['ExecutionPlan']]):
    """

    total_time_in_millis: float
    execution_plans: Union[Unset, list["ExecutionPlan"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_time_in_millis = self.total_time_in_millis

        execution_plans: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.execution_plans, Unset):
            execution_plans = []
            for execution_plans_item_data in self.execution_plans:
                execution_plans_item = execution_plans_item_data.to_dict()
                execution_plans.append(execution_plans_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalTimeInMillis": total_time_in_millis,
            }
        )
        if execution_plans is not UNSET:
            field_dict["executionPlans"] = execution_plans

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.execution_plan import ExecutionPlan

        d = src_dict.copy()
        total_time_in_millis = d.pop("totalTimeInMillis")

        execution_plans = []
        _execution_plans = d.pop("executionPlans", UNSET)
        for execution_plans_item_data in _execution_plans or []:
            execution_plans_item = ExecutionPlan.from_dict(execution_plans_item_data)

            execution_plans.append(execution_plans_item)

        performance_metrics = cls(
            total_time_in_millis=total_time_in_millis,
            execution_plans=execution_plans,
        )

        performance_metrics.additional_properties = d
        return performance_metrics

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
