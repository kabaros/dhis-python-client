from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category_option_group_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_category_option_groups_item import (
        CategoryOptionGroupGetObjectListGistgetObjectListGistAsCsvResponse200Type0CategoryOptionGroupsItem,
    )
    from ..models.gist_pager import GistPager


T = TypeVar("T", bound="CategoryOptionGroupGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class CategoryOptionGroupGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        category_option_groups (Union[Unset,
            list['CategoryOptionGroupGetObjectListGistgetObjectListGistAsCsvResponse200Type0CategoryOptionGroupsItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    category_option_groups: Union[
        Unset,
        list["CategoryOptionGroupGetObjectListGistgetObjectListGistAsCsvResponse200Type0CategoryOptionGroupsItem"],
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        category_option_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.category_option_groups, Unset):
            category_option_groups = []
            for category_option_groups_item_data in self.category_option_groups:
                category_option_groups_item = category_option_groups_item_data.to_dict()
                category_option_groups.append(category_option_groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if category_option_groups is not UNSET:
            field_dict["categoryOptionGroups"] = category_option_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.category_option_group_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_category_option_groups_item import (
            CategoryOptionGroupGetObjectListGistgetObjectListGistAsCsvResponse200Type0CategoryOptionGroupsItem,
        )
        from ..models.gist_pager import GistPager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        category_option_groups = []
        _category_option_groups = d.pop("categoryOptionGroups", UNSET)
        for category_option_groups_item_data in _category_option_groups or []:
            category_option_groups_item = CategoryOptionGroupGetObjectListGistgetObjectListGistAsCsvResponse200Type0CategoryOptionGroupsItem.from_dict(
                category_option_groups_item_data
            )

            category_option_groups.append(category_option_groups_item)

        category_option_group_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            category_option_groups=category_option_groups,
        )

        category_option_group_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return category_option_group_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
