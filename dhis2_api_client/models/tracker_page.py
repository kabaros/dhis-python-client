from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tracker_pager import TrackerPager


T = TypeVar("T", bound="TrackerPage")


@_attrs_define
class TrackerPage:
    """
    Attributes:
        page (Union[Unset, int]):
        page_count (Union[Unset, int]):
        page_size (Union[Unset, int]):
        pager (Union[Unset, TrackerPager]):
        total (Union[Unset, int]):
    """

    page: Union[Unset, int] = UNSET
    page_count: Union[Unset, int] = UNSET
    page_size: Union[Unset, int] = UNSET
    pager: Union[Unset, "TrackerPager"] = UNSET
    total: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        page_count = self.page_count

        page_size = self.page_size

        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page is not UNSET:
            field_dict["page"] = page
        if page_count is not UNSET:
            field_dict["pageCount"] = page_count
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if pager is not UNSET:
            field_dict["pager"] = pager
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tracker_pager import TrackerPager

        d = src_dict.copy()
        page = d.pop("page", UNSET)

        page_count = d.pop("pageCount", UNSET)

        page_size = d.pop("pageSize", UNSET)

        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, TrackerPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = TrackerPager.from_dict(_pager)

        total = d.pop("total", UNSET)

        tracker_page = cls(
            page=page,
            page_count=page_count,
            page_size=page_size,
            pager=pager,
            total=total,
        )

        tracker_page.additional_properties = d
        return tracker_page

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
