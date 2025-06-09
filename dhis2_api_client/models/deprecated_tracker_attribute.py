from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deprecated_tracker_attribute_value_type import DeprecatedTrackerAttributeValueType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeprecatedTrackerAttribute")


@_attrs_define
class DeprecatedTrackerAttribute:
    """
    Attributes:
        value_type (DeprecatedTrackerAttributeValueType):
        attribute (Union[Unset, str]):
        code (Union[Unset, str]):
        created (Union[Unset, str]):
        display_name (Union[Unset, str]):
        last_updated (Union[Unset, str]):
        stored_by (Union[Unset, str]):
        value (Union[Unset, str]):
    """

    value_type: DeprecatedTrackerAttributeValueType
    attribute: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    last_updated: Union[Unset, str] = UNSET
    stored_by: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value_type = self.value_type.value

        attribute = self.attribute

        code = self.code

        created = self.created

        display_name = self.display_name

        last_updated = self.last_updated

        stored_by = self.stored_by

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "valueType": value_type,
            }
        )
        if attribute is not UNSET:
            field_dict["attribute"] = attribute
        if code is not UNSET:
            field_dict["code"] = code
        if created is not UNSET:
            field_dict["created"] = created
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if stored_by is not UNSET:
            field_dict["storedBy"] = stored_by
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        value_type = DeprecatedTrackerAttributeValueType(d.pop("valueType"))

        attribute = d.pop("attribute", UNSET)

        code = d.pop("code", UNSET)

        created = d.pop("created", UNSET)

        display_name = d.pop("displayName", UNSET)

        last_updated = d.pop("lastUpdated", UNSET)

        stored_by = d.pop("storedBy", UNSET)

        value = d.pop("value", UNSET)

        deprecated_tracker_attribute = cls(
            value_type=value_type,
            attribute=attribute,
            code=code,
            created=created,
            display_name=display_name,
            last_updated=last_updated,
            stored_by=stored_by,
            value=value,
        )

        deprecated_tracker_attribute.additional_properties = d
        return deprecated_tracker_attribute

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
