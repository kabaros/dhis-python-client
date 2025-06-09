from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_operation_value import AddOperationValue


T = TypeVar("T", bound="AddOperation")


@_attrs_define
class AddOperation:
    """
    Attributes:
        op (Union[Unset, str]):
        path (Union[Unset, str]):
        value (Union[Unset, AddOperationValue]):
    """

    op: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    value: Union[Unset, "AddOperationValue"] = UNSET
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
        from ..models.add_operation_value import AddOperationValue

        d = src_dict.copy()
        op = d.pop("op", UNSET)

        path = d.pop("path", UNSET)

        _value = d.pop("value", UNSET)
        value: Union[Unset, AddOperationValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = AddOperationValue.from_dict(_value)

        add_operation = cls(
            op=op,
            path=path,
            value=value,
        )

        add_operation.additional_properties = d
        return add_operation

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
