import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FollowupValue")


@_attrs_define
class FollowupValue:
    """
    Attributes:
        aoc (Union[Unset, str]):
        aoc_name (Union[Unset, str]):
        coc (Union[Unset, str]):
        coc_name (Union[Unset, str]):
        comment (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        de (Union[Unset, str]):
        de_name (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        max_ (Union[Unset, int]):
        min_ (Union[Unset, int]):
        ou (Union[Unset, str]):
        ou_name (Union[Unset, str]):
        ou_path (Union[Unset, str]):
        pe (Union[Unset, str]):
        pe_end_date (Union[Unset, datetime.datetime]):
        pe_name (Union[Unset, str]):
        pe_start_date (Union[Unset, datetime.datetime]):
        pe_type (Union[Unset, str]):
        stored_by (Union[Unset, str]):
        value (Union[Unset, str]):
    """

    aoc: Union[Unset, str] = UNSET
    aoc_name: Union[Unset, str] = UNSET
    coc: Union[Unset, str] = UNSET
    coc_name: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    de: Union[Unset, str] = UNSET
    de_name: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    max_: Union[Unset, int] = UNSET
    min_: Union[Unset, int] = UNSET
    ou: Union[Unset, str] = UNSET
    ou_name: Union[Unset, str] = UNSET
    ou_path: Union[Unset, str] = UNSET
    pe: Union[Unset, str] = UNSET
    pe_end_date: Union[Unset, datetime.datetime] = UNSET
    pe_name: Union[Unset, str] = UNSET
    pe_start_date: Union[Unset, datetime.datetime] = UNSET
    pe_type: Union[Unset, str] = UNSET
    stored_by: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aoc = self.aoc

        aoc_name = self.aoc_name

        coc = self.coc

        coc_name = self.coc_name

        comment = self.comment

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        de = self.de

        de_name = self.de_name

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        max_ = self.max_

        min_ = self.min_

        ou = self.ou

        ou_name = self.ou_name

        ou_path = self.ou_path

        pe = self.pe

        pe_end_date: Union[Unset, str] = UNSET
        if not isinstance(self.pe_end_date, Unset):
            pe_end_date = self.pe_end_date.isoformat()

        pe_name = self.pe_name

        pe_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.pe_start_date, Unset):
            pe_start_date = self.pe_start_date.isoformat()

        pe_type = self.pe_type

        stored_by = self.stored_by

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aoc is not UNSET:
            field_dict["aoc"] = aoc
        if aoc_name is not UNSET:
            field_dict["aocName"] = aoc_name
        if coc is not UNSET:
            field_dict["coc"] = coc
        if coc_name is not UNSET:
            field_dict["cocName"] = coc_name
        if comment is not UNSET:
            field_dict["comment"] = comment
        if created is not UNSET:
            field_dict["created"] = created
        if de is not UNSET:
            field_dict["de"] = de
        if de_name is not UNSET:
            field_dict["deName"] = de_name
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_
        if ou is not UNSET:
            field_dict["ou"] = ou
        if ou_name is not UNSET:
            field_dict["ouName"] = ou_name
        if ou_path is not UNSET:
            field_dict["ouPath"] = ou_path
        if pe is not UNSET:
            field_dict["pe"] = pe
        if pe_end_date is not UNSET:
            field_dict["peEndDate"] = pe_end_date
        if pe_name is not UNSET:
            field_dict["peName"] = pe_name
        if pe_start_date is not UNSET:
            field_dict["peStartDate"] = pe_start_date
        if pe_type is not UNSET:
            field_dict["peType"] = pe_type
        if stored_by is not UNSET:
            field_dict["storedBy"] = stored_by
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        aoc = d.pop("aoc", UNSET)

        aoc_name = d.pop("aocName", UNSET)

        coc = d.pop("coc", UNSET)

        coc_name = d.pop("cocName", UNSET)

        comment = d.pop("comment", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        de = d.pop("de", UNSET)

        de_name = d.pop("deName", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        max_ = d.pop("max", UNSET)

        min_ = d.pop("min", UNSET)

        ou = d.pop("ou", UNSET)

        ou_name = d.pop("ouName", UNSET)

        ou_path = d.pop("ouPath", UNSET)

        pe = d.pop("pe", UNSET)

        _pe_end_date = d.pop("peEndDate", UNSET)
        pe_end_date: Union[Unset, datetime.datetime]
        if isinstance(_pe_end_date, Unset):
            pe_end_date = UNSET
        else:
            pe_end_date = isoparse(_pe_end_date)

        pe_name = d.pop("peName", UNSET)

        _pe_start_date = d.pop("peStartDate", UNSET)
        pe_start_date: Union[Unset, datetime.datetime]
        if isinstance(_pe_start_date, Unset):
            pe_start_date = UNSET
        else:
            pe_start_date = isoparse(_pe_start_date)

        pe_type = d.pop("peType", UNSET)

        stored_by = d.pop("storedBy", UNSET)

        value = d.pop("value", UNSET)

        followup_value = cls(
            aoc=aoc,
            aoc_name=aoc_name,
            coc=coc,
            coc_name=coc_name,
            comment=comment,
            created=created,
            de=de,
            de_name=de_name,
            last_updated=last_updated,
            max_=max_,
            min_=min_,
            ou=ou,
            ou_name=ou_name,
            ou_path=ou_path,
            pe=pe,
            pe_end_date=pe_end_date,
            pe_name=pe_name,
            pe_start_date=pe_start_date,
            pe_type=pe_type,
            stored_by=stored_by,
            value=value,
        )

        followup_value.additional_properties = d
        return followup_value

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
