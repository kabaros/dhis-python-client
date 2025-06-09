from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.date_filter_period import DateFilterPeriod


T = TypeVar("T", bound="EventDataFilter")


@_attrs_define
class EventDataFilter:
    """
    Attributes:
        data_item (Union[Unset, str]):
        date_filter (Union[Unset, DateFilterPeriod]):
        eq (Union[Unset, str]):
        ge (Union[Unset, str]):
        gt (Union[Unset, str]):
        in_ (Union[Unset, list[str]]):
        le (Union[Unset, str]):
        like (Union[Unset, str]):
        lt (Union[Unset, str]):
    """

    data_item: Union[Unset, str] = UNSET
    date_filter: Union[Unset, "DateFilterPeriod"] = UNSET
    eq: Union[Unset, str] = UNSET
    ge: Union[Unset, str] = UNSET
    gt: Union[Unset, str] = UNSET
    in_: Union[Unset, list[str]] = UNSET
    le: Union[Unset, str] = UNSET
    like: Union[Unset, str] = UNSET
    lt: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_item = self.data_item

        date_filter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.date_filter, Unset):
            date_filter = self.date_filter.to_dict()

        eq = self.eq

        ge = self.ge

        gt = self.gt

        in_: Union[Unset, list[str]] = UNSET
        if not isinstance(self.in_, Unset):
            in_ = self.in_

        le = self.le

        like = self.like

        lt = self.lt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_item is not UNSET:
            field_dict["dataItem"] = data_item
        if date_filter is not UNSET:
            field_dict["dateFilter"] = date_filter
        if eq is not UNSET:
            field_dict["eq"] = eq
        if ge is not UNSET:
            field_dict["ge"] = ge
        if gt is not UNSET:
            field_dict["gt"] = gt
        if in_ is not UNSET:
            field_dict["in"] = in_
        if le is not UNSET:
            field_dict["le"] = le
        if like is not UNSET:
            field_dict["like"] = like
        if lt is not UNSET:
            field_dict["lt"] = lt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.date_filter_period import DateFilterPeriod

        d = src_dict.copy()
        data_item = d.pop("dataItem", UNSET)

        _date_filter = d.pop("dateFilter", UNSET)
        date_filter: Union[Unset, DateFilterPeriod]
        if isinstance(_date_filter, Unset):
            date_filter = UNSET
        else:
            date_filter = DateFilterPeriod.from_dict(_date_filter)

        eq = d.pop("eq", UNSET)

        ge = d.pop("ge", UNSET)

        gt = d.pop("gt", UNSET)

        in_ = cast(list[str], d.pop("in", UNSET))

        le = d.pop("le", UNSET)

        like = d.pop("like", UNSET)

        lt = d.pop("lt", UNSET)

        event_data_filter = cls(
            data_item=data_item,
            date_filter=date_filter,
            eq=eq,
            ge=ge,
            gt=gt,
            in_=in_,
            le=le,
            like=like,
            lt=lt,
        )

        event_data_filter.additional_properties = d
        return event_data_filter

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
