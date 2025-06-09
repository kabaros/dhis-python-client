import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReservedValue")


@_attrs_define
class ReservedValue:
    """
    Attributes:
        created (Union[Unset, datetime.datetime]):
        expiry_date (Union[Unset, datetime.datetime]):
        key (Union[Unset, str]):
        owner_object (Union[Unset, str]):
        owner_uid (Union[Unset, str]):
        value (Union[Unset, str]):
    """

    created: Union[Unset, datetime.datetime] = UNSET
    expiry_date: Union[Unset, datetime.datetime] = UNSET
    key: Union[Unset, str] = UNSET
    owner_object: Union[Unset, str] = UNSET
    owner_uid: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        expiry_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiry_date, Unset):
            expiry_date = self.expiry_date.isoformat()

        key = self.key

        owner_object = self.owner_object

        owner_uid = self.owner_uid

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if expiry_date is not UNSET:
            field_dict["expiryDate"] = expiry_date
        if key is not UNSET:
            field_dict["key"] = key
        if owner_object is not UNSET:
            field_dict["ownerObject"] = owner_object
        if owner_uid is not UNSET:
            field_dict["ownerUid"] = owner_uid
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _expiry_date = d.pop("expiryDate", UNSET)
        expiry_date: Union[Unset, datetime.datetime]
        if isinstance(_expiry_date, Unset):
            expiry_date = UNSET
        else:
            expiry_date = isoparse(_expiry_date)

        key = d.pop("key", UNSET)

        owner_object = d.pop("ownerObject", UNSET)

        owner_uid = d.pop("ownerUid", UNSET)

        value = d.pop("value", UNSET)

        reserved_value = cls(
            created=created,
            expiry_date=expiry_date,
            key=key,
            owner_object=owner_object,
            owner_uid=owner_uid,
            value=value,
        )

        reserved_value.additional_properties = d
        return reserved_value

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
