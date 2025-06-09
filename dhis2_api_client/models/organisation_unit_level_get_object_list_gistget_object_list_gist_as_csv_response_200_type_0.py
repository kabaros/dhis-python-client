from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gist_pager import GistPager
    from ..models.organisation_unit_level_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_organisation_unit_levels_item import (
        OrganisationUnitLevelGetObjectListGistgetObjectListGistAsCsvResponse200Type0OrganisationUnitLevelsItem,
    )


T = TypeVar("T", bound="OrganisationUnitLevelGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class OrganisationUnitLevelGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        organisation_unit_levels (Union[Unset, list['OrganisationUnitLevelGetObjectListGistgetObjectListGistAsCsvRespons
            e200Type0OrganisationUnitLevelsItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    organisation_unit_levels: Union[
        Unset,
        list["OrganisationUnitLevelGetObjectListGistgetObjectListGistAsCsvResponse200Type0OrganisationUnitLevelsItem"],
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        organisation_unit_levels: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.organisation_unit_levels, Unset):
            organisation_unit_levels = []
            for organisation_unit_levels_item_data in self.organisation_unit_levels:
                organisation_unit_levels_item = organisation_unit_levels_item_data.to_dict()
                organisation_unit_levels.append(organisation_unit_levels_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if organisation_unit_levels is not UNSET:
            field_dict["organisationUnitLevels"] = organisation_unit_levels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.gist_pager import GistPager
        from ..models.organisation_unit_level_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_organisation_unit_levels_item import (
            OrganisationUnitLevelGetObjectListGistgetObjectListGistAsCsvResponse200Type0OrganisationUnitLevelsItem,
        )

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        organisation_unit_levels = []
        _organisation_unit_levels = d.pop("organisationUnitLevels", UNSET)
        for organisation_unit_levels_item_data in _organisation_unit_levels or []:
            organisation_unit_levels_item = OrganisationUnitLevelGetObjectListGistgetObjectListGistAsCsvResponse200Type0OrganisationUnitLevelsItem.from_dict(
                organisation_unit_levels_item_data
            )

            organisation_unit_levels.append(organisation_unit_levels_item)

        organisation_unit_level_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            organisation_unit_levels=organisation_unit_levels,
        )

        organisation_unit_level_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return organisation_unit_level_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
