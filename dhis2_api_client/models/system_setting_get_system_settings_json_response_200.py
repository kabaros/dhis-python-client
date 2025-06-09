from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SystemSettingGetSystemSettingsJsonResponse200")


@_attrs_define
class SystemSettingGetSystemSettingsJsonResponse200:
    """ """

    additional_properties: dict[str, Union[bool, float, str]] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        system_setting_get_system_settings_json_response_200 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(data: object) -> Union[bool, float, str]:
                return cast(Union[bool, float, str], data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        system_setting_get_system_settings_json_response_200.additional_properties = additional_properties
        return system_setting_get_system_settings_json_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Union[bool, float, str]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Union[bool, float, str]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
