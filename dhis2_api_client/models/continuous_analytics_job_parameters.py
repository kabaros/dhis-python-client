from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.continuous_analytics_job_parameters_skip_table_types_item import (
    ContinuousAnalyticsJobParametersSkipTableTypesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContinuousAnalyticsJobParameters")


@_attrs_define
class ContinuousAnalyticsJobParameters:
    """
    Attributes:
        full_update_hour_of_day (Union[Unset, int]):
        last_years (Union[Unset, int]):
        skip_outliers (Union[Unset, bool]):
        skip_table_types (Union[Unset, list[ContinuousAnalyticsJobParametersSkipTableTypesItem]]):
    """

    full_update_hour_of_day: Union[Unset, int] = UNSET
    last_years: Union[Unset, int] = UNSET
    skip_outliers: Union[Unset, bool] = UNSET
    skip_table_types: Union[Unset, list[ContinuousAnalyticsJobParametersSkipTableTypesItem]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        full_update_hour_of_day = self.full_update_hour_of_day

        last_years = self.last_years

        skip_outliers = self.skip_outliers

        skip_table_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.skip_table_types, Unset):
            skip_table_types = []
            for skip_table_types_item_data in self.skip_table_types:
                skip_table_types_item = skip_table_types_item_data.value
                skip_table_types.append(skip_table_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if full_update_hour_of_day is not UNSET:
            field_dict["fullUpdateHourOfDay"] = full_update_hour_of_day
        if last_years is not UNSET:
            field_dict["lastYears"] = last_years
        if skip_outliers is not UNSET:
            field_dict["skipOutliers"] = skip_outliers
        if skip_table_types is not UNSET:
            field_dict["skipTableTypes"] = skip_table_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        full_update_hour_of_day = d.pop("fullUpdateHourOfDay", UNSET)

        last_years = d.pop("lastYears", UNSET)

        skip_outliers = d.pop("skipOutliers", UNSET)

        skip_table_types = []
        _skip_table_types = d.pop("skipTableTypes", UNSET)
        for skip_table_types_item_data in _skip_table_types or []:
            skip_table_types_item = ContinuousAnalyticsJobParametersSkipTableTypesItem(skip_table_types_item_data)

            skip_table_types.append(skip_table_types_item)

        continuous_analytics_job_parameters = cls(
            full_update_hour_of_day=full_update_hour_of_day,
            last_years=last_years,
            skip_outliers=skip_outliers,
            skip_table_types=skip_table_types,
        )

        continuous_analytics_job_parameters.additional_properties = d
        return continuous_analytics_job_parameters

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
