from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_token_get_object_list_gistget_object_list_gist_as_csv_2_response_200_type_0_api_token_item import (
        ApiTokenGetObjectListGistgetObjectListGistAsCsv2Response200Type0ApiTokenItem,
    )
    from ..models.gist_pager import GistPager


T = TypeVar("T", bound="ApiTokenGetObjectListGistgetObjectListGistAsCsv2Response200Type0")


@_attrs_define
class ApiTokenGetObjectListGistgetObjectListGistAsCsv2Response200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        api_token (Union[Unset, list['ApiTokenGetObjectListGistgetObjectListGistAsCsv2Response200Type0ApiTokenItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    api_token: Union[Unset, list["ApiTokenGetObjectListGistgetObjectListGistAsCsv2Response200Type0ApiTokenItem"]] = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        api_token: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.api_token, Unset):
            api_token = []
            for api_token_item_data in self.api_token:
                api_token_item = api_token_item_data.to_dict()
                api_token.append(api_token_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if api_token is not UNSET:
            field_dict["apiToken"] = api_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.api_token_get_object_list_gistget_object_list_gist_as_csv_2_response_200_type_0_api_token_item import (
            ApiTokenGetObjectListGistgetObjectListGistAsCsv2Response200Type0ApiTokenItem,
        )
        from ..models.gist_pager import GistPager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        api_token = []
        _api_token = d.pop("apiToken", UNSET)
        for api_token_item_data in _api_token or []:
            api_token_item = ApiTokenGetObjectListGistgetObjectListGistAsCsv2Response200Type0ApiTokenItem.from_dict(
                api_token_item_data
            )

            api_token.append(api_token_item)

        api_token_get_object_list_gistget_object_list_gist_as_csv_2_response_200_type_0 = cls(
            pager=pager,
            api_token=api_token,
        )

        api_token_get_object_list_gistget_object_list_gist_as_csv_2_response_200_type_0.additional_properties = d
        return api_token_get_object_list_gistget_object_list_gist_as_csv_2_response_200_type_0

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
