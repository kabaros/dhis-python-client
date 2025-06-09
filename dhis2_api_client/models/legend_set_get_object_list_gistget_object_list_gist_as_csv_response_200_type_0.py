from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gist_pager import GistPager
    from ..models.legend_set_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_legend_sets_item import (
        LegendSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0LegendSetsItem,
    )


T = TypeVar("T", bound="LegendSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class LegendSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        legend_sets (Union[Unset,
            list['LegendSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0LegendSetsItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    legend_sets: Union[
        Unset, list["LegendSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0LegendSetsItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        legend_sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.legend_sets, Unset):
            legend_sets = []
            for legend_sets_item_data in self.legend_sets:
                legend_sets_item = legend_sets_item_data.to_dict()
                legend_sets.append(legend_sets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if legend_sets is not UNSET:
            field_dict["legendSets"] = legend_sets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.gist_pager import GistPager
        from ..models.legend_set_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_legend_sets_item import (
            LegendSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0LegendSetsItem,
        )

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        legend_sets = []
        _legend_sets = d.pop("legendSets", UNSET)
        for legend_sets_item_data in _legend_sets or []:
            legend_sets_item = LegendSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0LegendSetsItem.from_dict(
                legend_sets_item_data
            )

            legend_sets.append(legend_sets_item)

        legend_set_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            legend_sets=legend_sets,
        )

        legend_set_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return legend_set_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
