from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.replace_operation_value import ReplaceOperationValue


T = TypeVar("T", bound="ReplaceOperation")


@_attrs_define
class ReplaceOperation:
    """
    Attributes:
        op (Union[Unset, str]):
        path (Union[Unset, str]):
        value (Union[Unset, ReplaceOperationValue]):
    """

    op: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    value: Union[Unset, "ReplaceOperationValue"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        op = self.op

        path = self.path

        value: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if op is not UNSET:
            field_dict["op"] = op
        if path is not UNSET:
            field_dict["path"] = path
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.replace_operation_value import ReplaceOperationValue

        d = src_dict.copy()
        op = d.pop("op", UNSET)

        path = d.pop("path", UNSET)

        _value = d.pop("value", UNSET)
        value: Union[Unset, ReplaceOperationValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = ReplaceOperationValue.from_dict(_value)

        replace_operation = cls(
            op=op,
            path=path,
            value=value,
        )

        replace_operation.additional_properties = d
        return replace_operation

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
