import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeletedObject")


@_attrs_define
class DeletedObject:
    """
    Attributes:
        code (Union[Unset, str]):
        deleted_at (Union[Unset, datetime.datetime]):
        deleted_by (Union[Unset, str]):
        klass (Union[Unset, str]):
        uid (Union[Unset, str]):
    """

    code: Union[Unset, str] = UNSET
    deleted_at: Union[Unset, datetime.datetime] = UNSET
    deleted_by: Union[Unset, str] = UNSET
    klass: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        deleted_at: Union[Unset, str] = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

        deleted_by = self.deleted_by

        klass = self.klass

        uid = self.uid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if deleted_by is not UNSET:
            field_dict["deletedBy"] = deleted_by
        if klass is not UNSET:
            field_dict["klass"] = klass
        if uid is not UNSET:
            field_dict["uid"] = uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code", UNSET)

        _deleted_at = d.pop("deletedAt", UNSET)
        deleted_at: Union[Unset, datetime.datetime]
        if isinstance(_deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = isoparse(_deleted_at)

        deleted_by = d.pop("deletedBy", UNSET)

        klass = d.pop("klass", UNSET)

        uid = d.pop("uid", UNSET)

        deleted_object = cls(
            code=code,
            deleted_at=deleted_at,
            deleted_by=deleted_by,
            klass=klass,
            uid=uid,
        )

        deleted_object.additional_properties = d
        return deleted_object

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
