from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analytics_table_hook_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_analytics_table_hooks_item import (
        AnalyticsTableHookGetObjectListGistgetObjectListGistAsCsvResponse200Type0AnalyticsTableHooksItem,
    )
    from ..models.gist_pager import GistPager


T = TypeVar("T", bound="AnalyticsTableHookGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class AnalyticsTableHookGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        analytics_table_hooks (Union[Unset,
            list['AnalyticsTableHookGetObjectListGistgetObjectListGistAsCsvResponse200Type0AnalyticsTableHooksItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    analytics_table_hooks: Union[
        Unset, list["AnalyticsTableHookGetObjectListGistgetObjectListGistAsCsvResponse200Type0AnalyticsTableHooksItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        analytics_table_hooks: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.analytics_table_hooks, Unset):
            analytics_table_hooks = []
            for analytics_table_hooks_item_data in self.analytics_table_hooks:
                analytics_table_hooks_item = analytics_table_hooks_item_data.to_dict()
                analytics_table_hooks.append(analytics_table_hooks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if analytics_table_hooks is not UNSET:
            field_dict["analyticsTableHooks"] = analytics_table_hooks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.analytics_table_hook_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_analytics_table_hooks_item import (
            AnalyticsTableHookGetObjectListGistgetObjectListGistAsCsvResponse200Type0AnalyticsTableHooksItem,
        )
        from ..models.gist_pager import GistPager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        analytics_table_hooks = []
        _analytics_table_hooks = d.pop("analyticsTableHooks", UNSET)
        for analytics_table_hooks_item_data in _analytics_table_hooks or []:
            analytics_table_hooks_item = AnalyticsTableHookGetObjectListGistgetObjectListGistAsCsvResponse200Type0AnalyticsTableHooksItem.from_dict(
                analytics_table_hooks_item_data
            )

            analytics_table_hooks.append(analytics_table_hooks_item)

        analytics_table_hook_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            analytics_table_hooks=analytics_table_hooks,
        )

        analytics_table_hook_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return analytics_table_hook_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
