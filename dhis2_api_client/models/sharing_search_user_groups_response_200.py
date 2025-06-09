from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sharing_search_user_groups_response_200_additional_property import (
        SharingSearchUserGroupsResponse200AdditionalProperty,
    )


T = TypeVar("T", bound="SharingSearchUserGroupsResponse200")


@_attrs_define
class SharingSearchUserGroupsResponse200:
    """ """

    additional_properties: dict[str, "SharingSearchUserGroupsResponse200AdditionalProperty"] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.sharing_search_user_groups_response_200_additional_property import (
            SharingSearchUserGroupsResponse200AdditionalProperty,
        )

        d = src_dict.copy()
        sharing_search_user_groups_response_200 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = SharingSearchUserGroupsResponse200AdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        sharing_search_user_groups_response_200.additional_properties = additional_properties
        return sharing_search_user_groups_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "SharingSearchUserGroupsResponse200AdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "SharingSearchUserGroupsResponse200AdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
