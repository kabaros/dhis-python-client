from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organisation_unit import OrganisationUnit
    from ..models.pager import Pager


T = TypeVar("T", bound="OrganisationUnitGetUserDataViewOrganisationUnitsResponse200")


@_attrs_define
class OrganisationUnitGetUserDataViewOrganisationUnitsResponse200:
    """
    Attributes:
        pager (Union[Unset, Pager]):
        organisation_units (Union[Unset, list['OrganisationUnit']]):
    """

    pager: Union[Unset, "Pager"] = UNSET
    organisation_units: Union[Unset, list["OrganisationUnit"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        organisation_units: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.organisation_units, Unset):
            organisation_units = []
            for organisation_units_item_data in self.organisation_units:
                organisation_units_item = organisation_units_item_data.to_dict()
                organisation_units.append(organisation_units_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if organisation_units is not UNSET:
            field_dict["organisationUnits"] = organisation_units

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.organisation_unit import OrganisationUnit
        from ..models.pager import Pager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, Pager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = Pager.from_dict(_pager)

        organisation_units = []
        _organisation_units = d.pop("organisationUnits", UNSET)
        for organisation_units_item_data in _organisation_units or []:
            organisation_units_item = OrganisationUnit.from_dict(organisation_units_item_data)

            organisation_units.append(organisation_units_item)

        organisation_unit_get_user_data_view_organisation_units_response_200 = cls(
            pager=pager,
            organisation_units=organisation_units,
        )

        organisation_unit_get_user_data_view_organisation_units_response_200.additional_properties = d
        return organisation_unit_get_user_data_view_organisation_units_response_200

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
