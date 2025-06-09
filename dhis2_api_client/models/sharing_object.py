from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sharing_user import SharingUser
    from ..models.sharing_user_access import SharingUserAccess
    from ..models.sharing_user_group_access import SharingUserGroupAccess


T = TypeVar("T", bound="SharingObject")


@_attrs_define
class SharingObject:
    """
    Attributes:
        external_access (bool):
        display_name (Union[Unset, str]):
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        public_access (Union[Unset, str]):
        user (Union[Unset, SharingUser]):
        user_accesses (Union[Unset, list['SharingUserAccess']]):
        user_group_accesses (Union[Unset, list['SharingUserGroupAccess']]):
    """

    external_access: bool
    display_name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    public_access: Union[Unset, str] = UNSET
    user: Union[Unset, "SharingUser"] = UNSET
    user_accesses: Union[Unset, list["SharingUserAccess"]] = UNSET
    user_group_accesses: Union[Unset, list["SharingUserGroupAccess"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_access = self.external_access

        display_name = self.display_name

        id = self.id

        name = self.name

        public_access = self.public_access

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        user_accesses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.user_accesses, Unset):
            user_accesses = []
            for user_accesses_item_data in self.user_accesses:
                user_accesses_item = user_accesses_item_data.to_dict()
                user_accesses.append(user_accesses_item)

        user_group_accesses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.user_group_accesses, Unset):
            user_group_accesses = []
            for user_group_accesses_item_data in self.user_group_accesses:
                user_group_accesses_item = user_group_accesses_item_data.to_dict()
                user_group_accesses.append(user_group_accesses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "externalAccess": external_access,
            }
        )
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if public_access is not UNSET:
            field_dict["publicAccess"] = public_access
        if user is not UNSET:
            field_dict["user"] = user
        if user_accesses is not UNSET:
            field_dict["userAccesses"] = user_accesses
        if user_group_accesses is not UNSET:
            field_dict["userGroupAccesses"] = user_group_accesses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.sharing_user import SharingUser
        from ..models.sharing_user_access import SharingUserAccess
        from ..models.sharing_user_group_access import SharingUserGroupAccess

        d = src_dict.copy()
        external_access = d.pop("externalAccess")

        display_name = d.pop("displayName", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        public_access = d.pop("publicAccess", UNSET)

        _user = d.pop("user", UNSET)
        user: Union[Unset, SharingUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = SharingUser.from_dict(_user)

        user_accesses = []
        _user_accesses = d.pop("userAccesses", UNSET)
        for user_accesses_item_data in _user_accesses or []:
            user_accesses_item = SharingUserAccess.from_dict(user_accesses_item_data)

            user_accesses.append(user_accesses_item)

        user_group_accesses = []
        _user_group_accesses = d.pop("userGroupAccesses", UNSET)
        for user_group_accesses_item_data in _user_group_accesses or []:
            user_group_accesses_item = SharingUserGroupAccess.from_dict(user_group_accesses_item_data)

            user_group_accesses.append(user_group_accesses_item)

        sharing_object = cls(
            external_access=external_access,
            display_name=display_name,
            id=id,
            name=name,
            public_access=public_access,
            user=user,
            user_accesses=user_accesses,
            user_group_accesses=user_group_accesses,
        )

        sharing_object.additional_properties = d
        return sharing_object

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
