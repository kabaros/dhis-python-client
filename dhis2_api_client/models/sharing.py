from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sharing_user_groups import SharingUserGroups
    from ..models.sharing_users import SharingUsers


T = TypeVar("T", bound="Sharing")


@_attrs_define
class Sharing:
    """
    Attributes:
        external (Union[Unset, bool]):
        owner (Union[Unset, str]):
        public (Union[Unset, str]):
        user_groups (Union[Unset, SharingUserGroups]):
        users (Union[Unset, SharingUsers]):
    """

    external: Union[Unset, bool] = UNSET
    owner: Union[Unset, str] = UNSET
    public: Union[Unset, str] = UNSET
    user_groups: Union[Unset, "SharingUserGroups"] = UNSET
    users: Union[Unset, "SharingUsers"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external = self.external

        owner = self.owner

        public = self.public

        user_groups: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user_groups, Unset):
            user_groups = self.user_groups.to_dict()

        users: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.users, Unset):
            users = self.users.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external is not UNSET:
            field_dict["external"] = external
        if owner is not UNSET:
            field_dict["owner"] = owner
        if public is not UNSET:
            field_dict["public"] = public
        if user_groups is not UNSET:
            field_dict["userGroups"] = user_groups
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.sharing_user_groups import SharingUserGroups
        from ..models.sharing_users import SharingUsers

        d = src_dict.copy()
        external = d.pop("external", UNSET)

        owner = d.pop("owner", UNSET)

        public = d.pop("public", UNSET)

        _user_groups = d.pop("userGroups", UNSET)
        user_groups: Union[Unset, SharingUserGroups]
        if isinstance(_user_groups, Unset):
            user_groups = UNSET
        else:
            user_groups = SharingUserGroups.from_dict(_user_groups)

        _users = d.pop("users", UNSET)
        users: Union[Unset, SharingUsers]
        if isinstance(_users, Unset):
            users = UNSET
        else:
            users = SharingUsers.from_dict(_users)

        sharing = cls(
            external=external,
            owner=owner,
            public=public,
            user_groups=user_groups,
            users=users,
        )

        sharing.additional_properties = d
        return sharing

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
