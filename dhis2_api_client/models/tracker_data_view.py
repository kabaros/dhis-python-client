from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrackerDataView")


@_attrs_define
class TrackerDataView:
    """
    Attributes:
        attributes (Union[Unset, Any]): The exact type is unknown.
            (Java type was: `java.util.LinkedHashSet<java.lang.String>`)
        data_elements (Union[Unset, Any]): The exact type is unknown.
            (Java type was: `java.util.LinkedHashSet<java.lang.String>`)
    """

    attributes: Union[Unset, Any] = UNSET
    data_elements: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes = self.attributes

        data_elements = self.data_elements

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if data_elements is not UNSET:
            field_dict["dataElements"] = data_elements

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        attributes = d.pop("attributes", UNSET)

        data_elements = d.pop("dataElements", UNSET)

        tracker_data_view = cls(
            attributes=attributes,
            data_elements=data_elements,
        )

        tracker_data_view.additional_properties = d
        return tracker_data_view

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
