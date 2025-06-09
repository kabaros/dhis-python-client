import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.tracker_attribute_value_type import TrackerAttributeValueType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TrackerAttribute")


@_attrs_define
class TrackerAttribute:
    """
    Attributes:
        value_type (TrackerAttributeValueType):
        attribute (Union[Unset, str]): A UID for an TrackerAttribute object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Attribute`) Example: ce5CG4iu357.
        code (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime, int]):
        display_name (Union[Unset, str]):
        stored_by (Union[Unset, str]):
        updated_at (Union[Unset, datetime.datetime, int]):
        value (Union[Unset, str]):
    """

    value_type: TrackerAttributeValueType
    attribute: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime, int] = UNSET
    display_name: Union[Unset, str] = UNSET
    stored_by: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime, int] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value_type = self.value_type.value

        attribute = self.attribute

        code = self.code

        created_at: Union[Unset, int, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        display_name = self.display_name

        stored_by = self.stored_by

        updated_at: Union[Unset, int, str]
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

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
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if stored_by is not UNSET:
            field_dict["storedBy"] = stored_by
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        value_type = TrackerAttributeValueType(d.pop("valueType"))

        attribute = d.pop("attribute", UNSET)

        code = d.pop("code", UNSET)

        def _parse_created_at(data: object) -> Union[Unset, datetime.datetime, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)

                return created_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Unset, datetime.datetime, int], data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))

        display_name = d.pop("displayName", UNSET)

        stored_by = d.pop("storedBy", UNSET)

        def _parse_updated_at(data: object) -> Union[Unset, datetime.datetime, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Unset, datetime.datetime, int], data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))

        value = d.pop("value", UNSET)

        tracker_attribute = cls(
            value_type=value_type,
            attribute=attribute,
            code=code,
            created_at=created_at,
            display_name=display_name,
            stored_by=stored_by,
            updated_at=updated_at,
            value=value,
        )

        tracker_attribute.additional_properties = d
        return tracker_attribute

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
