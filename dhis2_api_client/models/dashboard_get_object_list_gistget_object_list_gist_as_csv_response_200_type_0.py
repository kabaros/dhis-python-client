from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_dashboards_item import (
        DashboardGetObjectListGistgetObjectListGistAsCsvResponse200Type0DashboardsItem,
    )
    from ..models.gist_pager import GistPager


T = TypeVar("T", bound="DashboardGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class DashboardGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        dashboards (Union[Unset,
            list['DashboardGetObjectListGistgetObjectListGistAsCsvResponse200Type0DashboardsItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    dashboards: Union[Unset, list["DashboardGetObjectListGistgetObjectListGistAsCsvResponse200Type0DashboardsItem"]] = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        dashboards: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.dashboards, Unset):
            dashboards = []
            for dashboards_item_data in self.dashboards:
                dashboards_item = dashboards_item_data.to_dict()
                dashboards.append(dashboards_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if dashboards is not UNSET:
            field_dict["dashboards"] = dashboards

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.dashboard_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_dashboards_item import (
            DashboardGetObjectListGistgetObjectListGistAsCsvResponse200Type0DashboardsItem,
        )
        from ..models.gist_pager import GistPager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        dashboards = []
        _dashboards = d.pop("dashboards", UNSET)
        for dashboards_item_data in _dashboards or []:
            dashboards_item = DashboardGetObjectListGistgetObjectListGistAsCsvResponse200Type0DashboardsItem.from_dict(
                dashboards_item_data
            )

            dashboards.append(dashboards_item)

        dashboard_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            dashboards=dashboards,
        )

        dashboard_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return dashboard_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
