import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.query_modifiers_aggregation_type import QueryModifiersAggregationType
from ..models.query_modifiers_value_type import QueryModifiersValueType
from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryModifiers")


@_attrs_define
class QueryModifiers:
    """
    Attributes:
        aggregation_type (QueryModifiersAggregationType):
        period_offset (int):
        value_type (QueryModifiersValueType):
        max_date (Union[Unset, datetime.datetime]):
        min_date (Union[Unset, datetime.datetime]):
        year_to_date (Union[Unset, bool]):
    """

    aggregation_type: QueryModifiersAggregationType
    period_offset: int
    value_type: QueryModifiersValueType
    max_date: Union[Unset, datetime.datetime] = UNSET
    min_date: Union[Unset, datetime.datetime] = UNSET
    year_to_date: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregation_type = self.aggregation_type.value

        period_offset = self.period_offset

        value_type = self.value_type.value

        max_date: Union[Unset, str] = UNSET
        if not isinstance(self.max_date, Unset):
            max_date = self.max_date.isoformat()

        min_date: Union[Unset, str] = UNSET
        if not isinstance(self.min_date, Unset):
            min_date = self.min_date.isoformat()

        year_to_date = self.year_to_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aggregationType": aggregation_type,
                "periodOffset": period_offset,
                "valueType": value_type,
            }
        )
        if max_date is not UNSET:
            field_dict["maxDate"] = max_date
        if min_date is not UNSET:
            field_dict["minDate"] = min_date
        if year_to_date is not UNSET:
            field_dict["yearToDate"] = year_to_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        aggregation_type = QueryModifiersAggregationType(d.pop("aggregationType"))

        period_offset = d.pop("periodOffset")

        value_type = QueryModifiersValueType(d.pop("valueType"))

        _max_date = d.pop("maxDate", UNSET)
        max_date: Union[Unset, datetime.datetime]
        if isinstance(_max_date, Unset):
            max_date = UNSET
        else:
            max_date = isoparse(_max_date)

        _min_date = d.pop("minDate", UNSET)
        min_date: Union[Unset, datetime.datetime]
        if isinstance(_min_date, Unset):
            min_date = UNSET
        else:
            min_date = isoparse(_min_date)

        year_to_date = d.pop("yearToDate", UNSET)

        query_modifiers = cls(
            aggregation_type=aggregation_type,
            period_offset=period_offset,
            value_type=value_type,
            max_date=max_date,
            min_date=min_date,
            year_to_date=year_to_date,
        )

        query_modifiers.additional_properties = d
        return query_modifiers

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
