import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataInputPeriod")


@_attrs_define
class DataInputPeriod:
    """
    Attributes:
        closing_date (Union[Unset, datetime.datetime]):
        opening_date (Union[Unset, datetime.datetime]):
        period (Union[Unset, str]):
    """

    closing_date: Union[Unset, datetime.datetime] = UNSET
    opening_date: Union[Unset, datetime.datetime] = UNSET
    period: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        closing_date: Union[Unset, str] = UNSET
        if not isinstance(self.closing_date, Unset):
            closing_date = self.closing_date.isoformat()

        opening_date: Union[Unset, str] = UNSET
        if not isinstance(self.opening_date, Unset):
            opening_date = self.opening_date.isoformat()

        period = self.period

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if closing_date is not UNSET:
            field_dict["closingDate"] = closing_date
        if opening_date is not UNSET:
            field_dict["openingDate"] = opening_date
        if period is not UNSET:
            field_dict["period"] = period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _closing_date = d.pop("closingDate", UNSET)
        closing_date: Union[Unset, datetime.datetime]
        if isinstance(_closing_date, Unset):
            closing_date = UNSET
        else:
            closing_date = isoparse(_closing_date)

        _opening_date = d.pop("openingDate", UNSET)
        opening_date: Union[Unset, datetime.datetime]
        if isinstance(_opening_date, Unset):
            opening_date = UNSET
        else:
            opening_date = isoparse(_opening_date)

        period = d.pop("period", UNSET)

        data_input_period = cls(
            closing_date=closing_date,
            opening_date=opening_date,
            period=period,
        )

        data_input_period.additional_properties = d
        return data_input_period

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
