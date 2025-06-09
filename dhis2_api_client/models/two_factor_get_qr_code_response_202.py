from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.two_factor_get_qr_code_response_202_additional_property import (
        TwoFactorGetQrCodeResponse202AdditionalProperty,
    )


T = TypeVar("T", bound="TwoFactorGetQrCodeResponse202")


@_attrs_define
class TwoFactorGetQrCodeResponse202:
    """ """

    additional_properties: dict[str, "TwoFactorGetQrCodeResponse202AdditionalProperty"] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.two_factor_get_qr_code_response_202_additional_property import (
            TwoFactorGetQrCodeResponse202AdditionalProperty,
        )

        d = src_dict.copy()
        two_factor_get_qr_code_response_202 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = TwoFactorGetQrCodeResponse202AdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        two_factor_get_qr_code_response_202.additional_properties = additional_properties
        return two_factor_get_qr_code_response_202

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "TwoFactorGetQrCodeResponse202AdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "TwoFactorGetQrCodeResponse202AdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
