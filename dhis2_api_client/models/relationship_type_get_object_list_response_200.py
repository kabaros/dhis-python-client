from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pager import Pager
    from ..models.relationship_type import RelationshipType


T = TypeVar("T", bound="RelationshipTypeGetObjectListResponse200")


@_attrs_define
class RelationshipTypeGetObjectListResponse200:
    """
    Attributes:
        pager (Union[Unset, Pager]):
        relationship_types (Union[Unset, list['RelationshipType']]):
    """

    pager: Union[Unset, "Pager"] = UNSET
    relationship_types: Union[Unset, list["RelationshipType"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        relationship_types: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.relationship_types, Unset):
            relationship_types = []
            for relationship_types_item_data in self.relationship_types:
                relationship_types_item = relationship_types_item_data.to_dict()
                relationship_types.append(relationship_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if relationship_types is not UNSET:
            field_dict["relationshipTypes"] = relationship_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.pager import Pager
        from ..models.relationship_type import RelationshipType

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, Pager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = Pager.from_dict(_pager)

        relationship_types = []
        _relationship_types = d.pop("relationshipTypes", UNSET)
        for relationship_types_item_data in _relationship_types or []:
            relationship_types_item = RelationshipType.from_dict(relationship_types_item_data)

            relationship_types.append(relationship_types_item)

        relationship_type_get_object_list_response_200 = cls(
            pager=pager,
            relationship_types=relationship_types,
        )

        relationship_type_get_object_list_response_200.additional_properties = d
        return relationship_type_get_object_list_response_200

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
