from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dimension_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_dimensions_item import (
        DimensionGetObjectListGistgetObjectListGistAsCsvResponse200Type0DimensionsItem,
    )
    from ..models.gist_pager import GistPager


T = TypeVar("T", bound="DimensionGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class DimensionGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        dimensions (Union[Unset,
            list['DimensionGetObjectListGistgetObjectListGistAsCsvResponse200Type0DimensionsItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    dimensions: Union[Unset, list["DimensionGetObjectListGistgetObjectListGistAsCsvResponse200Type0DimensionsItem"]] = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        dimensions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.dimensions, Unset):
            dimensions = []
            for dimensions_item_data in self.dimensions:
                dimensions_item = dimensions_item_data.to_dict()
                dimensions.append(dimensions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.dimension_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_dimensions_item import (
            DimensionGetObjectListGistgetObjectListGistAsCsvResponse200Type0DimensionsItem,
        )
        from ..models.gist_pager import GistPager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        dimensions = []
        _dimensions = d.pop("dimensions", UNSET)
        for dimensions_item_data in _dimensions or []:
            dimensions_item = DimensionGetObjectListGistgetObjectListGistAsCsvResponse200Type0DimensionsItem.from_dict(
                dimensions_item_data
            )

            dimensions.append(dimensions_item)

        dimension_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            dimensions=dimensions,
        )

        dimension_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return dimension_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
