from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attribute_value_attribute import AttributeValueAttribute


T = TypeVar("T", bound="AttributeValue")


@_attrs_define
class AttributeValue:
    """
    Attributes:
        attribute (Union[Unset, AttributeValueAttribute]): A UID reference to a Attribute
            (Java name `org.hisp.dhis.attribute.Attribute`)
        value (Union[Unset, str]):
    """

    attribute: Union[Unset, "AttributeValueAttribute"] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attribute, Unset):
            attribute = self.attribute.to_dict()

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attribute is not UNSET:
            field_dict["attribute"] = attribute
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.attribute_value_attribute import AttributeValueAttribute

        d = src_dict.copy()
        _attribute = d.pop("attribute", UNSET)
        attribute: Union[Unset, AttributeValueAttribute]
        if isinstance(_attribute, Unset):
            attribute = UNSET
        else:
            attribute = AttributeValueAttribute.from_dict(_attribute)

        value = d.pop("value", UNSET)

        attribute_value = cls(
            attribute=attribute,
            value=value,
        )

        attribute_value.additional_properties = d
        return attribute_value

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
