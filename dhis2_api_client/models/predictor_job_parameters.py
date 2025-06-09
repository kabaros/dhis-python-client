from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PredictorJobParameters")


@_attrs_define
class PredictorJobParameters:
    """
    Attributes:
        relative_end (int):
        relative_start (int):
        predictor_groups (Union[Unset, list[str]]):
        predictors (Union[Unset, list[str]]):
    """

    relative_end: int
    relative_start: int
    predictor_groups: Union[Unset, list[str]] = UNSET
    predictors: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        relative_end = self.relative_end

        relative_start = self.relative_start

        predictor_groups: Union[Unset, list[str]] = UNSET
        if not isinstance(self.predictor_groups, Unset):
            predictor_groups = self.predictor_groups

        predictors: Union[Unset, list[str]] = UNSET
        if not isinstance(self.predictors, Unset):
            predictors = self.predictors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "relativeEnd": relative_end,
                "relativeStart": relative_start,
            }
        )
        if predictor_groups is not UNSET:
            field_dict["predictorGroups"] = predictor_groups
        if predictors is not UNSET:
            field_dict["predictors"] = predictors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        relative_end = d.pop("relativeEnd")

        relative_start = d.pop("relativeStart")

        predictor_groups = cast(list[str], d.pop("predictorGroups", UNSET))

        predictors = cast(list[str], d.pop("predictors", UNSET))

        predictor_job_parameters = cls(
            relative_end=relative_end,
            relative_start=relative_start,
            predictor_groups=predictor_groups,
            predictors=predictors,
        )

        predictor_job_parameters.additional_properties = d
        return predictor_job_parameters

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
