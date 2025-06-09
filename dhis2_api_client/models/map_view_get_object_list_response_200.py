from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_view import MapView
    from ..models.pager import Pager


T = TypeVar("T", bound="MapViewGetObjectListResponse200")


@_attrs_define
class MapViewGetObjectListResponse200:
    """
    Attributes:
        pager (Union[Unset, Pager]):
        map_views (Union[Unset, list['MapView']]):
    """

    pager: Union[Unset, "Pager"] = UNSET
    map_views: Union[Unset, list["MapView"]] = UNSET
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
        from ..models.map_view import MapView
        from ..models.pager import Pager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, Pager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = Pager.from_dict(_pager)

        map_views = []
        _map_views = d.pop("mapViews", UNSET)
        for map_views_item_data in _map_views or []:
            map_views_item = MapView.from_dict(map_views_item_data)

            map_views.append(map_views_item)

        map_view_get_object_list_response_200 = cls(
            pager=pager,
            map_views=map_views,
        )

        map_view_get_object_list_response_200.additional_properties = d
        return map_view_get_object_list_response_200

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
