from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_element_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_data_elements_item import (
        DataElementGetObjectListGistgetObjectListGistAsCsvResponse200Type0DataElementsItem,
    )
    from ..models.gist_pager import GistPager


T = TypeVar("T", bound="DataElementGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class DataElementGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        data_elements (Union[Unset,
            list['DataElementGetObjectListGistgetObjectListGistAsCsvResponse200Type0DataElementsItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    data_elements: Union[
        Unset, list["DataElementGetObjectListGistgetObjectListGistAsCsvResponse200Type0DataElementsItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        data_elements: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_elements, Unset):
            data_elements = []
            for data_elements_item_data in self.data_elements:
                data_elements_item = data_elements_item_data.to_dict()
                data_elements.append(data_elements_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if data_elements is not UNSET:
            field_dict["dataElements"] = data_elements

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.data_element_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_data_elements_item import (
            DataElementGetObjectListGistgetObjectListGistAsCsvResponse200Type0DataElementsItem,
        )
        from ..models.gist_pager import GistPager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        data_elements = []
        _data_elements = d.pop("dataElements", UNSET)
        for data_elements_item_data in _data_elements or []:
            data_elements_item = (
                DataElementGetObjectListGistgetObjectListGistAsCsvResponse200Type0DataElementsItem.from_dict(
                    data_elements_item_data
                )
            )

            data_elements.append(data_elements_item)

        data_element_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            data_elements=data_elements,
        )

        data_element_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return data_element_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
