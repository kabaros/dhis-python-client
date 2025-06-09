from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.exchange_target_type import ExchangeTargetType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api import Api
    from ..models.target_request import TargetRequest


T = TypeVar("T", bound="ExchangeTarget")


@_attrs_define
class ExchangeTarget:
    """
    Attributes:
        type_ (ExchangeTargetType):
        api (Union[Unset, Api]):
        request (Union[Unset, TargetRequest]):
    """

    type_: ExchangeTargetType
    api: Union[Unset, "Api"] = UNSET
    request: Union[Unset, "TargetRequest"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        api: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.api, Unset):
            api = self.api.to_dict()

        request: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.request, Unset):
            request = self.request.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if api is not UNSET:
            field_dict["api"] = api
        if request is not UNSET:
            field_dict["request"] = request

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.api import Api
        from ..models.target_request import TargetRequest

        d = src_dict.copy()
        type_ = ExchangeTargetType(d.pop("type"))

        _api = d.pop("api", UNSET)
        api: Union[Unset, Api]
        if isinstance(_api, Unset):
            api = UNSET
        else:
            api = Api.from_dict(_api)

        _request = d.pop("request", UNSET)
        request: Union[Unset, TargetRequest]
        if isinstance(_request, Unset):
            request = UNSET
        else:
            request = TargetRequest.from_dict(_request)

        exchange_target = cls(
            type_=type_,
            api=api,
            request=request,
        )

        exchange_target.additional_properties = d
        return exchange_target

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
