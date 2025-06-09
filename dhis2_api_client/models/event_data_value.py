import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_info_snapshot import UserInfoSnapshot


T = TypeVar("T", bound="EventDataValue")


@_attrs_define
class EventDataValue:
    """
    Attributes:
        created (Union[Unset, datetime.datetime]):
        created_by_user_info (Union[Unset, UserInfoSnapshot]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by_user_info (Union[Unset, UserInfoSnapshot]):
        provided_elsewhere (Union[Unset, bool]):
        stored_by (Union[Unset, str]):
        value (Union[Unset, str]):
    """

    created: Union[Unset, datetime.datetime] = UNSET
    created_by_user_info: Union[Unset, "UserInfoSnapshot"] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by_user_info: Union[Unset, "UserInfoSnapshot"] = UNSET
    provided_elsewhere: Union[Unset, bool] = UNSET
    stored_by: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by_user_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by_user_info, Unset):
            created_by_user_info = self.created_by_user_info.to_dict()

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by_user_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by_user_info, Unset):
            last_updated_by_user_info = self.last_updated_by_user_info.to_dict()

        provided_elsewhere = self.provided_elsewhere

        stored_by = self.stored_by

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if created_by_user_info is not UNSET:
            field_dict["createdByUserInfo"] = created_by_user_info
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by_user_info is not UNSET:
            field_dict["lastUpdatedByUserInfo"] = last_updated_by_user_info
        if provided_elsewhere is not UNSET:
            field_dict["providedElsewhere"] = provided_elsewhere
        if stored_by is not UNSET:
            field_dict["storedBy"] = stored_by
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.user_info_snapshot import UserInfoSnapshot

        d = src_dict.copy()
        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by_user_info = d.pop("createdByUserInfo", UNSET)
        created_by_user_info: Union[Unset, UserInfoSnapshot]
        if isinstance(_created_by_user_info, Unset):
            created_by_user_info = UNSET
        else:
            created_by_user_info = UserInfoSnapshot.from_dict(_created_by_user_info)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by_user_info = d.pop("lastUpdatedByUserInfo", UNSET)
        last_updated_by_user_info: Union[Unset, UserInfoSnapshot]
        if isinstance(_last_updated_by_user_info, Unset):
            last_updated_by_user_info = UNSET
        else:
            last_updated_by_user_info = UserInfoSnapshot.from_dict(_last_updated_by_user_info)

        provided_elsewhere = d.pop("providedElsewhere", UNSET)

        stored_by = d.pop("storedBy", UNSET)

        value = d.pop("value", UNSET)

        event_data_value = cls(
            created=created,
            created_by_user_info=created_by_user_info,
            last_updated=last_updated,
            last_updated_by_user_info=last_updated_by_user_info,
            provided_elsewhere=provided_elsewhere,
            stored_by=stored_by,
            value=value,
        )

        event_data_value.additional_properties = d
        return event_data_value

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
