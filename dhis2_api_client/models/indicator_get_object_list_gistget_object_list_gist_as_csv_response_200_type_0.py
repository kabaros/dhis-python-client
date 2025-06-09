from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gist_pager import GistPager
    from ..models.indicator_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_indicators_item import (
        IndicatorGetObjectListGistgetObjectListGistAsCsvResponse200Type0IndicatorsItem,
    )


T = TypeVar("T", bound="IndicatorGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class IndicatorGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        indicators (Union[Unset,
            list['IndicatorGetObjectListGistgetObjectListGistAsCsvResponse200Type0IndicatorsItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    indicators: Union[Unset, list["IndicatorGetObjectListGistgetObjectListGistAsCsvResponse200Type0IndicatorsItem"]] = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        indicators: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.indicators, Unset):
            indicators = []
            for indicators_item_data in self.indicators:
                indicators_item = indicators_item_data.to_dict()
                indicators.append(indicators_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if indicators is not UNSET:
            field_dict["indicators"] = indicators

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.gist_pager import GistPager
        from ..models.indicator_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_indicators_item import (
            IndicatorGetObjectListGistgetObjectListGistAsCsvResponse200Type0IndicatorsItem,
        )

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        indicators = []
        _indicators = d.pop("indicators", UNSET)
        for indicators_item_data in _indicators or []:
            indicators_item = IndicatorGetObjectListGistgetObjectListGistAsCsvResponse200Type0IndicatorsItem.from_dict(
                indicators_item_data
            )

            indicators.append(indicators_item)

        indicator_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            indicators=indicators,
        )

        indicator_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return indicator_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
