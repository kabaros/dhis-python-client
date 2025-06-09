from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrackerTrigramIndexJobParameters")


@_attrs_define
class TrackerTrigramIndexJobParameters:
    """
    Attributes:
        attributes (Union[Unset, list[str]]):
        skip_index_deletion (Union[Unset, bool]):
    """

    attributes: Union[Unset, list[str]] = UNSET
    skip_index_deletion: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes

        skip_index_deletion = self.skip_index_deletion

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if skip_index_deletion is not UNSET:
            field_dict["skipIndexDeletion"] = skip_index_deletion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        attributes = cast(list[str], d.pop("attributes", UNSET))

        skip_index_deletion = d.pop("skipIndexDeletion", UNSET)

        tracker_trigram_index_job_parameters = cls(
            attributes=attributes,
            skip_index_deletion=skip_index_deletion,
        )

        tracker_trigram_index_job_parameters.additional_properties = d
        return tracker_trigram_index_job_parameters

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
