from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataValueCategoryDto")


@_attrs_define
class DataValueCategoryDto:
    """
    Attributes:
        combo (Union[Unset, str]): A UID for an CategoryCombo object
            (Java name `org.hisp.dhis.category.CategoryCombo`) Example: iZ9tI8jD7T4.
        options (Union[Unset, list[str]]):
    """

    combo: Union[Unset, str] = UNSET
    options: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        combo = self.combo

        options: Union[Unset, list[str]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if combo is not UNSET:
            field_dict["combo"] = combo
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        combo = d.pop("combo", UNSET)

        options = cast(list[str], d.pop("options", UNSET))

        data_value_category_dto = cls(
            combo=combo,
            options=options,
        )

        data_value_category_dto.additional_properties = d
        return data_value_category_dto

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
