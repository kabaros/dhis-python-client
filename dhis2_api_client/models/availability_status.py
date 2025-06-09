from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AvailabilityStatus")


@_attrs_define
class AvailabilityStatus:
    """
    Attributes:
        status_code (int):
        available (Union[Unset, bool]):
        message (Union[Unset, str]):
        status_phrase (Union[Unset, str]):
    """

    status_code: int
    available: Union[Unset, bool] = UNSET
    message: Union[Unset, str] = UNSET
    status_phrase: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status_code = self.status_code

        available = self.available

        message = self.message

        status_phrase = self.status_phrase

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "statusCode": status_code,
            }
        )
        if available is not UNSET:
            field_dict["available"] = available
        if message is not UNSET:
            field_dict["message"] = message
        if status_phrase is not UNSET:
            field_dict["statusPhrase"] = status_phrase

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        status_code = d.pop("statusCode")

        available = d.pop("available", UNSET)

        message = d.pop("message", UNSET)

        status_phrase = d.pop("statusPhrase", UNSET)

        availability_status = cls(
            status_code=status_code,
            available=available,
            message=message,
            status_phrase=status_phrase,
        )

        availability_status.additional_properties = d
        return availability_status

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
