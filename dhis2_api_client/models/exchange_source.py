from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.source_params import SourceParams
    from ..models.source_request import SourceRequest


T = TypeVar("T", bound="ExchangeSource")


@_attrs_define
class ExchangeSource:
    """
    Attributes:
        params (Union[Unset, SourceParams]):
        requests (Union[Unset, list['SourceRequest']]):
    """

    params: Union[Unset, "SourceParams"] = UNSET
    requests: Union[Unset, list["SourceRequest"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        params: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        requests: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.requests, Unset):
            requests = []
            for requests_item_data in self.requests:
                requests_item = requests_item_data.to_dict()
                requests.append(requests_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if params is not UNSET:
            field_dict["params"] = params
        if requests is not UNSET:
            field_dict["requests"] = requests

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.source_params import SourceParams
        from ..models.source_request import SourceRequest

        d = src_dict.copy()
        _params = d.pop("params", UNSET)
        params: Union[Unset, SourceParams]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = SourceParams.from_dict(_params)

        requests = []
        _requests = d.pop("requests", UNSET)
        for requests_item_data in _requests or []:
            requests_item = SourceRequest.from_dict(requests_item_data)

            requests.append(requests_item)

        exchange_source = cls(
            params=params,
            requests=requests,
        )

        exchange_source.additional_properties = d
        return exchange_source

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
