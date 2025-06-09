from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.web_message_error_code import WebMessageErrorCode
from ..models.web_message_status import WebMessageStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.web_message_response import WebMessageResponse


T = TypeVar("T", bound="WebMessage")


@_attrs_define
class WebMessage:
    """
    Attributes:
        error_code (WebMessageErrorCode):
        status (WebMessageStatus):
        code (Union[Unset, int]):
        dev_message (Union[Unset, str]):
        http_status (Union[Unset, str]):
        http_status_code (Union[Unset, int]):
        message (Union[Unset, str]):
        response (Union[Unset, WebMessageResponse]):
    """

    error_code: WebMessageErrorCode
    status: WebMessageStatus
    code: Union[Unset, int] = UNSET
    dev_message: Union[Unset, str] = UNSET
    http_status: Union[Unset, str] = UNSET
    http_status_code: Union[Unset, int] = UNSET
    message: Union[Unset, str] = UNSET
    response: Union[Unset, "WebMessageResponse"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_code = self.error_code.value

        status = self.status.value

        code = self.code

        dev_message = self.dev_message

        http_status = self.http_status

        http_status_code = self.http_status_code

        message = self.message

        response: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.response, Unset):
            response = self.response.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "errorCode": error_code,
                "status": status,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if dev_message is not UNSET:
            field_dict["devMessage"] = dev_message
        if http_status is not UNSET:
            field_dict["httpStatus"] = http_status
        if http_status_code is not UNSET:
            field_dict["httpStatusCode"] = http_status_code
        if message is not UNSET:
            field_dict["message"] = message
        if response is not UNSET:
            field_dict["response"] = response

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.web_message_response import WebMessageResponse

        d = src_dict.copy()
        error_code = WebMessageErrorCode(d.pop("errorCode"))

        status = WebMessageStatus(d.pop("status"))

        code = d.pop("code", UNSET)

        dev_message = d.pop("devMessage", UNSET)

        http_status = d.pop("httpStatus", UNSET)

        http_status_code = d.pop("httpStatusCode", UNSET)

        message = d.pop("message", UNSET)

        _response = d.pop("response", UNSET)
        response: Union[Unset, WebMessageResponse]
        if isinstance(_response, Unset):
            response = UNSET
        else:
            response = WebMessageResponse.from_dict(_response)

        web_message = cls(
            error_code=error_code,
            status=status,
            code=code,
            dev_message=dev_message,
            http_status=http_status,
            http_status_code=http_status_code,
            message=message,
            response=response,
        )

        web_message.additional_properties = d
        return web_message

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
