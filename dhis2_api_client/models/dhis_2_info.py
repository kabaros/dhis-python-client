import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Dhis2Info")


@_attrs_define
class Dhis2Info:
    """
    Attributes:
        build_time (Union[Unset, datetime.datetime]):
        revision (Union[Unset, str]):
        server_date (Union[Unset, datetime.datetime]):
        system_id (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    build_time: Union[Unset, datetime.datetime] = UNSET
    revision: Union[Unset, str] = UNSET
    server_date: Union[Unset, datetime.datetime] = UNSET
    system_id: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        build_time: Union[Unset, str] = UNSET
        if not isinstance(self.build_time, Unset):
            build_time = self.build_time.isoformat()

        revision = self.revision

        server_date: Union[Unset, str] = UNSET
        if not isinstance(self.server_date, Unset):
            server_date = self.server_date.isoformat()

        system_id = self.system_id

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if build_time is not UNSET:
            field_dict["buildTime"] = build_time
        if revision is not UNSET:
            field_dict["revision"] = revision
        if server_date is not UNSET:
            field_dict["serverDate"] = server_date
        if system_id is not UNSET:
            field_dict["systemId"] = system_id
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _build_time = d.pop("buildTime", UNSET)
        build_time: Union[Unset, datetime.datetime]
        if isinstance(_build_time, Unset):
            build_time = UNSET
        else:
            build_time = isoparse(_build_time)

        revision = d.pop("revision", UNSET)

        _server_date = d.pop("serverDate", UNSET)
        server_date: Union[Unset, datetime.datetime]
        if isinstance(_server_date, Unset):
            server_date = UNSET
        else:
            server_date = isoparse(_server_date)

        system_id = d.pop("systemId", UNSET)

        version = d.pop("version", UNSET)

        dhis_2_info = cls(
            build_time=build_time,
            revision=revision,
            server_date=server_date,
            system_id=system_id,
            version=version,
        )

        dhis_2_info.additional_properties = d
        return dhis_2_info

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
