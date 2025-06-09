import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseInfo")


@_attrs_define
class DatabaseInfo:
    """
    Attributes:
        database_version (Union[Unset, str]):
        name (Union[Unset, str]):
        spatial_support (Union[Unset, bool]):
        time (Union[Unset, datetime.datetime]):
        url (Union[Unset, str]):
        user (Union[Unset, str]):
    """

    database_version: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    spatial_support: Union[Unset, bool] = UNSET
    time: Union[Unset, datetime.datetime] = UNSET
    url: Union[Unset, str] = UNSET
    user: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        database_version = self.database_version

        name = self.name

        spatial_support = self.spatial_support

        time: Union[Unset, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        url = self.url

        user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if database_version is not UNSET:
            field_dict["databaseVersion"] = database_version
        if name is not UNSET:
            field_dict["name"] = name
        if spatial_support is not UNSET:
            field_dict["spatialSupport"] = spatial_support
        if time is not UNSET:
            field_dict["time"] = time
        if url is not UNSET:
            field_dict["url"] = url
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        database_version = d.pop("databaseVersion", UNSET)

        name = d.pop("name", UNSET)

        spatial_support = d.pop("spatialSupport", UNSET)

        _time = d.pop("time", UNSET)
        time: Union[Unset, datetime.datetime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        url = d.pop("url", UNSET)

        user = d.pop("user", UNSET)

        database_info = cls(
            database_version=database_version,
            name=name,
            spatial_support=spatial_support,
            time=time,
            url=url,
            user=user,
        )

        database_info.additional_properties = d
        return database_info

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
