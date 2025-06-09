from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AggregateDataExchangeJobParameters")


@_attrs_define
class AggregateDataExchangeJobParameters:
    """
    Attributes:
        data_exchange_ids (Union[Unset, list[str]]):
    """

    data_exchange_ids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_exchange_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.data_exchange_ids, Unset):
            data_exchange_ids = self.data_exchange_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_exchange_ids is not UNSET:
            field_dict["dataExchangeIds"] = data_exchange_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        data_exchange_ids = cast(list[str], d.pop("dataExchangeIds", UNSET))

        aggregate_data_exchange_job_parameters = cls(
            data_exchange_ids=data_exchange_ids,
        )

        aggregate_data_exchange_job_parameters.additional_properties = d
        return aggregate_data_exchange_job_parameters

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
