from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.org_unit_info import OrgUnitInfo
    from ..models.profile_item import ProfileItem


T = TypeVar("T", bound="OrgUnitProfileData")


@_attrs_define
class OrgUnitProfileData:
    """
    Attributes:
        attributes (Union[Unset, list['ProfileItem']]):
        data_items (Union[Unset, list['ProfileItem']]):
        group_sets (Union[Unset, list['ProfileItem']]):
        info (Union[Unset, OrgUnitInfo]):
    """

    attributes: Union[Unset, list["ProfileItem"]] = UNSET
    data_items: Union[Unset, list["ProfileItem"]] = UNSET
    group_sets: Union[Unset, list["ProfileItem"]] = UNSET
    info: Union[Unset, "OrgUnitInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()
                attributes.append(attributes_item)

        data_items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_items, Unset):
            data_items = []
            for data_items_item_data in self.data_items:
                data_items_item = data_items_item_data.to_dict()
                data_items.append(data_items_item)

        group_sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.group_sets, Unset):
            group_sets = []
            for group_sets_item_data in self.group_sets:
                group_sets_item = group_sets_item_data.to_dict()
                group_sets.append(group_sets_item)

        info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.info, Unset):
            info = self.info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if data_items is not UNSET:
            field_dict["dataItems"] = data_items
        if group_sets is not UNSET:
            field_dict["groupSets"] = group_sets
        if info is not UNSET:
            field_dict["info"] = info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.org_unit_info import OrgUnitInfo
        from ..models.profile_item import ProfileItem

        d = src_dict.copy()
        attributes = []
        _attributes = d.pop("attributes", UNSET)
        for attributes_item_data in _attributes or []:
            attributes_item = ProfileItem.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        data_items = []
        _data_items = d.pop("dataItems", UNSET)
        for data_items_item_data in _data_items or []:
            data_items_item = ProfileItem.from_dict(data_items_item_data)

            data_items.append(data_items_item)

        group_sets = []
        _group_sets = d.pop("groupSets", UNSET)
        for group_sets_item_data in _group_sets or []:
            group_sets_item = ProfileItem.from_dict(group_sets_item_data)

            group_sets.append(group_sets_item)

        _info = d.pop("info", UNSET)
        info: Union[Unset, OrgUnitInfo]
        if isinstance(_info, Unset):
            info = UNSET
        else:
            info = OrgUnitInfo.from_dict(_info)

        org_unit_profile_data = cls(
            attributes=attributes,
            data_items=data_items,
            group_sets=group_sets,
            info=info,
        )

        org_unit_profile_data.additional_properties = d
        return org_unit_profile_data

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
