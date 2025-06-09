from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entries_response_entries_item import EntriesResponseEntriesItem
    from ..models.entries_response_pager import EntriesResponsePager


T = TypeVar("T", bound="EntriesResponse")


@_attrs_define
class EntriesResponse:
    """
    Attributes:
        entries (Union[Unset, list['EntriesResponseEntriesItem']]):
        pager (Union[Unset, EntriesResponsePager]):
    """

    entries: Union[Unset, list["EntriesResponseEntriesItem"]] = UNSET
    pager: Union[Unset, "EntriesResponsePager"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entries is not UNSET:
            field_dict["entries"] = entries
        if pager is not UNSET:
            field_dict["pager"] = pager

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.entries_response_entries_item import EntriesResponseEntriesItem
        from ..models.entries_response_pager import EntriesResponsePager

        d = src_dict.copy()
        entries = []
        _entries = d.pop("entries", UNSET)
        for entries_item_data in _entries or []:
            entries_item = EntriesResponseEntriesItem.from_dict(entries_item_data)

            entries.append(entries_item)

        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, EntriesResponsePager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = EntriesResponsePager.from_dict(_pager)

        entries_response = cls(
            entries=entries,
            pager=pager,
        )

        entries_response.additional_properties = d
        return entries_response

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
