from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pager import Pager
    from ..models.tracked_entity_type import TrackedEntityType


T = TypeVar("T", bound="TrackedEntityTypeGetObjectListResponse200")


@_attrs_define
class TrackedEntityTypeGetObjectListResponse200:
    """
    Attributes:
        pager (Union[Unset, Pager]):
        tracked_entity_types (Union[Unset, list['TrackedEntityType']]):
    """

    pager: Union[Unset, "Pager"] = UNSET
    tracked_entity_types: Union[Unset, list["TrackedEntityType"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        tracked_entity_types: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tracked_entity_types, Unset):
            tracked_entity_types = []
            for tracked_entity_types_item_data in self.tracked_entity_types:
                tracked_entity_types_item = tracked_entity_types_item_data.to_dict()
                tracked_entity_types.append(tracked_entity_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if tracked_entity_types is not UNSET:
            field_dict["trackedEntityTypes"] = tracked_entity_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.pager import Pager
        from ..models.tracked_entity_type import TrackedEntityType

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, Pager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = Pager.from_dict(_pager)

        tracked_entity_types = []
        _tracked_entity_types = d.pop("trackedEntityTypes", UNSET)
        for tracked_entity_types_item_data in _tracked_entity_types or []:
            tracked_entity_types_item = TrackedEntityType.from_dict(tracked_entity_types_item_data)

            tracked_entity_types.append(tracked_entity_types_item)

        tracked_entity_type_get_object_list_response_200 = cls(
            pager=pager,
            tracked_entity_types=tracked_entity_types,
        )

        tracked_entity_type_get_object_list_response_200.additional_properties = d
        return tracked_entity_type_get_object_list_response_200

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
