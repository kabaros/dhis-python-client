from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deprecated_tracker_relationship_item import DeprecatedTrackerRelationshipItem


T = TypeVar("T", bound="DeprecatedTrackerRelationship")


@_attrs_define
class DeprecatedTrackerRelationship:
    """
    Attributes:
        bidirectional (Union[Unset, bool]):
        created (Union[Unset, str]):
        from_ (Union[Unset, DeprecatedTrackerRelationshipItem]):
        last_updated (Union[Unset, str]):
        relationship (Union[Unset, str]):
        relationship_name (Union[Unset, str]):
        relationship_type (Union[Unset, str]):
        to (Union[Unset, DeprecatedTrackerRelationshipItem]):
    """

    bidirectional: Union[Unset, bool] = UNSET
    created: Union[Unset, str] = UNSET
    from_: Union[Unset, "DeprecatedTrackerRelationshipItem"] = UNSET
    last_updated: Union[Unset, str] = UNSET
    relationship: Union[Unset, str] = UNSET
    relationship_name: Union[Unset, str] = UNSET
    relationship_type: Union[Unset, str] = UNSET
    to: Union[Unset, "DeprecatedTrackerRelationshipItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bidirectional = self.bidirectional

        created = self.created

        from_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        last_updated = self.last_updated

        relationship = self.relationship

        relationship_name = self.relationship_name

        relationship_type = self.relationship_type

        to: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bidirectional is not UNSET:
            field_dict["bidirectional"] = bidirectional
        if created is not UNSET:
            field_dict["created"] = created
        if from_ is not UNSET:
            field_dict["from"] = from_
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if relationship is not UNSET:
            field_dict["relationship"] = relationship
        if relationship_name is not UNSET:
            field_dict["relationshipName"] = relationship_name
        if relationship_type is not UNSET:
            field_dict["relationshipType"] = relationship_type
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.deprecated_tracker_relationship_item import DeprecatedTrackerRelationshipItem

        d = src_dict.copy()
        bidirectional = d.pop("bidirectional", UNSET)

        created = d.pop("created", UNSET)

        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, DeprecatedTrackerRelationshipItem]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = DeprecatedTrackerRelationshipItem.from_dict(_from_)

        last_updated = d.pop("lastUpdated", UNSET)

        relationship = d.pop("relationship", UNSET)

        relationship_name = d.pop("relationshipName", UNSET)

        relationship_type = d.pop("relationshipType", UNSET)

        _to = d.pop("to", UNSET)
        to: Union[Unset, DeprecatedTrackerRelationshipItem]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = DeprecatedTrackerRelationshipItem.from_dict(_to)

        deprecated_tracker_relationship = cls(
            bidirectional=bidirectional,
            created=created,
            from_=from_,
            last_updated=last_updated,
            relationship=relationship,
            relationship_name=relationship_name,
            relationship_type=relationship_type,
            to=to,
        )

        deprecated_tracker_relationship.additional_properties = d
        return deprecated_tracker_relationship

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
