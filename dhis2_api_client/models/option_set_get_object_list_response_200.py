from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.option_set import OptionSet
    from ..models.pager import Pager


T = TypeVar("T", bound="OptionSetGetObjectListResponse200")


@_attrs_define
class OptionSetGetObjectListResponse200:
    """
    Attributes:
        pager (Union[Unset, Pager]):
        option_sets (Union[Unset, list['OptionSet']]):
    """

    pager: Union[Unset, "Pager"] = UNSET
    option_sets: Union[Unset, list["OptionSet"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        option_sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.option_sets, Unset):
            option_sets = []
            for option_sets_item_data in self.option_sets:
                option_sets_item = option_sets_item_data.to_dict()
                option_sets.append(option_sets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if option_sets is not UNSET:
            field_dict["optionSets"] = option_sets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.option_set import OptionSet
        from ..models.pager import Pager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, Pager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = Pager.from_dict(_pager)

        option_sets = []
        _option_sets = d.pop("optionSets", UNSET)
        for option_sets_item_data in _option_sets or []:
            option_sets_item = OptionSet.from_dict(option_sets_item_data)

            option_sets.append(option_sets_item)

        option_set_get_object_list_response_200 = cls(
            pager=pager,
            option_sets=option_sets,
        )

        option_set_get_object_list_response_200.additional_properties = d
        return option_set_get_object_list_response_200

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
