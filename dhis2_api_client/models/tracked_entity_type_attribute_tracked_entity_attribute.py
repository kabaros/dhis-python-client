from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TrackedEntityTypeAttributeTrackedEntityAttribute")


@_attrs_define
class TrackedEntityTypeAttributeTrackedEntityAttribute:
    """A UID reference to a TrackedEntityAttribute
    (Java name `org.hisp.dhis.trackedentity.TrackedEntityAttribute`)

        Attributes:
            id (str):  Example: Ip8AV7eW679.
    """

    id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        tracked_entity_type_attribute_tracked_entity_attribute = cls(
            id=id,
        )

        tracked_entity_type_attribute_tracked_entity_attribute.additional_properties = d
        return tracked_entity_type_attribute_tracked_entity_attribute

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
