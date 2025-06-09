from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gist_pager import GistPager
    from ..models.tracked_entity_attribute_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_tracked_entity_attributes_item import (
        TrackedEntityAttributeGetObjectListGistgetObjectListGistAsCsvResponse200Type0TrackedEntityAttributesItem,
    )


T = TypeVar("T", bound="TrackedEntityAttributeGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class TrackedEntityAttributeGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        tracked_entity_attributes (Union[Unset, list['TrackedEntityAttributeGetObjectListGistgetObjectListGistAsCsvRespo
            nse200Type0TrackedEntityAttributesItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    tracked_entity_attributes: Union[
        Unset,
        list[
            "TrackedEntityAttributeGetObjectListGistgetObjectListGistAsCsvResponse200Type0TrackedEntityAttributesItem"
        ],
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        tracked_entity_attributes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tracked_entity_attributes, Unset):
            tracked_entity_attributes = []
            for tracked_entity_attributes_item_data in self.tracked_entity_attributes:
                tracked_entity_attributes_item = tracked_entity_attributes_item_data.to_dict()
                tracked_entity_attributes.append(tracked_entity_attributes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if tracked_entity_attributes is not UNSET:
            field_dict["trackedEntityAttributes"] = tracked_entity_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.gist_pager import GistPager
        from ..models.tracked_entity_attribute_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_tracked_entity_attributes_item import (
            TrackedEntityAttributeGetObjectListGistgetObjectListGistAsCsvResponse200Type0TrackedEntityAttributesItem,
        )

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        tracked_entity_attributes = []
        _tracked_entity_attributes = d.pop("trackedEntityAttributes", UNSET)
        for tracked_entity_attributes_item_data in _tracked_entity_attributes or []:
            tracked_entity_attributes_item = TrackedEntityAttributeGetObjectListGistgetObjectListGistAsCsvResponse200Type0TrackedEntityAttributesItem.from_dict(
                tracked_entity_attributes_item_data
            )

            tracked_entity_attributes.append(tracked_entity_attributes_item)

        tracked_entity_attribute_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            tracked_entity_attributes=tracked_entity_attributes,
        )

        tracked_entity_attribute_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return tracked_entity_attribute_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
