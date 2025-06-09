import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tracked_entity_attribute_value_tracked_entity_attribute import (
        TrackedEntityAttributeValueTrackedEntityAttribute,
    )
    from ..models.tracked_entity_attribute_value_tracked_entity_instance import (
        TrackedEntityAttributeValueTrackedEntityInstance,
    )


T = TypeVar("T", bound="TrackedEntityAttributeValue")


@_attrs_define
class TrackedEntityAttributeValue:
    """
    Attributes:
        created (Union[Unset, datetime.datetime]):
        last_updated (Union[Unset, datetime.datetime]):
        stored_by (Union[Unset, str]):
        tracked_entity_attribute (Union[Unset, TrackedEntityAttributeValueTrackedEntityAttribute]): A UID reference to a
            TrackedEntityAttribute
            (Java name `org.hisp.dhis.trackedentity.TrackedEntityAttribute`)
        tracked_entity_instance (Union[Unset, TrackedEntityAttributeValueTrackedEntityInstance]): A UID reference to a
            TrackedEntity
            (Java name `org.hisp.dhis.trackedentity.TrackedEntity`)
        value (Union[Unset, str]):
    """

    created: Union[Unset, datetime.datetime] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    stored_by: Union[Unset, str] = UNSET
    tracked_entity_attribute: Union[Unset, "TrackedEntityAttributeValueTrackedEntityAttribute"] = UNSET
    tracked_entity_instance: Union[Unset, "TrackedEntityAttributeValueTrackedEntityInstance"] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        stored_by = self.stored_by

        tracked_entity_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tracked_entity_attribute, Unset):
            tracked_entity_attribute = self.tracked_entity_attribute.to_dict()

        tracked_entity_instance: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tracked_entity_instance, Unset):
            tracked_entity_instance = self.tracked_entity_instance.to_dict()

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if stored_by is not UNSET:
            field_dict["storedBy"] = stored_by
        if tracked_entity_attribute is not UNSET:
            field_dict["trackedEntityAttribute"] = tracked_entity_attribute
        if tracked_entity_instance is not UNSET:
            field_dict["trackedEntityInstance"] = tracked_entity_instance
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tracked_entity_attribute_value_tracked_entity_attribute import (
            TrackedEntityAttributeValueTrackedEntityAttribute,
        )
        from ..models.tracked_entity_attribute_value_tracked_entity_instance import (
            TrackedEntityAttributeValueTrackedEntityInstance,
        )

        d = src_dict.copy()
        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        stored_by = d.pop("storedBy", UNSET)

        _tracked_entity_attribute = d.pop("trackedEntityAttribute", UNSET)
        tracked_entity_attribute: Union[Unset, TrackedEntityAttributeValueTrackedEntityAttribute]
        if isinstance(_tracked_entity_attribute, Unset):
            tracked_entity_attribute = UNSET
        else:
            tracked_entity_attribute = TrackedEntityAttributeValueTrackedEntityAttribute.from_dict(
                _tracked_entity_attribute
            )

        _tracked_entity_instance = d.pop("trackedEntityInstance", UNSET)
        tracked_entity_instance: Union[Unset, TrackedEntityAttributeValueTrackedEntityInstance]
        if isinstance(_tracked_entity_instance, Unset):
            tracked_entity_instance = UNSET
        else:
            tracked_entity_instance = TrackedEntityAttributeValueTrackedEntityInstance.from_dict(
                _tracked_entity_instance
            )

        value = d.pop("value", UNSET)

        tracked_entity_attribute_value = cls(
            created=created,
            last_updated=last_updated,
            stored_by=stored_by,
            tracked_entity_attribute=tracked_entity_attribute,
            tracked_entity_instance=tracked_entity_instance,
            value=value,
        )

        tracked_entity_attribute_value.additional_properties = d
        return tracked_entity_attribute_value

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
