from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.incoming_sms import IncomingSms
    from ..models.pager import Pager


T = TypeVar("T", bound="SmsInboundGetObjectListResponse200")


@_attrs_define
class SmsInboundGetObjectListResponse200:
    """
    Attributes:
        pager (Union[Unset, Pager]):
        smsinbound (Union[Unset, list['IncomingSms']]):
    """

    pager: Union[Unset, "Pager"] = UNSET
    smsinbound: Union[Unset, list["IncomingSms"]] = UNSET
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
        from ..models.incoming_sms import IncomingSms
        from ..models.pager import Pager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, Pager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = Pager.from_dict(_pager)

        smsinbound = []
        _smsinbound = d.pop("smsinbound", UNSET)
        for smsinbound_item_data in _smsinbound or []:
            smsinbound_item = IncomingSms.from_dict(smsinbound_item_data)

            smsinbound.append(smsinbound_item)

        sms_inbound_get_object_list_response_200 = cls(
            pager=pager,
            smsinbound=smsinbound,
        )

        sms_inbound_get_object_list_response_200.additional_properties = d
        return sms_inbound_get_object_list_response_200

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
