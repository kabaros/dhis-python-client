from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_item import DashboardItem
    from ..models.pager import Pager


T = TypeVar("T", bound="DashboardItemGetObjectListResponse200")


@_attrs_define
class DashboardItemGetObjectListResponse200:
    """
    Attributes:
        pager (Union[Unset, Pager]):
        dashboard_items (Union[Unset, list['DashboardItem']]):
    """

    pager: Union[Unset, "Pager"] = UNSET
    dashboard_items: Union[Unset, list["DashboardItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        dashboard_items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.dashboard_items, Unset):
            dashboard_items = []
            for dashboard_items_item_data in self.dashboard_items:
                dashboard_items_item = dashboard_items_item_data.to_dict()
                dashboard_items.append(dashboard_items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if dashboard_items is not UNSET:
            field_dict["dashboardItems"] = dashboard_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.dashboard_item import DashboardItem
        from ..models.pager import Pager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, Pager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = Pager.from_dict(_pager)

        dashboard_items = []
        _dashboard_items = d.pop("dashboardItems", UNSET)
        for dashboard_items_item_data in _dashboard_items or []:
            dashboard_items_item = DashboardItem.from_dict(dashboard_items_item_data)

            dashboard_items.append(dashboard_items_item)

        dashboard_item_get_object_list_response_200 = cls(
            pager=pager,
            dashboard_items=dashboard_items,
        )

        dashboard_item_get_object_list_response_200.additional_properties = d
        return dashboard_item_get_object_list_response_200

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
