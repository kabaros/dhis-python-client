from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GistPager")


@_attrs_define
class GistPager:
    """
    Attributes:
        page (int):
        page_size (int):
        next_page (Union[Unset, str]):
        page_count (Union[Unset, int]):
        prev_page (Union[Unset, str]):
        total (Union[Unset, int]):
    """

    page: int
    page_size: int
    next_page: Union[Unset, str] = UNSET
    page_count: Union[Unset, int] = UNSET
    prev_page: Union[Unset, str] = UNSET
    total: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        page_size = self.page_size

        next_page = self.next_page

        page_count = self.page_count

        prev_page = self.prev_page

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page": page,
                "pageSize": page_size,
            }
        )
        if next_page is not UNSET:
            field_dict["nextPage"] = next_page
        if page_count is not UNSET:
            field_dict["pageCount"] = page_count
        if prev_page is not UNSET:
            field_dict["prevPage"] = prev_page
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        page = d.pop("page")

        page_size = d.pop("pageSize")

        next_page = d.pop("nextPage", UNSET)

        page_count = d.pop("pageCount", UNSET)

        prev_page = d.pop("prevPage", UNSET)

        total = d.pop("total", UNSET)

        gist_pager = cls(
            page=page,
            page_size=page_size,
            next_page=next_page,
            page_count=page_count,
            prev_page=prev_page,
            total=total,
        )

        gist_pager.additional_properties = d
        return gist_pager

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
