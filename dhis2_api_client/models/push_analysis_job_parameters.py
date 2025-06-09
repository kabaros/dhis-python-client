from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PushAnalysisJobParameters")


@_attrs_define
class PushAnalysisJobParameters:
    """
    Attributes:
        push_analysis (list[str]):
    """

    push_analysis: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        push_analysis = self.push_analysis

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pushAnalysis": push_analysis,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        push_analysis = cast(list[str], d.pop("pushAnalysis"))

        push_analysis_job_parameters = cls(
            push_analysis=push_analysis,
        )

        push_analysis_job_parameters.additional_properties = d
        return push_analysis_job_parameters

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
