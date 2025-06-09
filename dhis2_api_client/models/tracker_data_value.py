import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tracker_user import TrackerUser


T = TypeVar("T", bound="TrackerDataValue")


@_attrs_define
class TrackerDataValue:
    """
    Attributes:
        created_at (Union[Unset, datetime.datetime, int]):
        created_by (Union[Unset, TrackerUser]):
        data_element (Union[Unset, str]): A UID for an DataElement object
            (Java name `org.hisp.dhis.dataelement.DataElement`) Example: hX7n8Y4pu89.
        provided_elsewhere (Union[Unset, bool]):
        stored_by (Union[Unset, str]):
        updated_at (Union[Unset, datetime.datetime, int]):
        updated_by (Union[Unset, TrackerUser]):
        value (Union[Unset, str]):
    """

    created_at: Union[Unset, datetime.datetime, int] = UNSET
    created_by: Union[Unset, "TrackerUser"] = UNSET
    data_element: Union[Unset, str] = UNSET
    provided_elsewhere: Union[Unset, bool] = UNSET
    stored_by: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime, int] = UNSET
    updated_by: Union[Unset, "TrackerUser"] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at: Union[Unset, int, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        data_element = self.data_element

        provided_elsewhere = self.provided_elsewhere

        stored_by = self.stored_by

        updated_at: Union[Unset, int, str]
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.updated_by, Unset):
            updated_by = self.updated_by.to_dict()

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if data_element is not UNSET:
            field_dict["dataElement"] = data_element
        if provided_elsewhere is not UNSET:
            field_dict["providedElsewhere"] = provided_elsewhere
        if stored_by is not UNSET:
            field_dict["storedBy"] = stored_by
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tracker_user import TrackerUser

        d = src_dict.copy()

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

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, TrackerUser]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = TrackerUser.from_dict(_created_by)

        data_element = d.pop("dataElement", UNSET)

        provided_elsewhere = d.pop("providedElsewhere", UNSET)

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

        _updated_by = d.pop("updatedBy", UNSET)
        updated_by: Union[Unset, TrackerUser]
        if isinstance(_updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = TrackerUser.from_dict(_updated_by)

        value = d.pop("value", UNSET)

        tracker_data_value = cls(
            created_at=created_at,
            created_by=created_by,
            data_element=data_element,
            provided_elsewhere=provided_elsewhere,
            stored_by=stored_by,
            updated_at=updated_at,
            updated_by=updated_by,
            value=value,
        )

        tracker_data_value.additional_properties = d
        return tracker_data_value

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
