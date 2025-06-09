from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gist_pager import GistPager
    from ..models.map_view_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_map_views_item import (
        MapViewGetObjectListGistgetObjectListGistAsCsvResponse200Type0MapViewsItem,
    )


T = TypeVar("T", bound="MapViewGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class MapViewGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        map_views (Union[Unset, list['MapViewGetObjectListGistgetObjectListGistAsCsvResponse200Type0MapViewsItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    map_views: Union[Unset, list["MapViewGetObjectListGistgetObjectListGistAsCsvResponse200Type0MapViewsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        map_views: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.map_views, Unset):
            map_views = []
            for map_views_item_data in self.map_views:
                map_views_item = map_views_item_data.to_dict()
                map_views.append(map_views_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if map_views is not UNSET:
            field_dict["mapViews"] = map_views

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.gist_pager import GistPager
        from ..models.map_view_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_map_views_item import (
            MapViewGetObjectListGistgetObjectListGistAsCsvResponse200Type0MapViewsItem,
        )

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        map_views = []
        _map_views = d.pop("mapViews", UNSET)
        for map_views_item_data in _map_views or []:
            map_views_item = MapViewGetObjectListGistgetObjectListGistAsCsvResponse200Type0MapViewsItem.from_dict(
                map_views_item_data
            )

            map_views.append(map_views_item)

        map_view_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            map_views=map_views,
        )

        map_view_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return map_view_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
