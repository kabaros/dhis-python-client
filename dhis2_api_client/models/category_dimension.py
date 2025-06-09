from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category_dimension_category import CategoryDimensionCategory
    from ..models.category_dimension_category_options_item import CategoryDimensionCategoryOptionsItem


T = TypeVar("T", bound="CategoryDimension")


@_attrs_define
class CategoryDimension:
    """
    Attributes:
        category (Union[Unset, CategoryDimensionCategory]): A UID reference to a Category
            (Java name `org.hisp.dhis.category.Category`)
        category_options (Union[Unset, list['CategoryDimensionCategoryOptionsItem']]):
    """

    category: Union[Unset, "CategoryDimensionCategory"] = UNSET
    category_options: Union[Unset, list["CategoryDimensionCategoryOptionsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        category_options: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.category_options, Unset):
            category_options = []
            for category_options_item_data in self.category_options:
                category_options_item = category_options_item_data.to_dict()
                category_options.append(category_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if category_options is not UNSET:
            field_dict["categoryOptions"] = category_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.category_dimension_category import CategoryDimensionCategory
        from ..models.category_dimension_category_options_item import CategoryDimensionCategoryOptionsItem

        d = src_dict.copy()
        _category = d.pop("category", UNSET)
        category: Union[Unset, CategoryDimensionCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = CategoryDimensionCategory.from_dict(_category)

        category_options = []
        _category_options = d.pop("categoryOptions", UNSET)
        for category_options_item_data in _category_options or []:
            category_options_item = CategoryDimensionCategoryOptionsItem.from_dict(category_options_item_data)

            category_options.append(category_options_item)

        category_dimension = cls(
            category=category,
            category_options=category_options,
        )

        category_dimension.additional_properties = d
        return category_dimension

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
