from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identifiable_objects_additions_item import IdentifiableObjectsAdditionsItem
    from ..models.identifiable_objects_deletions_item import IdentifiableObjectsDeletionsItem
    from ..models.identifiable_objects_identifiable_objects_item import IdentifiableObjectsIdentifiableObjectsItem


T = TypeVar("T", bound="IdentifiableObjects")


@_attrs_define
class IdentifiableObjects:
    """
    Attributes:
        additions (Union[Unset, list['IdentifiableObjectsAdditionsItem']]):
        deletions (Union[Unset, list['IdentifiableObjectsDeletionsItem']]):
        identifiable_objects (Union[Unset, list['IdentifiableObjectsIdentifiableObjectsItem']]):
    """

    additions: Union[Unset, list["IdentifiableObjectsAdditionsItem"]] = UNSET
    deletions: Union[Unset, list["IdentifiableObjectsDeletionsItem"]] = UNSET
    identifiable_objects: Union[Unset, list["IdentifiableObjectsIdentifiableObjectsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.additions, Unset):
            additions = []
            for additions_item_data in self.additions:
                additions_item = additions_item_data.to_dict()
                additions.append(additions_item)

        deletions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.deletions, Unset):
            deletions = []
            for deletions_item_data in self.deletions:
                deletions_item = deletions_item_data.to_dict()
                deletions.append(deletions_item)

        identifiable_objects: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.identifiable_objects, Unset):
            identifiable_objects = []
            for identifiable_objects_item_data in self.identifiable_objects:
                identifiable_objects_item = identifiable_objects_item_data.to_dict()
                identifiable_objects.append(identifiable_objects_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additions is not UNSET:
            field_dict["additions"] = additions
        if deletions is not UNSET:
            field_dict["deletions"] = deletions
        if identifiable_objects is not UNSET:
            field_dict["identifiableObjects"] = identifiable_objects

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.identifiable_objects_additions_item import IdentifiableObjectsAdditionsItem
        from ..models.identifiable_objects_deletions_item import IdentifiableObjectsDeletionsItem
        from ..models.identifiable_objects_identifiable_objects_item import IdentifiableObjectsIdentifiableObjectsItem

        d = src_dict.copy()
        additions = []
        _additions = d.pop("additions", UNSET)
        for additions_item_data in _additions or []:
            additions_item = IdentifiableObjectsAdditionsItem.from_dict(additions_item_data)

            additions.append(additions_item)

        deletions = []
        _deletions = d.pop("deletions", UNSET)
        for deletions_item_data in _deletions or []:
            deletions_item = IdentifiableObjectsDeletionsItem.from_dict(deletions_item_data)

            deletions.append(deletions_item)

        identifiable_objects = []
        _identifiable_objects = d.pop("identifiableObjects", UNSET)
        for identifiable_objects_item_data in _identifiable_objects or []:
            identifiable_objects_item = IdentifiableObjectsIdentifiableObjectsItem.from_dict(
                identifiable_objects_item_data
            )

            identifiable_objects.append(identifiable_objects_item)

        identifiable_objects = cls(
            additions=additions,
            deletions=deletions,
            identifiable_objects=identifiable_objects,
        )

        identifiable_objects.additional_properties = d
        return identifiable_objects

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
