from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MinMaxValueParams")


@_attrs_define
class MinMaxValueParams:
    """
    Attributes:
        data_sets (Union[Unset, list[str]]):
        organisation_unit (Union[Unset, str]):
    """

    data_sets: Union[Unset, list[str]] = UNSET
    organisation_unit: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_sets: Union[Unset, list[str]] = UNSET
        if not isinstance(self.data_sets, Unset):
            data_sets = self.data_sets

        organisation_unit = self.organisation_unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_sets is not UNSET:
            field_dict["dataSets"] = data_sets
        if organisation_unit is not UNSET:
            field_dict["organisationUnit"] = organisation_unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        data_sets = cast(list[str], d.pop("dataSets", UNSET))

        organisation_unit = d.pop("organisationUnit", UNSET)

        min_max_value_params = cls(
            data_sets=data_sets,
            organisation_unit=organisation_unit,
        )

        min_max_value_params.additional_properties = d
        return min_max_value_params

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
