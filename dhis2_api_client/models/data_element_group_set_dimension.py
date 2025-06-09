from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_element_group_set_dimension_data_element_group_set import (
        DataElementGroupSetDimensionDataElementGroupSet,
    )
    from ..models.data_element_group_set_dimension_data_element_groups_item import (
        DataElementGroupSetDimensionDataElementGroupsItem,
    )


T = TypeVar("T", bound="DataElementGroupSetDimension")


@_attrs_define
class DataElementGroupSetDimension:
    """
    Attributes:
        data_element_group_set (Union[Unset, DataElementGroupSetDimensionDataElementGroupSet]): A UID reference to a
            DataElementGroupSet
            (Java name `org.hisp.dhis.dataelement.DataElementGroupSet`)
        data_element_groups (Union[Unset, list['DataElementGroupSetDimensionDataElementGroupsItem']]):
    """

    data_element_group_set: Union[Unset, "DataElementGroupSetDimensionDataElementGroupSet"] = UNSET
    data_element_groups: Union[Unset, list["DataElementGroupSetDimensionDataElementGroupsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_element_group_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_element_group_set, Unset):
            data_element_group_set = self.data_element_group_set.to_dict()

        data_element_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_element_groups, Unset):
            data_element_groups = []
            for data_element_groups_item_data in self.data_element_groups:
                data_element_groups_item = data_element_groups_item_data.to_dict()
                data_element_groups.append(data_element_groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_element_group_set is not UNSET:
            field_dict["dataElementGroupSet"] = data_element_group_set
        if data_element_groups is not UNSET:
            field_dict["dataElementGroups"] = data_element_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.data_element_group_set_dimension_data_element_group_set import (
            DataElementGroupSetDimensionDataElementGroupSet,
        )
        from ..models.data_element_group_set_dimension_data_element_groups_item import (
            DataElementGroupSetDimensionDataElementGroupsItem,
        )

        d = src_dict.copy()
        _data_element_group_set = d.pop("dataElementGroupSet", UNSET)
        data_element_group_set: Union[Unset, DataElementGroupSetDimensionDataElementGroupSet]
        if isinstance(_data_element_group_set, Unset):
            data_element_group_set = UNSET
        else:
            data_element_group_set = DataElementGroupSetDimensionDataElementGroupSet.from_dict(_data_element_group_set)

        data_element_groups = []
        _data_element_groups = d.pop("dataElementGroups", UNSET)
        for data_element_groups_item_data in _data_element_groups or []:
            data_element_groups_item = DataElementGroupSetDimensionDataElementGroupsItem.from_dict(
                data_element_groups_item_data
            )

            data_element_groups.append(data_element_groups_item)

        data_element_group_set_dimension = cls(
            data_element_group_set=data_element_group_set,
            data_element_groups=data_element_groups,
        )

        data_element_group_set_dimension.additional_properties = d
        return data_element_group_set_dimension

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
