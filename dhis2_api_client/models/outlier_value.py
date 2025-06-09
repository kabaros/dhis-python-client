import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutlierValue")


@_attrs_define
class OutlierValue:
    """
    Attributes:
        abs_dev (Union[Unset, float]):
        aoc (Union[Unset, str]):
        aoc_name (Union[Unset, str]):
        coc (Union[Unset, str]):
        coc_name (Union[Unset, str]):
        de (Union[Unset, str]):
        de_name (Union[Unset, str]):
        followup (Union[Unset, bool]):
        last_updated (Union[Unset, datetime.datetime]):
        lower_bound (Union[Unset, float]):
        mean (Union[Unset, float]):
        median (Union[Unset, float]):
        ou (Union[Unset, str]):
        ou_name (Union[Unset, str]):
        pe (Union[Unset, str]):
        std_dev (Union[Unset, float]):
        upper_bound (Union[Unset, float]):
        value (Union[Unset, float]):
        z_score (Union[Unset, float]):
    """

    abs_dev: Union[Unset, float] = UNSET
    aoc: Union[Unset, str] = UNSET
    aoc_name: Union[Unset, str] = UNSET
    coc: Union[Unset, str] = UNSET
    coc_name: Union[Unset, str] = UNSET
    de: Union[Unset, str] = UNSET
    de_name: Union[Unset, str] = UNSET
    followup: Union[Unset, bool] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    lower_bound: Union[Unset, float] = UNSET
    mean: Union[Unset, float] = UNSET
    median: Union[Unset, float] = UNSET
    ou: Union[Unset, str] = UNSET
    ou_name: Union[Unset, str] = UNSET
    pe: Union[Unset, str] = UNSET
    std_dev: Union[Unset, float] = UNSET
    upper_bound: Union[Unset, float] = UNSET
    value: Union[Unset, float] = UNSET
    z_score: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        abs_dev = self.abs_dev

        aoc = self.aoc

        aoc_name = self.aoc_name

        coc = self.coc

        coc_name = self.coc_name

        de = self.de

        de_name = self.de_name

        followup = self.followup

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        lower_bound = self.lower_bound

        mean = self.mean

        median = self.median

        ou = self.ou

        ou_name = self.ou_name

        pe = self.pe

        std_dev = self.std_dev

        upper_bound = self.upper_bound

        value = self.value

        z_score = self.z_score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if abs_dev is not UNSET:
            field_dict["absDev"] = abs_dev
        if aoc is not UNSET:
            field_dict["aoc"] = aoc
        if aoc_name is not UNSET:
            field_dict["aocName"] = aoc_name
        if coc is not UNSET:
            field_dict["coc"] = coc
        if coc_name is not UNSET:
            field_dict["cocName"] = coc_name
        if de is not UNSET:
            field_dict["de"] = de
        if de_name is not UNSET:
            field_dict["deName"] = de_name
        if followup is not UNSET:
            field_dict["followup"] = followup
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if lower_bound is not UNSET:
            field_dict["lowerBound"] = lower_bound
        if mean is not UNSET:
            field_dict["mean"] = mean
        if median is not UNSET:
            field_dict["median"] = median
        if ou is not UNSET:
            field_dict["ou"] = ou
        if ou_name is not UNSET:
            field_dict["ouName"] = ou_name
        if pe is not UNSET:
            field_dict["pe"] = pe
        if std_dev is not UNSET:
            field_dict["stdDev"] = std_dev
        if upper_bound is not UNSET:
            field_dict["upperBound"] = upper_bound
        if value is not UNSET:
            field_dict["value"] = value
        if z_score is not UNSET:
            field_dict["zScore"] = z_score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        abs_dev = d.pop("absDev", UNSET)

        aoc = d.pop("aoc", UNSET)

        aoc_name = d.pop("aocName", UNSET)

        coc = d.pop("coc", UNSET)

        coc_name = d.pop("cocName", UNSET)

        de = d.pop("de", UNSET)

        de_name = d.pop("deName", UNSET)

        followup = d.pop("followup", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        lower_bound = d.pop("lowerBound", UNSET)

        mean = d.pop("mean", UNSET)

        median = d.pop("median", UNSET)

        ou = d.pop("ou", UNSET)

        ou_name = d.pop("ouName", UNSET)

        pe = d.pop("pe", UNSET)

        std_dev = d.pop("stdDev", UNSET)

        upper_bound = d.pop("upperBound", UNSET)

        value = d.pop("value", UNSET)

        z_score = d.pop("zScore", UNSET)

        outlier_value = cls(
            abs_dev=abs_dev,
            aoc=aoc,
            aoc_name=aoc_name,
            coc=coc,
            coc_name=coc_name,
            de=de,
            de_name=de_name,
            followup=followup,
            last_updated=last_updated,
            lower_bound=lower_bound,
            mean=mean,
            median=median,
            ou=ou,
            ou_name=ou_name,
            pe=pe,
            std_dev=std_dev,
            upper_bound=upper_bound,
            value=value,
            z_score=z_score,
        )

        outlier_value.additional_properties = d
        return outlier_value

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
