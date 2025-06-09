from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gist_pager import GistPager
    from ..models.indicator_type_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_indicator_types_item import (
        IndicatorTypeGetObjectListGistgetObjectListGistAsCsvResponse200Type0IndicatorTypesItem,
    )


T = TypeVar("T", bound="IndicatorTypeGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class IndicatorTypeGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        indicator_types (Union[Unset,
            list['IndicatorTypeGetObjectListGistgetObjectListGistAsCsvResponse200Type0IndicatorTypesItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    indicator_types: Union[
        Unset, list["IndicatorTypeGetObjectListGistgetObjectListGistAsCsvResponse200Type0IndicatorTypesItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        indicator_types: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.indicator_types, Unset):
            indicator_types = []
            for indicator_types_item_data in self.indicator_types:
                indicator_types_item = indicator_types_item_data.to_dict()
                indicator_types.append(indicator_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if indicator_types is not UNSET:
            field_dict["indicatorTypes"] = indicator_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.gist_pager import GistPager
        from ..models.indicator_type_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_indicator_types_item import (
            IndicatorTypeGetObjectListGistgetObjectListGistAsCsvResponse200Type0IndicatorTypesItem,
        )

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        indicator_types = []
        _indicator_types = d.pop("indicatorTypes", UNSET)
        for indicator_types_item_data in _indicator_types or []:
            indicator_types_item = (
                IndicatorTypeGetObjectListGistgetObjectListGistAsCsvResponse200Type0IndicatorTypesItem.from_dict(
                    indicator_types_item_data
                )
            )

            indicator_types.append(indicator_types_item)

        indicator_type_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            indicator_types=indicator_types,
        )

        indicator_type_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return indicator_type_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
