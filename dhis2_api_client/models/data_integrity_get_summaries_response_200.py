from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.data_integrity_summary import DataIntegritySummary


T = TypeVar("T", bound="DataIntegrityGetSummariesResponse200")


@_attrs_define
class DataIntegrityGetSummariesResponse200:
    """ """

    additional_properties: dict[str, "DataIntegritySummary"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.data_integrity_summary import DataIntegritySummary

        d = src_dict.copy()
        data_integrity_get_summaries_response_200 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = DataIntegritySummary.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        data_integrity_get_summaries_response_200.additional_properties = additional_properties
        return data_integrity_get_summaries_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "DataIntegritySummary":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "DataIntegritySummary") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
