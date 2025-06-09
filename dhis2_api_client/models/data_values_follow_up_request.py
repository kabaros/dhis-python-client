from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_value_follow_up_request import DataValueFollowUpRequest


T = TypeVar("T", bound="DataValuesFollowUpRequest")


@_attrs_define
class DataValuesFollowUpRequest:
    """
    Attributes:
        values (Union[Unset, list['DataValueFollowUpRequest']]):
    """

    values: Union[Unset, list["DataValueFollowUpRequest"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.data_value_follow_up_request import DataValueFollowUpRequest

        d = src_dict.copy()
        values = []
        _values = d.pop("values", UNSET)
        for values_item_data in _values or []:
            values_item = DataValueFollowUpRequest.from_dict(values_item_data)

            values.append(values_item)

        data_values_follow_up_request = cls(
            values=values,
        )

        data_values_follow_up_request.additional_properties = d
        return data_values_follow_up_request

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
