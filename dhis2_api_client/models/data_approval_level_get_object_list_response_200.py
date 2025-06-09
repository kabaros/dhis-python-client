from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_approval_level import DataApprovalLevel
    from ..models.pager import Pager


T = TypeVar("T", bound="DataApprovalLevelGetObjectListResponse200")


@_attrs_define
class DataApprovalLevelGetObjectListResponse200:
    """
    Attributes:
        pager (Union[Unset, Pager]):
        data_approval_levels (Union[Unset, list['DataApprovalLevel']]):
    """

    pager: Union[Unset, "Pager"] = UNSET
    data_approval_levels: Union[Unset, list["DataApprovalLevel"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        data_approval_levels: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_approval_levels, Unset):
            data_approval_levels = []
            for data_approval_levels_item_data in self.data_approval_levels:
                data_approval_levels_item = data_approval_levels_item_data.to_dict()
                data_approval_levels.append(data_approval_levels_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if data_approval_levels is not UNSET:
            field_dict["dataApprovalLevels"] = data_approval_levels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.data_approval_level import DataApprovalLevel
        from ..models.pager import Pager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, Pager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = Pager.from_dict(_pager)

        data_approval_levels = []
        _data_approval_levels = d.pop("dataApprovalLevels", UNSET)
        for data_approval_levels_item_data in _data_approval_levels or []:
            data_approval_levels_item = DataApprovalLevel.from_dict(data_approval_levels_item_data)

            data_approval_levels.append(data_approval_levels_item)

        data_approval_level_get_object_list_response_200 = cls(
            pager=pager,
            data_approval_levels=data_approval_levels,
        )

        data_approval_level_get_object_list_response_200.additional_properties = d
        return data_approval_level_get_object_list_response_200

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
