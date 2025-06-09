from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_plan_plan import ExecutionPlanPlan


T = TypeVar("T", bound="ExecutionPlan")


@_attrs_define
class ExecutionPlan:
    """
    Attributes:
        execution_time (Union[Unset, float]):
        plan (Union[Unset, ExecutionPlanPlan]):
        planning_time (Union[Unset, float]):
        query (Union[Unset, str]):
        time_in_millis (Union[Unset, float]):
    """

    execution_time: Union[Unset, float] = UNSET
    plan: Union[Unset, "ExecutionPlanPlan"] = UNSET
    planning_time: Union[Unset, float] = UNSET
    query: Union[Unset, str] = UNSET
    time_in_millis: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_time = self.execution_time

        plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.plan, Unset):
            plan = self.plan.to_dict()

        planning_time = self.planning_time

        query = self.query

        time_in_millis = self.time_in_millis

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if execution_time is not UNSET:
            field_dict["executionTime"] = execution_time
        if plan is not UNSET:
            field_dict["plan"] = plan
        if planning_time is not UNSET:
            field_dict["planningTime"] = planning_time
        if query is not UNSET:
            field_dict["query"] = query
        if time_in_millis is not UNSET:
            field_dict["timeInMillis"] = time_in_millis

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.execution_plan_plan import ExecutionPlanPlan

        d = src_dict.copy()
        execution_time = d.pop("executionTime", UNSET)

        _plan = d.pop("plan", UNSET)
        plan: Union[Unset, ExecutionPlanPlan]
        if isinstance(_plan, Unset):
            plan = UNSET
        else:
            plan = ExecutionPlanPlan.from_dict(_plan)

        planning_time = d.pop("planningTime", UNSET)

        query = d.pop("query", UNSET)

        time_in_millis = d.pop("timeInMillis", UNSET)

        execution_plan = cls(
            execution_time=execution_time,
            plan=plan,
            planning_time=planning_time,
            query=query,
            time_in_millis=time_in_millis,
        )

        execution_plan.additional_properties = d
        return execution_plan

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
