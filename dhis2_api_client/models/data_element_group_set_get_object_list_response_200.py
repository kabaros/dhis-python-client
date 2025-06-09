from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_element_group_set import DataElementGroupSet
    from ..models.pager import Pager


T = TypeVar("T", bound="DataElementGroupSetGetObjectListResponse200")


@_attrs_define
class DataElementGroupSetGetObjectListResponse200:
    """
    Attributes:
        pager (Union[Unset, Pager]):
        data_element_group_sets (Union[Unset, list['DataElementGroupSet']]):
    """

    pager: Union[Unset, "Pager"] = UNSET
    data_element_group_sets: Union[Unset, list["DataElementGroupSet"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        data_element_group_sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_element_group_sets, Unset):
            data_element_group_sets = []
            for data_element_group_sets_item_data in self.data_element_group_sets:
                data_element_group_sets_item = data_element_group_sets_item_data.to_dict()
                data_element_group_sets.append(data_element_group_sets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if data_element_group_sets is not UNSET:
            field_dict["dataElementGroupSets"] = data_element_group_sets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.data_element_group_set import DataElementGroupSet
        from ..models.pager import Pager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, Pager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = Pager.from_dict(_pager)

        data_element_group_sets = []
        _data_element_group_sets = d.pop("dataElementGroupSets", UNSET)
        for data_element_group_sets_item_data in _data_element_group_sets or []:
            data_element_group_sets_item = DataElementGroupSet.from_dict(data_element_group_sets_item_data)

            data_element_group_sets.append(data_element_group_sets_item)

        data_element_group_set_get_object_list_response_200 = cls(
            pager=pager,
            data_element_group_sets=data_element_group_sets,
        )

        data_element_group_set_get_object_list_response_200.additional_properties = d
        return data_element_group_set_get_object_list_response_200

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
