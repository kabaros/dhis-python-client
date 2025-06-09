from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_resource_owner_domain import FileResourceOwnerDomain
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileResourceOwner")


@_attrs_define
class FileResourceOwner:
    """
    Attributes:
        domain (FileResourceOwnerDomain):
        co (Union[Unset, str]):
        de (Union[Unset, str]):
        id (Union[Unset, str]):
        ou (Union[Unset, str]):
        pe (Union[Unset, str]):
    """

    domain: FileResourceOwnerDomain
    co: Union[Unset, str] = UNSET
    de: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    ou: Union[Unset, str] = UNSET
    pe: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain.value

        co = self.co

        de = self.de

        id = self.id

        ou = self.ou

        pe = self.pe

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain": domain,
            }
        )
        if co is not UNSET:
            field_dict["co"] = co
        if de is not UNSET:
            field_dict["de"] = de
        if id is not UNSET:
            field_dict["id"] = id
        if ou is not UNSET:
            field_dict["ou"] = ou
        if pe is not UNSET:
            field_dict["pe"] = pe

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        domain = FileResourceOwnerDomain(d.pop("domain"))

        co = d.pop("co", UNSET)

        de = d.pop("de", UNSET)

        id = d.pop("id", UNSET)

        ou = d.pop("ou", UNSET)

        pe = d.pop("pe", UNSET)

        file_resource_owner = cls(
            domain=domain,
            co=co,
            de=de,
            id=id,
            ou=ou,
            pe=pe,
        )

        file_resource_owner.additional_properties = d
        return file_resource_owner

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
