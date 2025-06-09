from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApprovalDto")


@_attrs_define
class ApprovalDto:
    """
    Attributes:
        aoc (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        ou (Union[Unset, str]): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
    """

    aoc: Union[Unset, str] = UNSET
    ou: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aoc = self.aoc

        ou = self.ou

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aoc is not UNSET:
            field_dict["aoc"] = aoc
        if ou is not UNSET:
            field_dict["ou"] = ou

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        aoc = d.pop("aoc", UNSET)

        ou = d.pop("ou", UNSET)

        approval_dto = cls(
            aoc=aoc,
            ou=ou,
        )

        approval_dto.additional_properties = d
        return approval_dto

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
