from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata_item import MetadataItem


T = TypeVar("T", bound="Keyword")


@_attrs_define
class Keyword:
    """
    Attributes:
        key (Union[Unset, str]):
        metadata_item (Union[Unset, MetadataItem]):
    """

    key: Union[Unset, str] = UNSET
    metadata_item: Union[Unset, "MetadataItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        metadata_item: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata_item, Unset):
            metadata_item = self.metadata_item.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if metadata_item is not UNSET:
            field_dict["metadataItem"] = metadata_item

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.metadata_item import MetadataItem

        d = src_dict.copy()
        key = d.pop("key", UNSET)

        _metadata_item = d.pop("metadataItem", UNSET)
        metadata_item: Union[Unset, MetadataItem]
        if isinstance(_metadata_item, Unset):
            metadata_item = UNSET
        else:
            metadata_item = MetadataItem.from_dict(_metadata_item)

        keyword = cls(
            key=key,
            metadata_item=metadata_item,
        )

        keyword.additional_properties = d
        return keyword

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
