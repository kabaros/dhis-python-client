from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.indicator_group import IndicatorGroup
    from ..models.pager import Pager


T = TypeVar("T", bound="IndicatorGroupGetObjectListResponse200")


@_attrs_define
class IndicatorGroupGetObjectListResponse200:
    """
    Attributes:
        pager (Union[Unset, Pager]):
        indicator_groups (Union[Unset, list['IndicatorGroup']]):
    """

    pager: Union[Unset, "Pager"] = UNSET
    indicator_groups: Union[Unset, list["IndicatorGroup"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        indicator_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.indicator_groups, Unset):
            indicator_groups = []
            for indicator_groups_item_data in self.indicator_groups:
                indicator_groups_item = indicator_groups_item_data.to_dict()
                indicator_groups.append(indicator_groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if indicator_groups is not UNSET:
            field_dict["indicatorGroups"] = indicator_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.indicator_group import IndicatorGroup
        from ..models.pager import Pager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, Pager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = Pager.from_dict(_pager)

        indicator_groups = []
        _indicator_groups = d.pop("indicatorGroups", UNSET)
        for indicator_groups_item_data in _indicator_groups or []:
            indicator_groups_item = IndicatorGroup.from_dict(indicator_groups_item_data)

            indicator_groups.append(indicator_groups_item)

        indicator_group_get_object_list_response_200 = cls(
            pager=pager,
            indicator_groups=indicator_groups,
        )

        indicator_group_get_object_list_response_200.additional_properties = d
        return indicator_group_get_object_list_response_200

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
