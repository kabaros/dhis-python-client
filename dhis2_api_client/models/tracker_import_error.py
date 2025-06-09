from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrackerImportError")


@_attrs_define
class TrackerImportError:
    """
    Attributes:
        args (Union[Unset, list[str]]):
        error_code (Union[Unset, str]):
        message (Union[Unset, str]):
        tracker_type (Union[Unset, str]):
        uid (Union[Unset, str]):
    """

    args: Union[Unset, list[str]] = UNSET
    error_code: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    tracker_type: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        args: Union[Unset, list[str]] = UNSET
        if not isinstance(self.args, Unset):
            args = self.args

        error_code = self.error_code

        message = self.message

        tracker_type = self.tracker_type

        uid = self.uid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if args is not UNSET:
            field_dict["args"] = args
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if message is not UNSET:
            field_dict["message"] = message
        if tracker_type is not UNSET:
            field_dict["trackerType"] = tracker_type
        if uid is not UNSET:
            field_dict["uid"] = uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        args = cast(list[str], d.pop("args", UNSET))

        error_code = d.pop("errorCode", UNSET)

        message = d.pop("message", UNSET)

        tracker_type = d.pop("trackerType", UNSET)

        uid = d.pop("uid", UNSET)

        tracker_import_error = cls(
            args=args,
            error_code=error_code,
            message=message,
            tracker_type=tracker_type,
            uid=uid,
        )

        tracker_import_error.additional_properties = d
        return tracker_import_error

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
