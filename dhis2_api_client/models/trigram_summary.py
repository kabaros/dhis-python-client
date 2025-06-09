from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trigram_summary_indexable_attributes_item import TrigramSummaryIndexableAttributesItem
    from ..models.trigram_summary_indexed_attributes_item import TrigramSummaryIndexedAttributesItem
    from ..models.trigram_summary_obsolete_indexed_attributes_item import TrigramSummaryObsoleteIndexedAttributesItem


T = TypeVar("T", bound="TrigramSummary")


@_attrs_define
class TrigramSummary:
    """
    Attributes:
        indexable_attributes (Union[Unset, list['TrigramSummaryIndexableAttributesItem']]):
        indexed_attributes (Union[Unset, list['TrigramSummaryIndexedAttributesItem']]):
        obsolete_indexed_attributes (Union[Unset, list['TrigramSummaryObsoleteIndexedAttributesItem']]):
    """

    indexable_attributes: Union[Unset, list["TrigramSummaryIndexableAttributesItem"]] = UNSET
    indexed_attributes: Union[Unset, list["TrigramSummaryIndexedAttributesItem"]] = UNSET
    obsolete_indexed_attributes: Union[Unset, list["TrigramSummaryObsoleteIndexedAttributesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        indexable_attributes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.indexable_attributes, Unset):
            indexable_attributes = []
            for indexable_attributes_item_data in self.indexable_attributes:
                indexable_attributes_item = indexable_attributes_item_data.to_dict()
                indexable_attributes.append(indexable_attributes_item)

        indexed_attributes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.indexed_attributes, Unset):
            indexed_attributes = []
            for indexed_attributes_item_data in self.indexed_attributes:
                indexed_attributes_item = indexed_attributes_item_data.to_dict()
                indexed_attributes.append(indexed_attributes_item)

        obsolete_indexed_attributes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.obsolete_indexed_attributes, Unset):
            obsolete_indexed_attributes = []
            for obsolete_indexed_attributes_item_data in self.obsolete_indexed_attributes:
                obsolete_indexed_attributes_item = obsolete_indexed_attributes_item_data.to_dict()
                obsolete_indexed_attributes.append(obsolete_indexed_attributes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if indexable_attributes is not UNSET:
            field_dict["indexableAttributes"] = indexable_attributes
        if indexed_attributes is not UNSET:
            field_dict["indexedAttributes"] = indexed_attributes
        if obsolete_indexed_attributes is not UNSET:
            field_dict["obsoleteIndexedAttributes"] = obsolete_indexed_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.trigram_summary_indexable_attributes_item import TrigramSummaryIndexableAttributesItem
        from ..models.trigram_summary_indexed_attributes_item import TrigramSummaryIndexedAttributesItem
        from ..models.trigram_summary_obsolete_indexed_attributes_item import (
            TrigramSummaryObsoleteIndexedAttributesItem,
        )

        d = src_dict.copy()
        indexable_attributes = []
        _indexable_attributes = d.pop("indexableAttributes", UNSET)
        for indexable_attributes_item_data in _indexable_attributes or []:
            indexable_attributes_item = TrigramSummaryIndexableAttributesItem.from_dict(indexable_attributes_item_data)

            indexable_attributes.append(indexable_attributes_item)

        indexed_attributes = []
        _indexed_attributes = d.pop("indexedAttributes", UNSET)
        for indexed_attributes_item_data in _indexed_attributes or []:
            indexed_attributes_item = TrigramSummaryIndexedAttributesItem.from_dict(indexed_attributes_item_data)

            indexed_attributes.append(indexed_attributes_item)

        obsolete_indexed_attributes = []
        _obsolete_indexed_attributes = d.pop("obsoleteIndexedAttributes", UNSET)
        for obsolete_indexed_attributes_item_data in _obsolete_indexed_attributes or []:
            obsolete_indexed_attributes_item = TrigramSummaryObsoleteIndexedAttributesItem.from_dict(
                obsolete_indexed_attributes_item_data
            )

            obsolete_indexed_attributes.append(obsolete_indexed_attributes_item)

        trigram_summary = cls(
            indexable_attributes=indexable_attributes,
            indexed_attributes=indexed_attributes,
            obsolete_indexed_attributes=obsolete_indexed_attributes,
        )

        trigram_summary.additional_properties = d
        return trigram_summary

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
