from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.option_group import OptionGroup
    from ..models.pager import Pager


T = TypeVar("T", bound="OptionGroupGetObjectListResponse200")


@_attrs_define
class OptionGroupGetObjectListResponse200:
    """
    Attributes:
        pager (Union[Unset, Pager]):
        option_groups (Union[Unset, list['OptionGroup']]):
    """

    pager: Union[Unset, "Pager"] = UNSET
    option_groups: Union[Unset, list["OptionGroup"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        option_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.option_groups, Unset):
            option_groups = []
            for option_groups_item_data in self.option_groups:
                option_groups_item = option_groups_item_data.to_dict()
                option_groups.append(option_groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if option_groups is not UNSET:
            field_dict["optionGroups"] = option_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.option_group import OptionGroup
        from ..models.pager import Pager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, Pager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = Pager.from_dict(_pager)

        option_groups = []
        _option_groups = d.pop("optionGroups", UNSET)
        for option_groups_item_data in _option_groups or []:
            option_groups_item = OptionGroup.from_dict(option_groups_item_data)

            option_groups.append(option_groups_item)

        option_group_get_object_list_response_200 = cls(
            pager=pager,
            option_groups=option_groups,
        )

        option_group_get_object_list_response_200.additional_properties = d
        return option_group_get_object_list_response_200

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
