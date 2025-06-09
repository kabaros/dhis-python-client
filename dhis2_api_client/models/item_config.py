from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.item_config_insert_position import ItemConfigInsertPosition
from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemConfig")


@_attrs_define
class ItemConfig:
    """
    Attributes:
        insert_position (ItemConfigInsertPosition):
        insert_height (Union[Unset, int]):
    """

    insert_position: ItemConfigInsertPosition
    insert_height: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        insert_position = self.insert_position.value

        insert_height = self.insert_height

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "insertPosition": insert_position,
            }
        )
        if insert_height is not UNSET:
            field_dict["insertHeight"] = insert_height

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        insert_position = ItemConfigInsertPosition(d.pop("insertPosition"))

        insert_height = d.pop("insertHeight", UNSET)

        item_config = cls(
            insert_position=insert_position,
            insert_height=insert_height,
        )

        item_config.additional_properties = d
        return item_config

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
