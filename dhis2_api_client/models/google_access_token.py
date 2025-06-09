from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleAccessToken")


@_attrs_define
class GoogleAccessToken:
    """
    Attributes:
        expires_in (int):
        access_token (Union[Unset, str]):
        client_id (Union[Unset, str]):
    """

    expires_in: int
    access_token: Union[Unset, str] = UNSET
    client_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_in = self.expires_in

        access_token = self.access_token

        client_id = self.client_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expires_in": expires_in,
            }
        )
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if client_id is not UNSET:
            field_dict["client_id"] = client_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        expires_in = d.pop("expires_in")

        access_token = d.pop("access_token", UNSET)

        client_id = d.pop("client_id", UNSET)

        google_access_token = cls(
            expires_in=expires_in,
            access_token=access_token,
            client_id=client_id,
        )

        google_access_token.additional_properties = d
        return google_access_token

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
