from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Warning_")


@_attrs_define
class Warning_:
    """
    Attributes:
        message (Union[Unset, str]):
        tracker_type (Union[Unset, str]):
        uid (Union[Unset, str]):
        warning_code (Union[Unset, str]):
    """

    message: Union[Unset, str] = UNSET
    tracker_type: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    warning_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        tracker_type = self.tracker_type

        uid = self.uid

        warning_code = self.warning_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if tracker_type is not UNSET:
            field_dict["trackerType"] = tracker_type
        if uid is not UNSET:
            field_dict["uid"] = uid
        if warning_code is not UNSET:
            field_dict["warningCode"] = warning_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message", UNSET)

        tracker_type = d.pop("trackerType", UNSET)

        uid = d.pop("uid", UNSET)

        warning_code = d.pop("warningCode", UNSET)

        warning = cls(
            message=message,
            tracker_type=tracker_type,
            uid=uid,
            warning_code=warning_code,
        )

        warning.additional_properties = d
        return warning

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
