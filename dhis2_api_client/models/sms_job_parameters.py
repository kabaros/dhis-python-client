from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SmsJobParameters")


@_attrs_define
class SmsJobParameters:
    """
    Attributes:
        message (Union[Unset, str]):
        recipients_list (Union[Unset, list[str]]):
        sms_subject (Union[Unset, str]):
    """

    message: Union[Unset, str] = UNSET
    recipients_list: Union[Unset, list[str]] = UNSET
    sms_subject: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        recipients_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.recipients_list, Unset):
            recipients_list = self.recipients_list

        sms_subject = self.sms_subject

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if recipients_list is not UNSET:
            field_dict["recipientsList"] = recipients_list
        if sms_subject is not UNSET:
            field_dict["smsSubject"] = sms_subject

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message", UNSET)

        recipients_list = cast(list[str], d.pop("recipientsList", UNSET))

        sms_subject = d.pop("smsSubject", UNSET)

        sms_job_parameters = cls(
            message=message,
            recipients_list=recipients_list,
            sms_subject=sms_subject,
        )

        sms_job_parameters.additional_properties = d
        return sms_job_parameters

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
