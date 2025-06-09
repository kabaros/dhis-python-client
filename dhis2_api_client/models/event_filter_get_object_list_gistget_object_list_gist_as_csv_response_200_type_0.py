from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_filter_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_event_filters_item import (
        EventFilterGetObjectListGistgetObjectListGistAsCsvResponse200Type0EventFiltersItem,
    )
    from ..models.gist_pager import GistPager


T = TypeVar("T", bound="EventFilterGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class EventFilterGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        event_filters (Union[Unset,
            list['EventFilterGetObjectListGistgetObjectListGistAsCsvResponse200Type0EventFiltersItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    event_filters: Union[
        Unset, list["EventFilterGetObjectListGistgetObjectListGistAsCsvResponse200Type0EventFiltersItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        event_filters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.event_filters, Unset):
            event_filters = []
            for event_filters_item_data in self.event_filters:
                event_filters_item = event_filters_item_data.to_dict()
                event_filters.append(event_filters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if event_filters is not UNSET:
            field_dict["eventFilters"] = event_filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.event_filter_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_event_filters_item import (
            EventFilterGetObjectListGistgetObjectListGistAsCsvResponse200Type0EventFiltersItem,
        )
        from ..models.gist_pager import GistPager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        event_filters = []
        _event_filters = d.pop("eventFilters", UNSET)
        for event_filters_item_data in _event_filters or []:
            event_filters_item = (
                EventFilterGetObjectListGistgetObjectListGistAsCsvResponse200Type0EventFiltersItem.from_dict(
                    event_filters_item_data
                )
            )

            event_filters.append(event_filters_item)

        event_filter_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            event_filters=event_filters,
        )

        event_filter_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return event_filter_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
