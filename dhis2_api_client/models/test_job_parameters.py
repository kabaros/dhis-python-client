from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.test_job_parameters_fail_with_policy import TestJobParametersFailWithPolicy
from ..types import UNSET, Unset

T = TypeVar("T", bound="TestJobParameters")


@_attrs_define
class TestJobParameters:
    """
    Attributes:
        fail_with_policy (TestJobParametersFailWithPolicy):
        fail_at_item (Union[Unset, int]):
        fail_at_stage (Union[Unset, int]):
        fail_with_exception (Union[Unset, bool]):
        fail_with_message (Union[Unset, str]):
        item_duration (Union[Unset, int]):
        items (Union[Unset, int]):
        run_stages_parallel (Union[Unset, bool]):
        stages (Union[Unset, int]):
        wait_millis (Union[Unset, int]):
    """

    fail_with_policy: TestJobParametersFailWithPolicy
    fail_at_item: Union[Unset, int] = UNSET
    fail_at_stage: Union[Unset, int] = UNSET
    fail_with_exception: Union[Unset, bool] = UNSET
    fail_with_message: Union[Unset, str] = UNSET
    item_duration: Union[Unset, int] = UNSET
    items: Union[Unset, int] = UNSET
    run_stages_parallel: Union[Unset, bool] = UNSET
    stages: Union[Unset, int] = UNSET
    wait_millis: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fail_with_policy = self.fail_with_policy.value

        fail_at_item = self.fail_at_item

        fail_at_stage = self.fail_at_stage

        fail_with_exception = self.fail_with_exception

        fail_with_message = self.fail_with_message

        item_duration = self.item_duration

        items = self.items

        run_stages_parallel = self.run_stages_parallel

        stages = self.stages

        wait_millis = self.wait_millis

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "failWithPolicy": fail_with_policy,
            }
        )
        if fail_at_item is not UNSET:
            field_dict["failAtItem"] = fail_at_item
        if fail_at_stage is not UNSET:
            field_dict["failAtStage"] = fail_at_stage
        if fail_with_exception is not UNSET:
            field_dict["failWithException"] = fail_with_exception
        if fail_with_message is not UNSET:
            field_dict["failWithMessage"] = fail_with_message
        if item_duration is not UNSET:
            field_dict["itemDuration"] = item_duration
        if items is not UNSET:
            field_dict["items"] = items
        if run_stages_parallel is not UNSET:
            field_dict["runStagesParallel"] = run_stages_parallel
        if stages is not UNSET:
            field_dict["stages"] = stages
        if wait_millis is not UNSET:
            field_dict["waitMillis"] = wait_millis

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        fail_with_policy = TestJobParametersFailWithPolicy(d.pop("failWithPolicy"))

        fail_at_item = d.pop("failAtItem", UNSET)

        fail_at_stage = d.pop("failAtStage", UNSET)

        fail_with_exception = d.pop("failWithException", UNSET)

        fail_with_message = d.pop("failWithMessage", UNSET)

        item_duration = d.pop("itemDuration", UNSET)

        items = d.pop("items", UNSET)

        run_stages_parallel = d.pop("runStagesParallel", UNSET)

        stages = d.pop("stages", UNSET)

        wait_millis = d.pop("waitMillis", UNSET)

        test_job_parameters = cls(
            fail_with_policy=fail_with_policy,
            fail_at_item=fail_at_item,
            fail_at_stage=fail_at_stage,
            fail_with_exception=fail_with_exception,
            fail_with_message=fail_with_message,
            item_duration=item_duration,
            items=items,
            run_stages_parallel=run_stages_parallel,
            stages=stages,
            wait_millis=wait_millis,
        )

        test_job_parameters.additional_properties = d
        return test_job_parameters

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
