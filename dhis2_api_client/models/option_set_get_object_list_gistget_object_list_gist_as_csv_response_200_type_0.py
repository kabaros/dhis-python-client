from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gist_pager import GistPager
    from ..models.option_set_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_option_sets_item import (
        OptionSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0OptionSetsItem,
    )


T = TypeVar("T", bound="OptionSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class OptionSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        option_sets (Union[Unset,
            list['OptionSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0OptionSetsItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    option_sets: Union[
        Unset, list["OptionSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0OptionSetsItem"]
    ] = UNSET
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
        from ..models.gist_pager import GistPager
        from ..models.option_set_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_option_sets_item import (
            OptionSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0OptionSetsItem,
        )

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        option_sets = []
        _option_sets = d.pop("optionSets", UNSET)
        for option_sets_item_data in _option_sets or []:
            option_sets_item = OptionSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0OptionSetsItem.from_dict(
                option_sets_item_data
            )

            option_sets.append(option_sets_item)

        option_set_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            option_sets=option_sets,
        )

        option_set_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return option_set_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
