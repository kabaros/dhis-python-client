from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_token_auth import ApiTokenAuth
    from ..models.http_basic_auth import HttpBasicAuth
    from ..models.webhook_target_headers import WebhookTargetHeaders


T = TypeVar("T", bound="WebhookTarget")


@_attrs_define
class WebhookTarget:
    """
    Attributes:
        client_id (str):
        content_type (str):
        url (str):
        auth (Union['ApiTokenAuth', 'HttpBasicAuth', Unset]):
        headers (Union[Unset, WebhookTargetHeaders]):
        type_ (Union[Unset, str]):
    """

    client_id: str
    content_type: str
    url: str
    auth: Union["ApiTokenAuth", "HttpBasicAuth", Unset] = UNSET
    headers: Union[Unset, "WebhookTargetHeaders"] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.http_basic_auth import HttpBasicAuth

        client_id = self.client_id

        content_type = self.content_type

        url = self.url

        auth: Union[Unset, dict[str, Any]]
        if isinstance(self.auth, Unset):
            auth = UNSET
        elif isinstance(self.auth, HttpBasicAuth):
            auth = self.auth.to_dict()
        else:
            auth = self.auth.to_dict()

        headers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientId": client_id,
                "contentType": content_type,
                "url": url,
            }
        )
        if auth is not UNSET:
            field_dict["auth"] = auth
        if headers is not UNSET:
            field_dict["headers"] = headers
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.api_token_auth import ApiTokenAuth
        from ..models.http_basic_auth import HttpBasicAuth
        from ..models.webhook_target_headers import WebhookTargetHeaders

        d = src_dict.copy()
        client_id = d.pop("clientId")

        content_type = d.pop("contentType")

        url = d.pop("url")

        def _parse_auth(data: object) -> Union["ApiTokenAuth", "HttpBasicAuth", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                auth_type_0 = HttpBasicAuth.from_dict(data)

                return auth_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            auth_type_1 = ApiTokenAuth.from_dict(data)

            return auth_type_1

        auth = _parse_auth(d.pop("auth", UNSET))

        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, WebhookTargetHeaders]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = WebhookTargetHeaders.from_dict(_headers)

        type_ = d.pop("type", UNSET)

        webhook_target = cls(
            client_id=client_id,
            content_type=content_type,
            url=url,
            auth=auth,
            headers=headers,
            type_=type_,
        )

        webhook_target.additional_properties = d
        return webhook_target

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
