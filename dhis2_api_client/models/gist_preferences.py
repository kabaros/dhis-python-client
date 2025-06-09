from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gist_preferences_included import GistPreferencesIncluded
from ..models.gist_preferences_transformation import GistPreferencesTransformation

T = TypeVar("T", bound="GistPreferences")


@_attrs_define
class GistPreferences:
    """
    Attributes:
        included (GistPreferencesIncluded):
        transformation (GistPreferencesTransformation):
    """

    included: GistPreferencesIncluded
    transformation: GistPreferencesTransformation
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        included = self.included.value

        transformation = self.transformation.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "included": included,
                "transformation": transformation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        included = GistPreferencesIncluded(d.pop("included"))

        transformation = GistPreferencesTransformation(d.pop("transformation"))

        gist_preferences = cls(
            included=included,
            transformation=transformation,
        )

        gist_preferences.additional_properties = d
        return gist_preferences

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
