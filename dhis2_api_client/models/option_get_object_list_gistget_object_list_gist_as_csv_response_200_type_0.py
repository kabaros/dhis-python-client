from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gist_pager import GistPager
    from ..models.option_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_options_item import (
        OptionGetObjectListGistgetObjectListGistAsCsvResponse200Type0OptionsItem,
    )


T = TypeVar("T", bound="OptionGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class OptionGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        options (Union[Unset, list['OptionGetObjectListGistgetObjectListGistAsCsvResponse200Type0OptionsItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    options: Union[Unset, list["OptionGetObjectListGistgetObjectListGistAsCsvResponse200Type0OptionsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        options: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.gist_pager import GistPager
        from ..models.option_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_options_item import (
            OptionGetObjectListGistgetObjectListGistAsCsvResponse200Type0OptionsItem,
        )

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = OptionGetObjectListGistgetObjectListGistAsCsvResponse200Type0OptionsItem.from_dict(
                options_item_data
            )

            options.append(options_item)

        option_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            options=options,
        )

        option_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return option_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
