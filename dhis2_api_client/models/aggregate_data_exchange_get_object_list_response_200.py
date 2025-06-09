from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aggregate_data_exchange import AggregateDataExchange
    from ..models.pager import Pager


T = TypeVar("T", bound="AggregateDataExchangeGetObjectListResponse200")


@_attrs_define
class AggregateDataExchangeGetObjectListResponse200:
    """
    Attributes:
        pager (Union[Unset, Pager]):
        aggregate_data_exchanges (Union[Unset, list['AggregateDataExchange']]):
    """

    pager: Union[Unset, "Pager"] = UNSET
    aggregate_data_exchanges: Union[Unset, list["AggregateDataExchange"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        aggregate_data_exchanges: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.aggregate_data_exchanges, Unset):
            aggregate_data_exchanges = []
            for aggregate_data_exchanges_item_data in self.aggregate_data_exchanges:
                aggregate_data_exchanges_item = aggregate_data_exchanges_item_data.to_dict()
                aggregate_data_exchanges.append(aggregate_data_exchanges_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if aggregate_data_exchanges is not UNSET:
            field_dict["aggregateDataExchanges"] = aggregate_data_exchanges

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.aggregate_data_exchange import AggregateDataExchange
        from ..models.pager import Pager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, Pager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = Pager.from_dict(_pager)

        aggregate_data_exchanges = []
        _aggregate_data_exchanges = d.pop("aggregateDataExchanges", UNSET)
        for aggregate_data_exchanges_item_data in _aggregate_data_exchanges or []:
            aggregate_data_exchanges_item = AggregateDataExchange.from_dict(aggregate_data_exchanges_item_data)

            aggregate_data_exchanges.append(aggregate_data_exchanges_item)

        aggregate_data_exchange_get_object_list_response_200 = cls(
            pager=pager,
            aggregate_data_exchanges=aggregate_data_exchanges,
        )

        aggregate_data_exchange_get_object_list_response_200.additional_properties = d
        return aggregate_data_exchange_get_object_list_response_200

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
