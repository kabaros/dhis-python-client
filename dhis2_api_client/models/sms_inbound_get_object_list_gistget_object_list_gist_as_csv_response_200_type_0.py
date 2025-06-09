from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gist_pager import GistPager
    from ..models.sms_inbound_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_smsinbound_item import (
        SmsInboundGetObjectListGistgetObjectListGistAsCsvResponse200Type0SmsinboundItem,
    )


T = TypeVar("T", bound="SmsInboundGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class SmsInboundGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        smsinbound (Union[Unset,
            list['SmsInboundGetObjectListGistgetObjectListGistAsCsvResponse200Type0SmsinboundItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    smsinbound: Union[
        Unset, list["SmsInboundGetObjectListGistgetObjectListGistAsCsvResponse200Type0SmsinboundItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        smsinbound: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.smsinbound, Unset):
            smsinbound = []
            for smsinbound_item_data in self.smsinbound:
                smsinbound_item = smsinbound_item_data.to_dict()
                smsinbound.append(smsinbound_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if smsinbound is not UNSET:
            field_dict["smsinbound"] = smsinbound

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.gist_pager import GistPager
        from ..models.sms_inbound_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_smsinbound_item import (
            SmsInboundGetObjectListGistgetObjectListGistAsCsvResponse200Type0SmsinboundItem,
        )

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        smsinbound = []
        _smsinbound = d.pop("smsinbound", UNSET)
        for smsinbound_item_data in _smsinbound or []:
            smsinbound_item = SmsInboundGetObjectListGistgetObjectListGistAsCsvResponse200Type0SmsinboundItem.from_dict(
                smsinbound_item_data
            )

            smsinbound.append(smsinbound_item)

        sms_inbound_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            smsinbound=smsinbound,
        )

        sms_inbound_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return sms_inbound_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
