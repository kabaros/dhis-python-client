from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.form_category_combo_categories_item_category_options_item import (
        FormCategoryComboCategoriesItemCategoryOptionsItem,
    )


T = TypeVar("T", bound="FormCategoryComboCategoriesItem")


@_attrs_define
class FormCategoryComboCategoriesItem:
    """
    Attributes:
        category_options (Union[Unset, list['FormCategoryComboCategoriesItemCategoryOptionsItem']]):
        id (Union[Unset, str]):
        label (Union[Unset, str]):
    """

    category_options: Union[Unset, list["FormCategoryComboCategoriesItemCategoryOptionsItem"]] = UNSET
    id: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category_options: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.category_options, Unset):
            category_options = []
            for category_options_item_data in self.category_options:
                category_options_item = category_options_item_data.to_dict()
                category_options.append(category_options_item)

        id = self.id

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category_options is not UNSET:
            field_dict["categoryOptions"] = category_options
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.form_category_combo_categories_item_category_options_item import (
            FormCategoryComboCategoriesItemCategoryOptionsItem,
        )

        d = src_dict.copy()
        category_options = []
        _category_options = d.pop("categoryOptions", UNSET)
        for category_options_item_data in _category_options or []:
            category_options_item = FormCategoryComboCategoriesItemCategoryOptionsItem.from_dict(
                category_options_item_data
            )

            category_options.append(category_options_item)

        id = d.pop("id", UNSET)

        label = d.pop("label", UNSET)

        form_category_combo_categories_item = cls(
            category_options=category_options,
            id=id,
            label=label,
        )

        form_category_combo_categories_item.additional_properties = d
        return form_category_combo_categories_item

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
