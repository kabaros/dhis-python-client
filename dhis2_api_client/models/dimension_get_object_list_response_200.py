from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dimensional_object import DimensionalObject
    from ..models.pager import Pager


T = TypeVar("T", bound="DimensionGetObjectListResponse200")


@_attrs_define
class DimensionGetObjectListResponse200:
    """
    Attributes:
        pager (Union[Unset, Pager]):
        dimensions (Union[Unset, list['DimensionalObject']]):
    """

    pager: Union[Unset, "Pager"] = UNSET
    dimensions: Union[Unset, list["DimensionalObject"]] = UNSET
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
        from ..models.dimensional_object import DimensionalObject
        from ..models.pager import Pager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, Pager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = Pager.from_dict(_pager)

        dimensions = []
        _dimensions = d.pop("dimensions", UNSET)
        for dimensions_item_data in _dimensions or []:
            dimensions_item = DimensionalObject.from_dict(dimensions_item_data)

            dimensions.append(dimensions_item)

        dimension_get_object_list_response_200 = cls(
            pager=pager,
            dimensions=dimensions,
        )

        dimension_get_object_list_response_200.additional_properties = d
        return dimension_get_object_list_response_200

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
