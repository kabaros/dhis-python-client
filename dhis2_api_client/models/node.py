from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.node_type import NodeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.property_ import Property


T = TypeVar("T", bound="Node")


@_attrs_define
class Node:
    """
    Attributes:
        order (int):
        type_ (NodeType):
        children (Union[Unset, list['Node']]):
        collection (Union[Unset, bool]):
        comment (Union[Unset, str]):
        complex_ (Union[Unset, bool]):
        metadata (Union[Unset, bool]):
        name (Union[Unset, str]):
        namespace (Union[Unset, str]):
        parent (Union[Unset, Node]):
        property_ (Union[Unset, Property]):
        simple (Union[Unset, bool]):
        unordered_children (Union[Unset, list['Node']]):
    """

    order: int
    type_: NodeType
    children: Union[Unset, list["Node"]] = UNSET
    collection: Union[Unset, bool] = UNSET
    comment: Union[Unset, str] = UNSET
    complex_: Union[Unset, bool] = UNSET
    metadata: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    namespace: Union[Unset, str] = UNSET
    parent: Union[Unset, "Node"] = UNSET
    property_: Union[Unset, "Property"] = UNSET
    simple: Union[Unset, bool] = UNSET
    unordered_children: Union[Unset, list["Node"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order = self.order

        type_ = self.type_.value

        children: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        collection = self.collection

        comment = self.comment

        complex_ = self.complex_

        metadata = self.metadata

        name = self.name

        namespace = self.namespace

        parent: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        property_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.property_, Unset):
            property_ = self.property_.to_dict()

        simple = self.simple

        unordered_children: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.unordered_children, Unset):
            unordered_children = []
            for unordered_children_item_data in self.unordered_children:
                unordered_children_item = unordered_children_item_data.to_dict()
                unordered_children.append(unordered_children_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order": order,
                "type": type_,
            }
        )
        if children is not UNSET:
            field_dict["children"] = children
        if collection is not UNSET:
            field_dict["collection"] = collection
        if comment is not UNSET:
            field_dict["comment"] = comment
        if complex_ is not UNSET:
            field_dict["complex"] = complex_
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if parent is not UNSET:
            field_dict["parent"] = parent
        if property_ is not UNSET:
            field_dict["property"] = property_
        if simple is not UNSET:
            field_dict["simple"] = simple
        if unordered_children is not UNSET:
            field_dict["unorderedChildren"] = unordered_children

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.property_ import Property

        d = src_dict.copy()
        order = d.pop("order")

        type_ = NodeType(d.pop("type"))

        children = []
        _children = d.pop("children", UNSET)
        for children_item_data in _children or []:
            children_item = Node.from_dict(children_item_data)

            children.append(children_item)

        collection = d.pop("collection", UNSET)

        comment = d.pop("comment", UNSET)

        complex_ = d.pop("complex", UNSET)

        metadata = d.pop("metadata", UNSET)

        name = d.pop("name", UNSET)

        namespace = d.pop("namespace", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, Node]
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = Node.from_dict(_parent)

        _property_ = d.pop("property", UNSET)
        property_: Union[Unset, Property]
        if isinstance(_property_, Unset):
            property_ = UNSET
        else:
            property_ = Property.from_dict(_property_)

        simple = d.pop("simple", UNSET)

        unordered_children = []
        _unordered_children = d.pop("unorderedChildren", UNSET)
        for unordered_children_item_data in _unordered_children or []:
            unordered_children_item = Node.from_dict(unordered_children_item_data)

            unordered_children.append(unordered_children_item)

        node = cls(
            order=order,
            type_=type_,
            children=children,
            collection=collection,
            comment=comment,
            complex_=complex_,
            metadata=metadata,
            name=name,
            namespace=namespace,
            parent=parent,
            property_=property_,
            simple=simple,
            unordered_children=unordered_children,
        )

        node.additional_properties = d
        return node

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
