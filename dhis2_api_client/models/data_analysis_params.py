from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataAnalysisParams")


@_attrs_define
class DataAnalysisParams:
    """
    Attributes:
        ds (Union[Unset, list[str]]):
        end_date (Union[Unset, str]):
        ou (Union[Unset, str]):
        standard_deviation (Union[Unset, float]):
        start_date (Union[Unset, str]):
    """

    ds: Union[Unset, list[str]] = UNSET
    end_date: Union[Unset, str] = UNSET
    ou: Union[Unset, str] = UNSET
    standard_deviation: Union[Unset, float] = UNSET
    start_date: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ds: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ds, Unset):
            ds = self.ds

        end_date = self.end_date

        ou = self.ou

        standard_deviation = self.standard_deviation

        start_date = self.start_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ds is not UNSET:
            field_dict["ds"] = ds
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if ou is not UNSET:
            field_dict["ou"] = ou
        if standard_deviation is not UNSET:
            field_dict["standardDeviation"] = standard_deviation
        if start_date is not UNSET:
            field_dict["startDate"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        ds = cast(list[str], d.pop("ds", UNSET))

        end_date = d.pop("endDate", UNSET)

        ou = d.pop("ou", UNSET)

        standard_deviation = d.pop("standardDeviation", UNSET)

        start_date = d.pop("startDate", UNSET)

        data_analysis_params = cls(
            ds=ds,
            end_date=end_date,
            ou=ou,
            standard_deviation=standard_deviation,
            start_date=start_date,
        )

        data_analysis_params.additional_properties = d
        return data_analysis_params

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
