from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DataElementGroupSetDimensionDataElementGroupSet")


@_attrs_define
class DataElementGroupSetDimensionDataElementGroupSet:
    """A UID reference to a DataElementGroupSet
    (Java name `org.hisp.dhis.dataelement.DataElementGroupSet`)

        Attributes:
            id (str):  Example: p5Bv16cx3Yh.
    """

    id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        data_element_group_set_dimension_data_element_group_set = cls(
            id=id,
        )

        data_element_group_set_dimension_data_element_group_set.additional_properties = d
        return data_element_group_set_dimension_data_element_group_set

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
