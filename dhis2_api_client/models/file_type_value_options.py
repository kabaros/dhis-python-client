from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileTypeValueOptions")


@_attrs_define
class FileTypeValueOptions:
    """
    Attributes:
        max_file_size (int):
        version (int):
        allowed_content_types (Union[Unset, list[str]]):
    """

    max_file_size: int
    version: int
    allowed_content_types: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_file_size = self.max_file_size

        version = self.version

        allowed_content_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allowed_content_types, Unset):
            allowed_content_types = self.allowed_content_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "maxFileSize": max_file_size,
                "version": version,
            }
        )
        if allowed_content_types is not UNSET:
            field_dict["allowedContentTypes"] = allowed_content_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        max_file_size = d.pop("maxFileSize")

        version = d.pop("version")

        allowed_content_types = cast(list[str], d.pop("allowedContentTypes", UNSET))

        file_type_value_options = cls(
            max_file_size=max_file_size,
            version=version,
            allowed_content_types=allowed_content_types,
        )

        file_type_value_options.additional_properties = d
        return file_type_value_options

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
