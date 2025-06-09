from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportingParams")


@_attrs_define
class ReportingParams:
    """
    Attributes:
        grand_parent_organisation_unit (Union[Unset, bool]):
        organisation_unit (Union[Unset, bool]):
        parent_organisation_unit (Union[Unset, bool]):
        reporting_period (Union[Unset, bool]):
    """

    grand_parent_organisation_unit: Union[Unset, bool] = UNSET
    organisation_unit: Union[Unset, bool] = UNSET
    parent_organisation_unit: Union[Unset, bool] = UNSET
    reporting_period: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grand_parent_organisation_unit = self.grand_parent_organisation_unit

        organisation_unit = self.organisation_unit

        parent_organisation_unit = self.parent_organisation_unit

        reporting_period = self.reporting_period

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if grand_parent_organisation_unit is not UNSET:
            field_dict["grandParentOrganisationUnit"] = grand_parent_organisation_unit
        if organisation_unit is not UNSET:
            field_dict["organisationUnit"] = organisation_unit
        if parent_organisation_unit is not UNSET:
            field_dict["parentOrganisationUnit"] = parent_organisation_unit
        if reporting_period is not UNSET:
            field_dict["reportingPeriod"] = reporting_period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        grand_parent_organisation_unit = d.pop("grandParentOrganisationUnit", UNSET)

        organisation_unit = d.pop("organisationUnit", UNSET)

        parent_organisation_unit = d.pop("parentOrganisationUnit", UNSET)

        reporting_period = d.pop("reportingPeriod", UNSET)

        reporting_params = cls(
            grand_parent_organisation_unit=grand_parent_organisation_unit,
            organisation_unit=organisation_unit,
            parent_organisation_unit=parent_organisation_unit,
            reporting_period=reporting_period,
        )

        reporting_params.additional_properties = d
        return reporting_params

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
