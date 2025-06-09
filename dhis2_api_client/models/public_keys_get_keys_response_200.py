from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.public_keys_get_keys_response_200_additional_property import (
        PublicKeysGetKeysResponse200AdditionalProperty,
    )


T = TypeVar("T", bound="PublicKeysGetKeysResponse200")


@_attrs_define
class PublicKeysGetKeysResponse200:
    """ """

    additional_properties: dict[str, "PublicKeysGetKeysResponse200AdditionalProperty"] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.public_keys_get_keys_response_200_additional_property import (
            PublicKeysGetKeysResponse200AdditionalProperty,
        )

        d = src_dict.copy()
        public_keys_get_keys_response_200 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = PublicKeysGetKeysResponse200AdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        public_keys_get_keys_response_200.additional_properties = additional_properties
        return public_keys_get_keys_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "PublicKeysGetKeysResponse200AdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "PublicKeysGetKeysResponse200AdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
