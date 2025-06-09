from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.index_resource import IndexResource


T = TypeVar("T", bound="IndexResources")


@_attrs_define
class IndexResources:
    """
    Attributes:
        resources (Union[Unset, list['IndexResource']]):
    """

    resources: Union[Unset, list["IndexResource"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resources: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.resources, Unset):
            resources = []
            for resources_item_data in self.resources:
                resources_item = resources_item_data.to_dict()
                resources.append(resources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resources is not UNSET:
            field_dict["resources"] = resources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.index_resource import IndexResource

        d = src_dict.copy()
        resources = []
        _resources = d.pop("resources", UNSET)
        for resources_item_data in _resources or []:
            resources_item = IndexResource.from_dict(resources_item_data)

            resources.append(resources_item)

        index_resources = cls(
            resources=resources,
        )

        index_resources.additional_properties = d
        return index_resources

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
