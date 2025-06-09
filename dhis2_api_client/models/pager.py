from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Pager")


@_attrs_define
class Pager:
    """
    Attributes:
        page (int):
        page_count (int):
        page_size (int):
        total (int):
        next_page (Union[Unset, str]):
        prev_page (Union[Unset, str]):
    """

    page: int
    page_count: int
    page_size: int
    total: int
    next_page: Union[Unset, str] = UNSET
    prev_page: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        page_count = self.page_count

        page_size = self.page_size

        total = self.total

        next_page = self.next_page

        prev_page = self.prev_page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page": page,
                "pageCount": page_count,
                "pageSize": page_size,
                "total": total,
            }
        )
        if next_page is not UNSET:
            field_dict["nextPage"] = next_page
        if prev_page is not UNSET:
            field_dict["prevPage"] = prev_page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        page = d.pop("page")

        page_count = d.pop("pageCount")

        page_size = d.pop("pageSize")

        total = d.pop("total")

        next_page = d.pop("nextPage", UNSET)

        prev_page = d.pop("prevPage", UNSET)

        pager = cls(
            page=page,
            page_count=page_count,
            page_size=page_size,
            total=total,
            next_page=next_page,
            prev_page=prev_page,
        )

        pager.additional_properties = d
        return pager

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
