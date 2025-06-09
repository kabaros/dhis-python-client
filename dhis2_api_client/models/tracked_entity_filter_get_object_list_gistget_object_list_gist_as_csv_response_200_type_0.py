from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gist_pager import GistPager
    from ..models.tracked_entity_filter_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_tracked_entity_instance_filters_item import (
        TrackedEntityFilterGetObjectListGistgetObjectListGistAsCsvResponse200Type0TrackedEntityInstanceFiltersItem,
    )


T = TypeVar("T", bound="TrackedEntityFilterGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class TrackedEntityFilterGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        tracked_entity_instance_filters (Union[Unset, list['TrackedEntityFilterGetObjectListGistgetObjectListGistAsCsvRe
            sponse200Type0TrackedEntityInstanceFiltersItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    tracked_entity_instance_filters: Union[
        Unset,
        list[
            "TrackedEntityFilterGetObjectListGistgetObjectListGistAsCsvResponse200Type0TrackedEntityInstanceFiltersItem"
        ],
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        tracked_entity_instance_filters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tracked_entity_instance_filters, Unset):
            tracked_entity_instance_filters = []
            for tracked_entity_instance_filters_item_data in self.tracked_entity_instance_filters:
                tracked_entity_instance_filters_item = tracked_entity_instance_filters_item_data.to_dict()
                tracked_entity_instance_filters.append(tracked_entity_instance_filters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if tracked_entity_instance_filters is not UNSET:
            field_dict["trackedEntityInstanceFilters"] = tracked_entity_instance_filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.gist_pager import GistPager
        from ..models.tracked_entity_filter_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_tracked_entity_instance_filters_item import (
            TrackedEntityFilterGetObjectListGistgetObjectListGistAsCsvResponse200Type0TrackedEntityInstanceFiltersItem,
        )

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        tracked_entity_instance_filters = []
        _tracked_entity_instance_filters = d.pop("trackedEntityInstanceFilters", UNSET)
        for tracked_entity_instance_filters_item_data in _tracked_entity_instance_filters or []:
            tracked_entity_instance_filters_item = TrackedEntityFilterGetObjectListGistgetObjectListGistAsCsvResponse200Type0TrackedEntityInstanceFiltersItem.from_dict(
                tracked_entity_instance_filters_item_data
            )

            tracked_entity_instance_filters.append(tracked_entity_instance_filters_item)

        tracked_entity_filter_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            tracked_entity_instance_filters=tracked_entity_instance_filters,
        )

        tracked_entity_filter_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return tracked_entity_filter_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
