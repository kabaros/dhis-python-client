from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyword import Keyword


T = TypeVar("T", bound="DimensionItemKeywords")


@_attrs_define
class DimensionItemKeywords:
    """
    Attributes:
        empty (Union[Unset, bool]):
        keywords (Union[Unset, list['Keyword']]):
    """

    empty: Union[Unset, bool] = UNSET
    keywords: Union[Unset, list["Keyword"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        empty = self.empty

        keywords: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = []
            for keywords_item_data in self.keywords:
                keywords_item = keywords_item_data.to_dict()
                keywords.append(keywords_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if empty is not UNSET:
            field_dict["empty"] = empty
        if keywords is not UNSET:
            field_dict["keywords"] = keywords

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.keyword import Keyword

        d = src_dict.copy()
        empty = d.pop("empty", UNSET)

        keywords = []
        _keywords = d.pop("keywords", UNSET)
        for keywords_item_data in _keywords or []:
            keywords_item = Keyword.from_dict(keywords_item_data)

            keywords.append(keywords_item)

        dimension_item_keywords = cls(
            empty=empty,
            keywords=keywords,
        )

        dimension_item_keywords.additional_properties = d
        return dimension_item_keywords

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
