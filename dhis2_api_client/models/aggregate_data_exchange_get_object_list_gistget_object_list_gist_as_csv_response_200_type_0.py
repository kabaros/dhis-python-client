from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aggregate_data_exchange_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_aggregate_data_exchanges_item import (
        AggregateDataExchangeGetObjectListGistgetObjectListGistAsCsvResponse200Type0AggregateDataExchangesItem,
    )
    from ..models.gist_pager import GistPager


T = TypeVar("T", bound="AggregateDataExchangeGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class AggregateDataExchangeGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        aggregate_data_exchanges (Union[Unset, list['AggregateDataExchangeGetObjectListGistgetObjectListGistAsCsvRespons
            e200Type0AggregateDataExchangesItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    aggregate_data_exchanges: Union[
        Unset,
        list["AggregateDataExchangeGetObjectListGistgetObjectListGistAsCsvResponse200Type0AggregateDataExchangesItem"],
    ] = UNSET
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
        from ..models.aggregate_data_exchange_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_aggregate_data_exchanges_item import (
            AggregateDataExchangeGetObjectListGistgetObjectListGistAsCsvResponse200Type0AggregateDataExchangesItem,
        )
        from ..models.gist_pager import GistPager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        aggregate_data_exchanges = []
        _aggregate_data_exchanges = d.pop("aggregateDataExchanges", UNSET)
        for aggregate_data_exchanges_item_data in _aggregate_data_exchanges or []:
            aggregate_data_exchanges_item = AggregateDataExchangeGetObjectListGistgetObjectListGistAsCsvResponse200Type0AggregateDataExchangesItem.from_dict(
                aggregate_data_exchanges_item_data
            )

            aggregate_data_exchanges.append(aggregate_data_exchanges_item)

        aggregate_data_exchange_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            aggregate_data_exchanges=aggregate_data_exchanges,
        )

        aggregate_data_exchange_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return aggregate_data_exchange_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
