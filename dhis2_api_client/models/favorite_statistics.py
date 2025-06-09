import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FavoriteStatistics")


@_attrs_define
class FavoriteStatistics:
    """
    Attributes:
        created (Union[Unset, datetime.datetime]):
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        position (Union[Unset, int]):
        views (Union[Unset, int]):
    """

    created: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    position: Union[Unset, int] = UNSET
    views: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        id = self.id

        name = self.name

        position = self.position

        views = self.views

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if position is not UNSET:
            field_dict["position"] = position
        if views is not UNSET:
            field_dict["views"] = views

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        position = d.pop("position", UNSET)

        views = d.pop("views", UNSET)

        favorite_statistics = cls(
            created=created,
            id=id,
            name=name,
            position=position,
            views=views,
        )

        favorite_statistics.additional_properties = d
        return favorite_statistics

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
