import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_info_snapshot import UserInfoSnapshot


T = TypeVar("T", bound="DeprecatedTrackerNote")


@_attrs_define
class DeprecatedTrackerNote:
    """
    Attributes:
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, UserInfoSnapshot]):
        note (Union[Unset, str]):
        stored_by (Union[Unset, str]):
        stored_date (Union[Unset, str]):
        value (Union[Unset, str]):
    """

    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "UserInfoSnapshot"] = UNSET
    note: Union[Unset, str] = UNSET
    stored_by: Union[Unset, str] = UNSET
    stored_date: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        note = self.note

        stored_by = self.stored_by

        stored_date = self.stored_date

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if note is not UNSET:
            field_dict["note"] = note
        if stored_by is not UNSET:
            field_dict["storedBy"] = stored_by
        if stored_date is not UNSET:
            field_dict["storedDate"] = stored_date
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.user_info_snapshot import UserInfoSnapshot

        d = src_dict.copy()
        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, UserInfoSnapshot]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = UserInfoSnapshot.from_dict(_last_updated_by)

        note = d.pop("note", UNSET)

        stored_by = d.pop("storedBy", UNSET)

        stored_date = d.pop("storedDate", UNSET)

        value = d.pop("value", UNSET)

        deprecated_tracker_note = cls(
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            note=note,
            stored_by=stored_by,
            stored_date=stored_date,
            value=value,
        )

        deprecated_tracker_note.additional_properties = d
        return deprecated_tracker_note

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
