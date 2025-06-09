from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.field_type import FieldType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Field")


@_attrs_define
class Field:
    """
    Attributes:
        type_ (FieldType):
        category_option_combo (Union[Unset, str]):
        comment (Union[Unset, str]):
        data_element (Union[Unset, str]):
        label (Union[Unset, str]):
        option_set (Union[Unset, str]):
        value (Union[Unset, str]):
    """

    type_: FieldType
    category_option_combo: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    data_element: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    option_set: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        category_option_combo = self.category_option_combo

        comment = self.comment

        data_element = self.data_element

        label = self.label

        option_set = self.option_set

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if category_option_combo is not UNSET:
            field_dict["categoryOptionCombo"] = category_option_combo
        if comment is not UNSET:
            field_dict["comment"] = comment
        if data_element is not UNSET:
            field_dict["dataElement"] = data_element
        if label is not UNSET:
            field_dict["label"] = label
        if option_set is not UNSET:
            field_dict["optionSet"] = option_set
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        type_ = FieldType(d.pop("type"))

        category_option_combo = d.pop("categoryOptionCombo", UNSET)

        comment = d.pop("comment", UNSET)

        data_element = d.pop("dataElement", UNSET)

        label = d.pop("label", UNSET)

        option_set = d.pop("optionSet", UNSET)

        value = d.pop("value", UNSET)

        field = cls(
            type_=type_,
            category_option_combo=category_option_combo,
            comment=comment,
            data_element=data_element,
            label=label,
            option_set=option_set,
            value=value,
        )

        field.additional_properties = d
        return field

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
