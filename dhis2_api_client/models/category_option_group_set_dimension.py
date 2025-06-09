from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category_option_group_set_dimension_category_option_group_set import (
        CategoryOptionGroupSetDimensionCategoryOptionGroupSet,
    )
    from ..models.category_option_group_set_dimension_category_option_groups_item import (
        CategoryOptionGroupSetDimensionCategoryOptionGroupsItem,
    )


T = TypeVar("T", bound="CategoryOptionGroupSetDimension")


@_attrs_define
class CategoryOptionGroupSetDimension:
    """
    Attributes:
        category_option_group_set (Union[Unset, CategoryOptionGroupSetDimensionCategoryOptionGroupSet]): A UID reference
            to a CategoryOptionGroupSet
            (Java name `org.hisp.dhis.category.CategoryOptionGroupSet`)
        category_option_groups (Union[Unset, list['CategoryOptionGroupSetDimensionCategoryOptionGroupsItem']]):
    """

    category_option_group_set: Union[Unset, "CategoryOptionGroupSetDimensionCategoryOptionGroupSet"] = UNSET
    category_option_groups: Union[Unset, list["CategoryOptionGroupSetDimensionCategoryOptionGroupsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category_option_group_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.category_option_group_set, Unset):
            category_option_group_set = self.category_option_group_set.to_dict()

        category_option_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.category_option_groups, Unset):
            category_option_groups = []
            for category_option_groups_item_data in self.category_option_groups:
                category_option_groups_item = category_option_groups_item_data.to_dict()
                category_option_groups.append(category_option_groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category_option_group_set is not UNSET:
            field_dict["categoryOptionGroupSet"] = category_option_group_set
        if category_option_groups is not UNSET:
            field_dict["categoryOptionGroups"] = category_option_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.category_option_group_set_dimension_category_option_group_set import (
            CategoryOptionGroupSetDimensionCategoryOptionGroupSet,
        )
        from ..models.category_option_group_set_dimension_category_option_groups_item import (
            CategoryOptionGroupSetDimensionCategoryOptionGroupsItem,
        )

        d = src_dict.copy()
        _category_option_group_set = d.pop("categoryOptionGroupSet", UNSET)
        category_option_group_set: Union[Unset, CategoryOptionGroupSetDimensionCategoryOptionGroupSet]
        if isinstance(_category_option_group_set, Unset):
            category_option_group_set = UNSET
        else:
            category_option_group_set = CategoryOptionGroupSetDimensionCategoryOptionGroupSet.from_dict(
                _category_option_group_set
            )

        category_option_groups = []
        _category_option_groups = d.pop("categoryOptionGroups", UNSET)
        for category_option_groups_item_data in _category_option_groups or []:
            category_option_groups_item = CategoryOptionGroupSetDimensionCategoryOptionGroupsItem.from_dict(
                category_option_groups_item_data
            )

            category_option_groups.append(category_option_groups_item)

        category_option_group_set_dimension = cls(
            category_option_group_set=category_option_group_set,
            category_option_groups=category_option_groups,
        )

        category_option_group_set_dimension.additional_properties = d
        return category_option_group_set_dimension

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
