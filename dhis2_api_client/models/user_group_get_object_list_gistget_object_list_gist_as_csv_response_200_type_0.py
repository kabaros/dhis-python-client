from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gist_pager import GistPager
    from ..models.user_group_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_user_groups_item import (
        UserGroupGetObjectListGistgetObjectListGistAsCsvResponse200Type0UserGroupsItem,
    )


T = TypeVar("T", bound="UserGroupGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class UserGroupGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        user_groups (Union[Unset,
            list['UserGroupGetObjectListGistgetObjectListGistAsCsvResponse200Type0UserGroupsItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    user_groups: Union[
        Unset, list["UserGroupGetObjectListGistgetObjectListGistAsCsvResponse200Type0UserGroupsItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        user_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.user_groups, Unset):
            user_groups = []
            for user_groups_item_data in self.user_groups:
                user_groups_item = user_groups_item_data.to_dict()
                user_groups.append(user_groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if user_groups is not UNSET:
            field_dict["userGroups"] = user_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.gist_pager import GistPager
        from ..models.user_group_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_user_groups_item import (
            UserGroupGetObjectListGistgetObjectListGistAsCsvResponse200Type0UserGroupsItem,
        )

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        user_groups = []
        _user_groups = d.pop("userGroups", UNSET)
        for user_groups_item_data in _user_groups or []:
            user_groups_item = UserGroupGetObjectListGistgetObjectListGistAsCsvResponse200Type0UserGroupsItem.from_dict(
                user_groups_item_data
            )

            user_groups.append(user_groups_item)

        user_group_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            user_groups=user_groups,
        )

        user_group_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return user_group_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
