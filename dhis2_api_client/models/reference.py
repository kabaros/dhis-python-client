from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reference_node import ReferenceNode


T = TypeVar("T", bound="Reference")


@_attrs_define
class Reference:
    """
    Attributes:
        node (Union[Unset, ReferenceNode]):
        uuid (Union[Unset, str]):
    """

    node: Union[Unset, "ReferenceNode"] = UNSET
    uuid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.node, Unset):
            node = self.node.to_dict()

        uuid = self.uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node is not UNSET:
            field_dict["node"] = node
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.reference_node import ReferenceNode

        d = src_dict.copy()
        _node = d.pop("node", UNSET)
        node: Union[Unset, ReferenceNode]
        if isinstance(_node, Unset):
            node = UNSET
        else:
            node = ReferenceNode.from_dict(_node)

        uuid = d.pop("uuid", UNSET)

        reference = cls(
            node=node,
            uuid=uuid,
        )

        reference.additional_properties = d
        return reference

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
