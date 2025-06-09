from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_set import DataSet
    from ..models.pager import Pager


T = TypeVar("T", bound="DataSetGetObjectListResponse200")


@_attrs_define
class DataSetGetObjectListResponse200:
    """
    Attributes:
        pager (Union[Unset, Pager]):
        data_sets (Union[Unset, list['DataSet']]):
    """

    pager: Union[Unset, "Pager"] = UNSET
    data_sets: Union[Unset, list["DataSet"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        data_sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_sets, Unset):
            data_sets = []
            for data_sets_item_data in self.data_sets:
                data_sets_item = data_sets_item_data.to_dict()
                data_sets.append(data_sets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if data_sets is not UNSET:
            field_dict["dataSets"] = data_sets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.data_set import DataSet
        from ..models.pager import Pager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, Pager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = Pager.from_dict(_pager)

        data_sets = []
        _data_sets = d.pop("dataSets", UNSET)
        for data_sets_item_data in _data_sets or []:
            data_sets_item = DataSet.from_dict(data_sets_item_data)

            data_sets.append(data_sets_item)

        data_set_get_object_list_response_200 = cls(
            pager=pager,
            data_sets=data_sets,
        )

        data_set_get_object_list_response_200.additional_properties = d
        return data_set_get_object_list_response_200

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
