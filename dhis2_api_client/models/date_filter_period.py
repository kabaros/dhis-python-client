import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.date_filter_period_period import DateFilterPeriodPeriod
from ..models.date_filter_period_type import DateFilterPeriodType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DateFilterPeriod")


@_attrs_define
class DateFilterPeriod:
    """
    Attributes:
        end_buffer (int):
        period (DateFilterPeriodPeriod):
        start_buffer (int):
        type_ (DateFilterPeriodType):
        end_date (Union[Unset, datetime.datetime]):
        start_date (Union[Unset, datetime.datetime]):
    """

    end_buffer: int
    period: DateFilterPeriodPeriod
    start_buffer: int
    type_: DateFilterPeriodType
    end_date: Union[Unset, datetime.datetime] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_buffer = self.end_buffer

        period = self.period.value

        start_buffer = self.start_buffer

        type_ = self.type_.value

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endBuffer": end_buffer,
                "period": period,
                "startBuffer": start_buffer,
                "type": type_,
            }
        )
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if start_date is not UNSET:
            field_dict["startDate"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        end_buffer = d.pop("endBuffer")

        period = DateFilterPeriodPeriod(d.pop("period"))

        start_buffer = d.pop("startBuffer")

        type_ = DateFilterPeriodType(d.pop("type"))

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        date_filter_period = cls(
            end_buffer=end_buffer,
            period=period,
            start_buffer=start_buffer,
            type_=type_,
            end_date=end_date,
            start_date=start_date,
        )

        date_filter_period.additional_properties = d
        return date_filter_period

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
