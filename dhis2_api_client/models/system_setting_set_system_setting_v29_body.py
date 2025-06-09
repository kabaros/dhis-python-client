from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.system_setting_set_system_setting_v29_body_additional_property import (
        SystemSettingSetSystemSettingV29BodyAdditionalProperty,
    )


T = TypeVar("T", bound="SystemSettingSetSystemSettingV29Body")


@_attrs_define
class SystemSettingSetSystemSettingV29Body:
    """ """

    additional_properties: dict[str, "SystemSettingSetSystemSettingV29BodyAdditionalProperty"] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.system_setting_set_system_setting_v29_body_additional_property import (
            SystemSettingSetSystemSettingV29BodyAdditionalProperty,
        )

        d = src_dict.copy()
        system_setting_set_system_setting_v29_body = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = SystemSettingSetSystemSettingV29BodyAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        system_setting_set_system_setting_v29_body.additional_properties = additional_properties
        return system_setting_set_system_setting_v29_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "SystemSettingSetSystemSettingV29BodyAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "SystemSettingSetSystemSettingV29BodyAdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
