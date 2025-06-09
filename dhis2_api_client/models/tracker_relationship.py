import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tracker_relationship_item import TrackerRelationshipItem


T = TypeVar("T", bound="TrackerRelationship")


@_attrs_define
class TrackerRelationship:
    """
    Attributes:
        bidirectional (Union[Unset, bool]):
        created_at (Union[Unset, datetime.datetime, int]):
        created_at_client (Union[Unset, datetime.datetime, int]):
        from_ (Union[Unset, TrackerRelationshipItem]):
        relationship (Union[Unset, str]): A UID for an TrackerRelationship object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Relationship`) Example: w2mo4Wf3JL2.
        relationship_name (Union[Unset, str]):
        relationship_type (Union[Unset, str]): A UID for an RelationshipType object
            (Java name `org.hisp.dhis.relationship.RelationshipType`) Example: A6qs80jv0P3.
        to (Union[Unset, TrackerRelationshipItem]):
        updated_at (Union[Unset, datetime.datetime, int]):
    """

    bidirectional: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime, int] = UNSET
    created_at_client: Union[Unset, datetime.datetime, int] = UNSET
    from_: Union[Unset, "TrackerRelationshipItem"] = UNSET
    relationship: Union[Unset, str] = UNSET
    relationship_name: Union[Unset, str] = UNSET
    relationship_type: Union[Unset, str] = UNSET
    to: Union[Unset, "TrackerRelationshipItem"] = UNSET
    updated_at: Union[Unset, datetime.datetime, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bidirectional = self.bidirectional

        created_at: Union[Unset, int, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        created_at_client: Union[Unset, int, str]
        if isinstance(self.created_at_client, Unset):
            created_at_client = UNSET
        elif isinstance(self.created_at_client, datetime.datetime):
            created_at_client = self.created_at_client.isoformat()
        else:
            created_at_client = self.created_at_client

        from_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        relationship = self.relationship

        relationship_name = self.relationship_name

        relationship_type = self.relationship_type

        to: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        updated_at: Union[Unset, int, str]
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bidirectional is not UNSET:
            field_dict["bidirectional"] = bidirectional
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_at_client is not UNSET:
            field_dict["createdAtClient"] = created_at_client
        if from_ is not UNSET:
            field_dict["from"] = from_
        if relationship is not UNSET:
            field_dict["relationship"] = relationship
        if relationship_name is not UNSET:
            field_dict["relationshipName"] = relationship_name
        if relationship_type is not UNSET:
            field_dict["relationshipType"] = relationship_type
        if to is not UNSET:
            field_dict["to"] = to
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tracker_relationship_item import TrackerRelationshipItem

        d = src_dict.copy()
        bidirectional = d.pop("bidirectional", UNSET)

        def _parse_created_at(data: object) -> Union[Unset, datetime.datetime, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)

                return created_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Unset, datetime.datetime, int], data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))

        def _parse_created_at_client(data: object) -> Union[Unset, datetime.datetime, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_client_type_0 = isoparse(data)

                return created_at_client_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Unset, datetime.datetime, int], data)

        created_at_client = _parse_created_at_client(d.pop("createdAtClient", UNSET))

        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, TrackerRelationshipItem]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = TrackerRelationshipItem.from_dict(_from_)

        relationship = d.pop("relationship", UNSET)

        relationship_name = d.pop("relationshipName", UNSET)

        relationship_type = d.pop("relationshipType", UNSET)

        _to = d.pop("to", UNSET)
        to: Union[Unset, TrackerRelationshipItem]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = TrackerRelationshipItem.from_dict(_to)

        def _parse_updated_at(data: object) -> Union[Unset, datetime.datetime, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Unset, datetime.datetime, int], data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))

        tracker_relationship = cls(
            bidirectional=bidirectional,
            created_at=created_at,
            created_at_client=created_at_client,
            from_=from_,
            relationship=relationship,
            relationship_name=relationship_name,
            relationship_type=relationship_type,
            to=to,
            updated_at=updated_at,
        )

        tracker_relationship.additional_properties = d
        return tracker_relationship

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
