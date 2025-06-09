import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FollowupAnalysisMetadata")


@_attrs_define
class FollowupAnalysisMetadata:
    """
    Attributes:
        max_results (int):
        coc (Union[Unset, list[str]]):
        de (Union[Unset, list[str]]):
        end_date (Union[Unset, datetime.datetime]):
        ou (Union[Unset, list[str]]):
        start_date (Union[Unset, datetime.datetime]):
    """

    max_results: int
    coc: Union[Unset, list[str]] = UNSET
    de: Union[Unset, list[str]] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    ou: Union[Unset, list[str]] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_results = self.max_results

        coc: Union[Unset, list[str]] = UNSET
        if not isinstance(self.coc, Unset):
            coc = self.coc

        de: Union[Unset, list[str]] = UNSET
        if not isinstance(self.de, Unset):
            de = self.de

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        ou: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ou, Unset):
            ou = self.ou

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "maxResults": max_results,
            }
        )
        if coc is not UNSET:
            field_dict["coc"] = coc
        if de is not UNSET:
            field_dict["de"] = de
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if ou is not UNSET:
            field_dict["ou"] = ou
        if start_date is not UNSET:
            field_dict["startDate"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        max_results = d.pop("maxResults")

        coc = cast(list[str], d.pop("coc", UNSET))

        de = cast(list[str], d.pop("de", UNSET))

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        ou = cast(list[str], d.pop("ou", UNSET))

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        followup_analysis_metadata = cls(
            max_results=max_results,
            coc=coc,
            de=de,
            end_date=end_date,
            ou=ou,
            start_date=start_date,
        )

        followup_analysis_metadata.additional_properties = d
        return followup_analysis_metadata

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
