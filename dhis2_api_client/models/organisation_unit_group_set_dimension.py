from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organisation_unit_group_set_dimension_organisation_unit_group_set import (
        OrganisationUnitGroupSetDimensionOrganisationUnitGroupSet,
    )
    from ..models.organisation_unit_group_set_dimension_organisation_unit_groups_item import (
        OrganisationUnitGroupSetDimensionOrganisationUnitGroupsItem,
    )


T = TypeVar("T", bound="OrganisationUnitGroupSetDimension")


@_attrs_define
class OrganisationUnitGroupSetDimension:
    """
    Attributes:
        organisation_unit_group_set (Union[Unset, OrganisationUnitGroupSetDimensionOrganisationUnitGroupSet]): A UID
            reference to a OrganisationUnitGroupSet
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnitGroupSet`)
        organisation_unit_groups (Union[Unset, list['OrganisationUnitGroupSetDimensionOrganisationUnitGroupsItem']]):
    """

    organisation_unit_group_set: Union[Unset, "OrganisationUnitGroupSetDimensionOrganisationUnitGroupSet"] = UNSET
    organisation_unit_groups: Union[Unset, list["OrganisationUnitGroupSetDimensionOrganisationUnitGroupsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organisation_unit_group_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organisation_unit_group_set, Unset):
            organisation_unit_group_set = self.organisation_unit_group_set.to_dict()

        organisation_unit_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.organisation_unit_groups, Unset):
            organisation_unit_groups = []
            for organisation_unit_groups_item_data in self.organisation_unit_groups:
                organisation_unit_groups_item = organisation_unit_groups_item_data.to_dict()
                organisation_unit_groups.append(organisation_unit_groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organisation_unit_group_set is not UNSET:
            field_dict["organisationUnitGroupSet"] = organisation_unit_group_set
        if organisation_unit_groups is not UNSET:
            field_dict["organisationUnitGroups"] = organisation_unit_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.organisation_unit_group_set_dimension_organisation_unit_group_set import (
            OrganisationUnitGroupSetDimensionOrganisationUnitGroupSet,
        )
        from ..models.organisation_unit_group_set_dimension_organisation_unit_groups_item import (
            OrganisationUnitGroupSetDimensionOrganisationUnitGroupsItem,
        )

        d = src_dict.copy()
        _organisation_unit_group_set = d.pop("organisationUnitGroupSet", UNSET)
        organisation_unit_group_set: Union[Unset, OrganisationUnitGroupSetDimensionOrganisationUnitGroupSet]
        if isinstance(_organisation_unit_group_set, Unset):
            organisation_unit_group_set = UNSET
        else:
            organisation_unit_group_set = OrganisationUnitGroupSetDimensionOrganisationUnitGroupSet.from_dict(
                _organisation_unit_group_set
            )

        organisation_unit_groups = []
        _organisation_unit_groups = d.pop("organisationUnitGroups", UNSET)
        for organisation_unit_groups_item_data in _organisation_unit_groups or []:
            organisation_unit_groups_item = OrganisationUnitGroupSetDimensionOrganisationUnitGroupsItem.from_dict(
                organisation_unit_groups_item_data
            )

            organisation_unit_groups.append(organisation_unit_groups_item)

        organisation_unit_group_set_dimension = cls(
            organisation_unit_group_set=organisation_unit_group_set,
            organisation_unit_groups=organisation_unit_groups,
        )

        organisation_unit_group_set_dimension.additional_properties = d
        return organisation_unit_group_set_dimension

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
