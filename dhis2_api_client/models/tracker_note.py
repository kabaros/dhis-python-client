import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tracker_user import TrackerUser


T = TypeVar("T", bound="TrackerNote")


@_attrs_define
class TrackerNote:
    """
    Attributes:
        created_by (Union[Unset, TrackerUser]):
        note (Union[Unset, str]): A UID for an TrackerNote object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Note`) Example: k4mk6Uc50K2.
        stored_at (Union[Unset, datetime.datetime, int]):
        stored_by (Union[Unset, str]):
        value (Union[Unset, str]):
    """

    created_by: Union[Unset, "TrackerUser"] = UNSET
    note: Union[Unset, str] = UNSET
    stored_at: Union[Unset, datetime.datetime, int] = UNSET
    stored_by: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        note = self.note

        stored_at: Union[Unset, int, str]
        if isinstance(self.stored_at, Unset):
            stored_at = UNSET
        elif isinstance(self.stored_at, datetime.datetime):
            stored_at = self.stored_at.isoformat()
        else:
            stored_at = self.stored_at

        stored_by = self.stored_by

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if note is not UNSET:
            field_dict["note"] = note
        if stored_at is not UNSET:
            field_dict["storedAt"] = stored_at
        if stored_by is not UNSET:
            field_dict["storedBy"] = stored_by
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tracker_user import TrackerUser

        d = src_dict.copy()
        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, TrackerUser]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = TrackerUser.from_dict(_created_by)

        note = d.pop("note", UNSET)

        def _parse_stored_at(data: object) -> Union[Unset, datetime.datetime, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                stored_at_type_0 = isoparse(data)

                return stored_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Unset, datetime.datetime, int], data)

        stored_at = _parse_stored_at(d.pop("storedAt", UNSET))

        stored_by = d.pop("storedBy", UNSET)

        value = d.pop("value", UNSET)

        tracker_note = cls(
            created_by=created_by,
            note=note,
            stored_at=stored_at,
            stored_by=stored_by,
            value=value,
        )

        tracker_note.additional_properties = d
        return tracker_note

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
