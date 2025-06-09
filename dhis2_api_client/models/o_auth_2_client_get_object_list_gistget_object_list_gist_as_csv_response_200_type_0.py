from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gist_pager import GistPager
    from ..models.o_auth_2_client_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0o_auth_2_clients_item import (
        OAuth2ClientGetObjectListGistgetObjectListGistAsCsvResponse200Type0OAuth2ClientsItem,
    )


T = TypeVar("T", bound="OAuth2ClientGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class OAuth2ClientGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        o_auth_2_clients (Union[Unset,
            list['OAuth2ClientGetObjectListGistgetObjectListGistAsCsvResponse200Type0OAuth2ClientsItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    o_auth_2_clients: Union[
        Unset, list["OAuth2ClientGetObjectListGistgetObjectListGistAsCsvResponse200Type0OAuth2ClientsItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        o_auth_2_clients: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.o_auth_2_clients, Unset):
            o_auth_2_clients = []
            for o_auth_2_clients_item_data in self.o_auth_2_clients:
                o_auth_2_clients_item = o_auth_2_clients_item_data.to_dict()
                o_auth_2_clients.append(o_auth_2_clients_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if o_auth_2_clients is not UNSET:
            field_dict["oAuth2Clients"] = o_auth_2_clients

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.gist_pager import GistPager
        from ..models.o_auth_2_client_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0o_auth_2_clients_item import (
            OAuth2ClientGetObjectListGistgetObjectListGistAsCsvResponse200Type0OAuth2ClientsItem,
        )

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        o_auth_2_clients = []
        _o_auth_2_clients = d.pop("oAuth2Clients", UNSET)
        for o_auth_2_clients_item_data in _o_auth_2_clients or []:
            o_auth_2_clients_item = (
                OAuth2ClientGetObjectListGistgetObjectListGistAsCsvResponse200Type0OAuth2ClientsItem.from_dict(
                    o_auth_2_clients_item_data
                )
            )

            o_auth_2_clients.append(o_auth_2_clients_item)

        o_auth_2_client_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            o_auth_2_clients=o_auth_2_clients,
        )

        o_auth_2_client_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return o_auth_2_client_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
