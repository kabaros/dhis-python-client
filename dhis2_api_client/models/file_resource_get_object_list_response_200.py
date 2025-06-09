from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_resource import FileResource
    from ..models.pager import Pager


T = TypeVar("T", bound="FileResourceGetObjectListResponse200")


@_attrs_define
class FileResourceGetObjectListResponse200:
    """
    Attributes:
        pager (Union[Unset, Pager]):
        file_resources (Union[Unset, list['FileResource']]):
    """

    pager: Union[Unset, "Pager"] = UNSET
    file_resources: Union[Unset, list["FileResource"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        file_resources: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.file_resources, Unset):
            file_resources = []
            for file_resources_item_data in self.file_resources:
                file_resources_item = file_resources_item_data.to_dict()
                file_resources.append(file_resources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if file_resources is not UNSET:
            field_dict["fileResources"] = file_resources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.file_resource import FileResource
        from ..models.pager import Pager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, Pager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = Pager.from_dict(_pager)

        file_resources = []
        _file_resources = d.pop("fileResources", UNSET)
        for file_resources_item_data in _file_resources or []:
            file_resources_item = FileResource.from_dict(file_resources_item_data)

            file_resources.append(file_resources_item)

        file_resource_get_object_list_response_200 = cls(
            pager=pager,
            file_resources=file_resources,
        )

        file_resource_get_object_list_response_200.additional_properties = d
        return file_resource_get_object_list_response_200

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
