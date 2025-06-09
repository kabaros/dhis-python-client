from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MinMaxValueDto")


@_attrs_define
class MinMaxValueDto:
    """
    Attributes:
        category_option_combo (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        data_element (Union[Unset, str]): A UID for an DataElement object
            (Java name `org.hisp.dhis.dataelement.DataElement`) Example: hX7n8Y4pu89.
        max_value (Union[Unset, int]):
        min_value (Union[Unset, int]):
        org_unit (Union[Unset, str]): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
    """

    category_option_combo: Union[Unset, str] = UNSET
    data_element: Union[Unset, str] = UNSET
    max_value: Union[Unset, int] = UNSET
    min_value: Union[Unset, int] = UNSET
    org_unit: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category_option_combo = self.category_option_combo

        data_element = self.data_element

        max_value = self.max_value

        min_value = self.min_value

        org_unit = self.org_unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category_option_combo is not UNSET:
            field_dict["categoryOptionCombo"] = category_option_combo
        if data_element is not UNSET:
            field_dict["dataElement"] = data_element
        if max_value is not UNSET:
            field_dict["maxValue"] = max_value
        if min_value is not UNSET:
            field_dict["minValue"] = min_value
        if org_unit is not UNSET:
            field_dict["orgUnit"] = org_unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        category_option_combo = d.pop("categoryOptionCombo", UNSET)

        data_element = d.pop("dataElement", UNSET)

        max_value = d.pop("maxValue", UNSET)

        min_value = d.pop("minValue", UNSET)

        org_unit = d.pop("orgUnit", UNSET)

        min_max_value_dto = cls(
            category_option_combo=category_option_combo,
            data_element=data_element,
            max_value=max_value,
            min_value=min_value,
            org_unit=org_unit,
        )

        min_max_value_dto.additional_properties = d
        return min_max_value_dto

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
