from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProgramIndicatorProgramIndicatorGroupsItem")


@_attrs_define
class ProgramIndicatorProgramIndicatorGroupsItem:
    """A UID reference to a ProgramIndicatorGroup
    (Java name `org.hisp.dhis.program.ProgramIndicatorGroup`)

        Attributes:
            id (str):  Example: Do7D1Xm2NQ1.
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

        program_indicator_program_indicator_groups_item = cls(
            id=id,
        )

        program_indicator_program_indicator_groups_item.additional_properties = d
        return program_indicator_program_indicator_groups_item

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
