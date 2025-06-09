from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gist_pager import GistPager
    from ..models.sql_view_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_sql_views_item import (
        SqlViewGetObjectListGistgetObjectListGistAsCsvResponse200Type0SqlViewsItem,
    )


T = TypeVar("T", bound="SqlViewGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class SqlViewGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        sql_views (Union[Unset, list['SqlViewGetObjectListGistgetObjectListGistAsCsvResponse200Type0SqlViewsItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    sql_views: Union[Unset, list["SqlViewGetObjectListGistgetObjectListGistAsCsvResponse200Type0SqlViewsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        sql_views: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sql_views, Unset):
            sql_views = []
            for sql_views_item_data in self.sql_views:
                sql_views_item = sql_views_item_data.to_dict()
                sql_views.append(sql_views_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if sql_views is not UNSET:
            field_dict["sqlViews"] = sql_views

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.gist_pager import GistPager
        from ..models.sql_view_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_sql_views_item import (
            SqlViewGetObjectListGistgetObjectListGistAsCsvResponse200Type0SqlViewsItem,
        )

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        sql_views = []
        _sql_views = d.pop("sqlViews", UNSET)
        for sql_views_item_data in _sql_views or []:
            sql_views_item = SqlViewGetObjectListGistgetObjectListGistAsCsvResponse200Type0SqlViewsItem.from_dict(
                sql_views_item_data
            )

            sql_views.append(sql_views_item)

        sql_view_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            sql_views=sql_views,
        )

        sql_view_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return sql_view_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
