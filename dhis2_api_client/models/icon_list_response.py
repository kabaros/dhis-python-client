from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.icon_list_response_icons_item import IconListResponseIconsItem
    from ..models.pager import Pager


T = TypeVar("T", bound="IconListResponse")


@_attrs_define
class IconListResponse:
    """
    Attributes:
        icons (Union[Unset, list['IconListResponseIconsItem']]):
        pager (Union[Unset, Pager]):
    """

    icons: Union[Unset, list["IconListResponseIconsItem"]] = UNSET
    pager: Union[Unset, "Pager"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        icons: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.icons, Unset):
            icons = []
            for icons_item_data in self.icons:
                icons_item = icons_item_data.to_dict()
                icons.append(icons_item)

        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if icons is not UNSET:
            field_dict["icons"] = icons
        if pager is not UNSET:
            field_dict["pager"] = pager

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.icon_list_response_icons_item import IconListResponseIconsItem
        from ..models.pager import Pager

        d = src_dict.copy()
        icons = []
        _icons = d.pop("icons", UNSET)
        for icons_item_data in _icons or []:
            icons_item = IconListResponseIconsItem.from_dict(icons_item_data)

            icons.append(icons_item)

        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, Pager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = Pager.from_dict(_pager)

        icon_list_response = cls(
            icons=icons,
            pager=pager,
        )

        icon_list_response.additional_properties = d
        return icon_list_response

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
