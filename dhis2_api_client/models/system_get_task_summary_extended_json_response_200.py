from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.system_get_task_summary_extended_json_response_200_additional_property import (
        SystemGetTaskSummaryExtendedJsonResponse200AdditionalProperty,
    )


T = TypeVar("T", bound="SystemGetTaskSummaryExtendedJsonResponse200")


@_attrs_define
class SystemGetTaskSummaryExtendedJsonResponse200:
    """ """

    additional_properties: dict[str, "SystemGetTaskSummaryExtendedJsonResponse200AdditionalProperty"] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.system_get_task_summary_extended_json_response_200_additional_property import (
            SystemGetTaskSummaryExtendedJsonResponse200AdditionalProperty,
        )

        d = src_dict.copy()
        system_get_task_summary_extended_json_response_200 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = SystemGetTaskSummaryExtendedJsonResponse200AdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        system_get_task_summary_extended_json_response_200.additional_properties = additional_properties
        return system_get_task_summary_extended_json_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "SystemGetTaskSummaryExtendedJsonResponse200AdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "SystemGetTaskSummaryExtendedJsonResponse200AdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
