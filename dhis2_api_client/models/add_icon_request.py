from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddIconRequest")


@_attrs_define
class AddIconRequest:
    """
    Attributes:
        file_resource_id (str):
        key (str):
        description (Union[Unset, str]):
        keywords (Union[Unset, list[str]]):
    """

    file_resource_id: str
    key: str
    description: Union[Unset, str] = UNSET
    keywords: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_resource_id = self.file_resource_id

        key = self.key

        description = self.description

        keywords: Union[Unset, list[str]] = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fileResourceId": file_resource_id,
                "key": key,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if keywords is not UNSET:
            field_dict["keywords"] = keywords

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        file_resource_id = d.pop("fileResourceId")

        key = d.pop("key")

        description = d.pop("description", UNSET)

        keywords = cast(list[str], d.pop("keywords", UNSET))

        add_icon_request = cls(
            file_resource_id=file_resource_id,
            key=key,
            description=description,
            keywords=keywords,
        )

        add_icon_request.additional_properties = d
        return add_icon_request

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
