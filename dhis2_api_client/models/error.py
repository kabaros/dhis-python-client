from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Error")


@_attrs_define
class Error:
    """
    Attributes:
        args (Union[Unset, list[str]]):
        code (Union[Unset, str]):
        id (Union[Unset, str]):
        message (Union[Unset, str]):
        type_ (Union[Unset, str]):
    """

    args: Union[Unset, list[str]] = UNSET
    code: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        args: Union[Unset, list[str]] = UNSET
        if not isinstance(self.args, Unset):
            args = self.args

        code = self.code

        id = self.id

        message = self.message

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if args is not UNSET:
            field_dict["args"] = args
        if code is not UNSET:
            field_dict["code"] = code
        if id is not UNSET:
            field_dict["id"] = id
        if message is not UNSET:
            field_dict["message"] = message
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        args = cast(list[str], d.pop("args", UNSET))

        code = d.pop("code", UNSET)

        id = d.pop("id", UNSET)

        message = d.pop("message", UNSET)

        type_ = d.pop("type", UNSET)

        error = cls(
            args=args,
            code=code,
            id=id,
            message=message,
            type_=type_,
        )

        error.additional_properties = d
        return error

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
