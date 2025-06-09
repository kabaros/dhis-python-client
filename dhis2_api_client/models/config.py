from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.config_inclusion_strategy import ConfigInclusionStrategy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_properties import ConfigProperties


T = TypeVar("T", bound="Config")


@_attrs_define
class Config:
    """
    Attributes:
        inclusion_strategy (Union[Unset, ConfigInclusionStrategy]):
        properties (Union[Unset, ConfigProperties]):
    """

    inclusion_strategy: Union[Unset, ConfigInclusionStrategy] = UNSET
    properties: Union[Unset, "ConfigProperties"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inclusion_strategy: Union[Unset, str] = UNSET
        if not isinstance(self.inclusion_strategy, Unset):
            inclusion_strategy = self.inclusion_strategy.value

        properties: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inclusion_strategy is not UNSET:
            field_dict["inclusionStrategy"] = inclusion_strategy
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.config_properties import ConfigProperties

        d = src_dict.copy()
        _inclusion_strategy = d.pop("inclusionStrategy", UNSET)
        inclusion_strategy: Union[Unset, ConfigInclusionStrategy]
        if isinstance(_inclusion_strategy, Unset):
            inclusion_strategy = UNSET
        else:
            inclusion_strategy = ConfigInclusionStrategy(_inclusion_strategy)

        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, ConfigProperties]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = ConfigProperties.from_dict(_properties)

        config = cls(
            inclusion_strategy=inclusion_strategy,
            properties=properties,
        )

        config.additional_properties = d
        return config

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
