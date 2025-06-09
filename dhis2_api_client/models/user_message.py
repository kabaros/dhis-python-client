from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_message_user import UserMessageUser


T = TypeVar("T", bound="UserMessage")


@_attrs_define
class UserMessage:
    """
    Attributes:
        follow_up (Union[Unset, bool]):
        key (Union[Unset, str]):
        read (Union[Unset, bool]):
        user (Union[Unset, UserMessageUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    follow_up: Union[Unset, bool] = UNSET
    key: Union[Unset, str] = UNSET
    read: Union[Unset, bool] = UNSET
    user: Union[Unset, "UserMessageUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        follow_up = self.follow_up

        key = self.key

        read = self.read

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if follow_up is not UNSET:
            field_dict["followUp"] = follow_up
        if key is not UNSET:
            field_dict["key"] = key
        if read is not UNSET:
            field_dict["read"] = read
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.user_message_user import UserMessageUser

        d = src_dict.copy()
        follow_up = d.pop("followUp", UNSET)

        key = d.pop("key", UNSET)

        read = d.pop("read", UNSET)

        _user = d.pop("user", UNSET)
        user: Union[Unset, UserMessageUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserMessageUser.from_dict(_user)

        user_message = cls(
            follow_up=follow_up,
            key=key,
            read=read,
            user=user,
        )

        user_message.additional_properties = d
        return user_message

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
