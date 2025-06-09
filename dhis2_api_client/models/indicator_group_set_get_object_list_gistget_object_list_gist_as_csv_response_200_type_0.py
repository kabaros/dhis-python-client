from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gist_pager import GistPager
    from ..models.indicator_group_set_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_indicator_group_sets_item import (
        IndicatorGroupSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0IndicatorGroupSetsItem,
    )


T = TypeVar("T", bound="IndicatorGroupSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class IndicatorGroupSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        indicator_group_sets (Union[Unset,
            list['IndicatorGroupSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0IndicatorGroupSetsItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    indicator_group_sets: Union[
        Unset, list["IndicatorGroupSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0IndicatorGroupSetsItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        indicator_group_sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.indicator_group_sets, Unset):
            indicator_group_sets = []
            for indicator_group_sets_item_data in self.indicator_group_sets:
                indicator_group_sets_item = indicator_group_sets_item_data.to_dict()
                indicator_group_sets.append(indicator_group_sets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if indicator_group_sets is not UNSET:
            field_dict["indicatorGroupSets"] = indicator_group_sets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.gist_pager import GistPager
        from ..models.indicator_group_set_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_indicator_group_sets_item import (
            IndicatorGroupSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0IndicatorGroupSetsItem,
        )

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        indicator_group_sets = []
        _indicator_group_sets = d.pop("indicatorGroupSets", UNSET)
        for indicator_group_sets_item_data in _indicator_group_sets or []:
            indicator_group_sets_item = IndicatorGroupSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0IndicatorGroupSetsItem.from_dict(
                indicator_group_sets_item_data
            )

            indicator_group_sets.append(indicator_group_sets_item)

        indicator_group_set_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            indicator_group_sets=indicator_group_sets,
        )

        indicator_group_set_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return indicator_group_set_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
