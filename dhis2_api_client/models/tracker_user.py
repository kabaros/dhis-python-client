from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrackerUser")


@_attrs_define
class TrackerUser:
    """
    Attributes:
        display_name (Union[Unset, str]):
        first_name (Union[Unset, str]):
        surname (Union[Unset, str]):
        uid (Union[Unset, str]): A UID for an TrackerUser object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.User`) Example: r87xh9Xn8ON.
        username (Union[Unset, str]):
    """

    display_name: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    surname: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        first_name = self.first_name

        surname = self.surname

        uid = self.uid

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if surname is not UNSET:
            field_dict["surname"] = surname
        if uid is not UNSET:
            field_dict["uid"] = uid
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("displayName", UNSET)

        first_name = d.pop("firstName", UNSET)

        surname = d.pop("surname", UNSET)

        uid = d.pop("uid", UNSET)

        username = d.pop("username", UNSET)

        tracker_user = cls(
            display_name=display_name,
            first_name=first_name,
            surname=surname,
            uid=uid,
            username=username,
        )

        tracker_user.additional_properties = d
        return tracker_user

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
