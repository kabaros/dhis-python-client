from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MergeParams")


@_attrs_define
class MergeParams:
    """
    Attributes:
        delete_sources (Union[Unset, bool]):
        sources (Union[Unset, list[str]]):
        target (Union[Unset, str]):
    """

    delete_sources: Union[Unset, bool] = UNSET
    sources: Union[Unset, list[str]] = UNSET
    target: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delete_sources = self.delete_sources

        sources: Union[Unset, list[str]] = UNSET
        if not isinstance(self.sources, Unset):
            sources = self.sources

        target = self.target

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delete_sources is not UNSET:
            field_dict["deleteSources"] = delete_sources
        if sources is not UNSET:
            field_dict["sources"] = sources
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        delete_sources = d.pop("deleteSources", UNSET)

        sources = cast(list[str], d.pop("sources", UNSET))

        target = d.pop("target", UNSET)

        merge_params = cls(
            delete_sources=delete_sources,
            sources=sources,
            target=target,
        )

        merge_params.additional_properties = d
        return merge_params

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
