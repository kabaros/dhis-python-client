from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidationRulesAnalysisParams")


@_attrs_define
class ValidationRulesAnalysisParams:
    """
    Attributes:
        end_date (Union[Unset, str]):
        notification (Union[Unset, bool]):
        ou (Union[Unset, str]):
        persist (Union[Unset, bool]):
        start_date (Union[Unset, str]):
        vrg (Union[Unset, str]):
    """

    end_date: Union[Unset, str] = UNSET
    notification: Union[Unset, bool] = UNSET
    ou: Union[Unset, str] = UNSET
    persist: Union[Unset, bool] = UNSET
    start_date: Union[Unset, str] = UNSET
    vrg: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_date = self.end_date

        notification = self.notification

        ou = self.ou

        persist = self.persist

        start_date = self.start_date

        vrg = self.vrg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if notification is not UNSET:
            field_dict["notification"] = notification
        if ou is not UNSET:
            field_dict["ou"] = ou
        if persist is not UNSET:
            field_dict["persist"] = persist
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if vrg is not UNSET:
            field_dict["vrg"] = vrg

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        end_date = d.pop("endDate", UNSET)

        notification = d.pop("notification", UNSET)

        ou = d.pop("ou", UNSET)

        persist = d.pop("persist", UNSET)

        start_date = d.pop("startDate", UNSET)

        vrg = d.pop("vrg", UNSET)

        validation_rules_analysis_params = cls(
            end_date=end_date,
            notification=notification,
            ou=ou,
            persist=persist,
            start_date=start_date,
            vrg=vrg,
        )

        validation_rules_analysis_params.additional_properties = d
        return validation_rules_analysis_params

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
